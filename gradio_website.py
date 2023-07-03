import openai
import gradio as gr

openai.api_key = "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"
messages = [
    {"role": "system", "content": "You are an AI-powered chatbot integrated into a UAV"
                                  " (Unmanned Aerial Vehicle) system. Your purpose is to receive and execute"
                                  "commands from an officer. Your role is to understand and carry out these commands "
                                  "efficiently. You must acknowledge the command if you understand it. You can respond"
                                  " to the officer's instructions, ask for clarification if needed, and provide updates"
                                  " on the execution status of the given commands."}
]


def transcribe(audio):
    global messages
    audio_file = open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print(transcript)

    messages.append({"role": "user", "content": transcript["text"]})

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


ui = gr.Interface(
    fn=transcribe,
    inputs=gr.Audio(source="microphone", type="filepath"),
    outputs="text").launch(share=True)

ui.launch()
