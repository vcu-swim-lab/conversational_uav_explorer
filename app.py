import openai
import gradio as gr
from prompts import prompt_chat_response
from fewshot import FewShot4UAVs

openai.api_key = "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"

fewshot = FewShot4UAVs()


def transcribe(audio):
    messages = [
        {"role": "system",
         "content": prompt_chat_response}
    ]

    audio_file = open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    original_transcript = transcript["text"]
    messages.append({"role": "user", "content": original_transcript, "name": "Operator"})

    formatted_command_text = fewshot.get_command(original_transcript)
    messages.append({"role": "function", "content": formatted_command_text, "name": "UAV"})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    uav_response = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": uav_response, "name": "Assistant"})

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
    with gr.Row().style():
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
                    "Take off at your position.\n\n"
                    "Land now.")

demo.launch(share=True)
