import openai
import gradio as gr
import chatgpt4uavs
from maps import AddressLocator
from prompts import prompt_chat_response
from fewshot import FewShot4UAVs

openai.api_key = "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"

fewshot = FewShot4UAVs()
address_locator = AddressLocator()

def transcribe(audio):
    messages = [
        {"role": "system", 
         "content": prompt_chat_response}
    ]

    audio_file = open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    # formatted_command_text = chatgpt4uavs.get_command(transcript["text"])
    formatted_command_text = fewshot.get_command(transcript["text"])
    location = address_locator.get_location(formatted_command_text)

    if location is not None:
        formatted_command_text = formatted_command_text.replace("<location>", location)

    messages.append({"role": "user", "content": formatted_command_text})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    uav_response = response["choices"][0]["message"]["content"]

    messages.append({"role": "assistant", "content": uav_response})

    chat_transcript = ""
    for message in messages:
        if message['role'] != 'system':
            chat_transcript += message['role'] + ": " + message['content'] + "\n\n"

    return chat_transcript


with gr.Blocks(theme='sudeepshouche/minimalist') as demo:
    gr.Markdown("""
    # Conversational UAV Explorer
    Speak into the microphone to give a command.\n\n
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
                    "Land now.\n\n"
                    "Take off.")

demo.launch(share=True)
