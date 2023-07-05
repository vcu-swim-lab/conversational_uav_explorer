import os
from typing import Optional, Tuple

import openai
import gradio as gr
from threading import Lock

from langchain import ConversationChain

# from chatgpt4uavs.py import sentence_command_chain

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are an AI-powered chatbot integrated into a UAV "
                                  "(Unmanned Aerial Vehicle) system. Your purpose is to receive and execute"
                                  "commands from an officer. Your role is to understand and carry out these commands "
                                  "efficiently. You must acknowledge the command if you understand it. Use 2-3 "
                                  "sentences to respond to the officer's instructions, ask for clarification if "
                                  "needed, and provide updates on the execution status of the given commands."}
]


def load_chain():
    # need to load chains from chatgpt4uavs.py
    pass


def set_openai_api_key(api_key: str):
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
        chain = load_chain()
        os.environ["OPENAI_API_KEY"] = ""
        return chain


def transcribe(audio):
    global messages

    audio_file = open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    messages.append({"role": "user", "content": transcript["text"]})

    """Goal: Integrate LangChain into Gradio - my approach is to grab the original transcript above,
    run it through the chains from chatgpt4uavs.py and save it to filtered_transcript, and use the
    filtered transcript in the conversation with the conversational UAV.
    
    Currently getting a few errors with the sentence_command_chain, specifically the issue lies
    within PromptTemplate in chatgpt4uavs.py, so I will need to check that. I commented the code
    out to test the interface without errors."""
    # filtered_transcript = sentence_command_chain.run({"text": transcript["text"]})
    # messages.append({"role": "user", "content": filtered_transcript["output"]})

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


class ChatWrapper:
    def __init__(self):
        self.lock = Lock()

    def __call__(
            self, api_key: str, audio_input, state: Optional[Tuple[str, str]], chain: Optional[ConversationChain]
    ):
        self.lock.acquire()
        try:
            if chain is None:
                state.append(("Please paste your OpenAI key to use",))
                return state, state
            openai.api_key = api_key

            transcript = transcribe(audio_input)
            state.append((transcript,))

        except Exception as e:
            raise e
        finally:
            self.lock.release()

        return state, state


chat = ChatWrapper()

with gr.Blocks(theme='sudeepshouche/minimalist') as demo:
    gr.Markdown("""
    # Conversational UAV Explorer
    Speak into the microphone to give a command.\n\n
    Commands: Explore, Take Picture, Monitor, Stop, Land, Come Back, Left, Right, Up, Down, Get Closer""")
    with gr.Row():
        openai_api_key_textbox = gr.Textbox(
            placeholder="Paste your OpenAI API key",
            show_label=False,
            lines=1,
            type="password"
        )
    with gr.Row().style():
        audio_input = gr.Audio(source="microphone", type="filepath")
        output = gr.Textbox(label="Transcript")
    with gr.Row():
        with gr.Column():
            submit_btn = gr.Button("Give command", variant="primary")
            submit_btn.click(fn=transcribe, inputs=audio_input, outputs=output, api_name="record")
    with gr.Accordion("Examples:"):
        gr.Markdown("Explore the second floor of the green house.\n\n"
                    "Take a picture inside the brick house on Main St.\n\n"
                    "Monitor the house at the NE corner of the intersection of Main and Cary.")

    state = gr.State()

    openai_api_key_textbox.change(
        set_openai_api_key,
        inputs=[openai_api_key_textbox],
        outputs=[state],
    )

demo.launch(share=True)
