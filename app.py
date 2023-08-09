import openai
import gradio as gr
from prompts import prompt_chat_response
from fewshot import FewShot4UAVs

fewshot = FewShot4UAVs()


def transcribe(audio):
    messages = [
        {"role": "system",
         "content": prompt_chat_response}
    ]

    user_transcript = get_audio_transcript(audio, messages)
    uav_command = get_uav_command(user_transcript, messages)
    uav_response = get_uav_response(messages)

    # command, location = parse_command(uav_command)
    # send_command(command, location)

    chat_transcript = build_chat_transcript(user_transcript, uav_command, uav_response)

    return chat_transcript


def get_audio_transcript(audio, messages):
    audio_file = open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    user_transcript = transcript["text"]
    messages.append({"role": "user", "content": user_transcript, "name": "Operator"})
    return user_transcript


def get_uav_command(user_transcript, messages):
    uav_command = fewshot.get_command(user_transcript)
    messages.append({"role": "function", "content": uav_command, "name": "UAV"})
    return uav_command


def get_uav_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    uav_response = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": uav_response, "name": "Assistant"})
    return uav_response


def build_chat_transcript(user_transcript, uav_command, uav_response):
    messages = [
        {"role": "system", "content": prompt_chat_response},
        {"role": "user", "content": user_transcript, "name": "Operator"},
        {"role": "function", "content": uav_command, "name": "UAV"},
        {"role": "assistant", "content": uav_response, "name": "Assistant"}
    ]

    chat_transcript = ""
    for message in messages:
        if message['role'] != 'system':
            chat_transcript += f"{message['name']}: {message['content']} \n\n"

    return chat_transcript


with gr.Blocks(theme='sudeepshouche/minimalist') as demo:
    gr.Markdown("""
    # Conversational UAV Explorer
    Press record and speak into the microphone to give a command. Make sure to stop recording before pressing "Give Command."\n\n
    Commands: Take picture, Go to, Land, Take off""")
    with gr.Row():
        audio_input = gr.Audio(source="microphone", type="filepath")
        output = gr.Textbox(label="Transcript")
    with gr.Row():
        with gr.Column():
            submit_btn = gr.Button("Give command", variant="primary")
            submit_btn.click(fn=transcribe, inputs=audio_input, outputs=output, api_name="record")
    with gr.Accordion("Examples:"):
        gr.Markdown("Take a picture of the second floor of the green house.\n\n"
                    "Go to the brick house across the street.\n\n"
                    "Head to Libby Hill Park on E Franklin St.\n\n"
                    "Check out the Whole Foods on W Broad St.\n\n"
                    "Take off.\n\n"
                    "Land.")

demo.queue(concurrency_count=4)
demo.launch()
