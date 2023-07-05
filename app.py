import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are an AI-powered chatbot integrated into a UAV "
                                  "(Unmanned Aerial Vehicle) system. Your purpose is to receive and execute"
                                  "commands from an officer. Your role is to understand and carry out these commands "
                                  "efficiently. You must acknowledge the command if you understand it. Use 2-3 "
                                  "sentences to respond to the officer's instructions, ask for clarification if "
                                  "needed, and provide updates on the execution status of the given commands."}
]


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


with gr.Blocks(theme='sudeepshouche/minimalist') as demo:
    gr.Markdown("""
    # Conversational UAV Explorer
    Speak into the microphone to give a command.\n\n
    Commands: Explore, Take Picture, Monitor, Stop, Land, Come Back, Left, Right, Up, Down, Get Closer""")
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

demo.launch(share=True)
