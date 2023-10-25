# Ju Wang, VSU, 7/2023
# usage: from the root folder, python PyTorchAudio\conversational_uav_explorer\app.py
# transcribe from wav file or live mic using wisper or fine-tuned wav2vec model, model loc:
# 	PyTorchAudio\mymodel
# 	download the wav2vec parameter file from onedrive if needed
#!----LINES ADDED BY TERRENCE BLUNT:
#LINES 14, 16, 198 - 218, 232 - 242
#ABSOLUTE PATH LINES: 82, 84, 96, 120, 149, 152, 160, 163, 190, 193, 241
import openai
import gradio as gr
#import chatgpt4uavs
from prompts import PROMPT_CHAT_RESPONSE #prompt_chat_response
from fewshot import FewShot4UAVs
import os

import plotly.graph_objects as go

import shutil
import calendar
import time

import torch
import librosa
from transformers import Wav2Vec2ForCTC
from transformers import Wav2Vec2FeatureExtractor
from transformers import Wav2Vec2CTCTokenizer
from transformers import Wav2Vec2Processor

import whisper


# openai.api_key = "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"
# openai.api_key = "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"
openai.api_key = "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"


fewshot = FewShot4UAVs()

def transcribe(audio,audio2):
    messages = [
        {"role": "system", 
         "content": prompt_chat_response}
    ]

    if (audio != None):
        audio_file = open(audio, "rb")
    else :
        audio_file = open(audio2, "rb")
        audio = audio2

    try:
        chat_transcript = ""
       
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        chat_transcript += "whisper result: "
        chat_transcript += transcript["text"]
        chat_transcript += "\n\n"

        # formatted_command_text = chatgpt4uavs.get_command(transcript["text"])
        formatted_command_text = fewshot.get_command(transcript["text"])

        messages.append({"role": "user", "content": formatted_command_text})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        uav_response = response["choices"][0]["message"]["content"]

        messages.append({"role": "assistant", "content": uav_response})

        
        for message in messages:
            if message['role'] != 'system':
                chat_transcript += message['role'] + ": " + message['content'] + "\n\n"

        # save audio file to disk

        time_stamp = calendar.timegm(time.gmtime())
        tscript = transcript['text'].replace('?', '').replace('*', '').replace('\\','').replace(':','')
        with open (r"C:\Users\terre\Documents\PyTorchAudio\PyTorchAudio\audio\whisper\whisper-"+tscript[:10]+"-"+str(time_stamp)+".txt", 'w') as file:
            file.write(transcript['text'])
        file_name = r"C:\Users\terre\Documents\PyTorchAudio\PyTorchAudio\audio\whisper\whisper-"+tscript[:10]+"-"+str(time_stamp)+".wav"
        shutil.copy(audio, str(file_name))

    except Exception as e:
        chat_transcript =  "error : "+ str(e)

    return "raw trans: " + transcript["text"] + "\n\nfewshots: "+ chat_transcript

def transcribeWhisper(audio,audio2,selectMode):
    print(selectMode)
    chat_transcript = " "

    model = whisper.load_model(r"C:\Users\terre\Documents\PyTorchAudio\PyTorchAudio\whisper"+selectMode+".pt")
    ## read temp audio file 
    if (audio != None):
        audio_file = open(audio, "rb")
    else :
        audio_file = open(audio2, "rb")
        audio = audio2

    # predict
    transcript = model.transcribe(audio)
    chat_transcript =  transcript["text"]

    # save audio file to disk
    time_stamp = calendar.timegm(time.gmtime())
    with open ("./PyTorchAudio/audio/whisperOffline-"+chat_transcript[:10]+"-"+str(time_stamp)+".txt", 'w') as file:
        file.write(chat_transcript)
    # file_name = chat_transcript+"-"+str(time_stamp)+".wav"
    file_name = "./PyTorchAudio/audio/whisperOffline-"+chat_transcript[:10]+"-"+str(time_stamp)+".wav"
    shutil.copy(audio, str(file_name))

    return chat_transcript

def transcribeWav2Vec2(audio,audio2):
    chat_transcript = " "
    modelpath=r"C:\Users\terre\Documents\PyTorchAudio\PyTorchAudio\wav2vec_960h" # this get model using model name and save explicitly
    #"./PyTorchAudio/wav2vec_960_cache/snapshots/22aad52d435eb6dbaf354bdad9b0da84ce7d6156" this directly from cached model
    # "facebook/wav2vec2-base-960h" this use model name, it might come from online or local cache
 
    model = Wav2Vec2ForCTC.from_pretrained(modelpath)
    tokenizer = Wav2Vec2CTCTokenizer.from_pretrained(modelpath)
    # model.to("cuda")    

    feature_extractor = Wav2Vec2FeatureExtractor(feature_size=1, sampling_rate=16000, padding_value=0.0, do_normalize=True, return_attention_mask=False)
    processor = Wav2Vec2Processor(feature_extractor=feature_extractor, tokenizer=tokenizer)

    ## read temp audio file 
    if (audio != None):
        audio_file = open(audio, "rb")
    else :
        audio_file = open(audio2, "rb")
        audio = audio2

    # predict
    audioArray, rate = librosa.load(audio_file, sr = 16000)
    with torch.no_grad():
        input_values = torch.tensor(audioArray, device="cpu").unsqueeze(0) # or cuda
        logits = model(input_values).logits

    pred_ids = torch.argmax(logits, dim=-1)
    chat_transcript = processor.batch_decode(pred_ids)[0]

    # save audio file to disk
    time_stamp = calendar.timegm(time.gmtime())
    with open (r"C:\Users\terre\Documents\PyTorchAudio\PyTorchAudio\audio\Wav2Vec2\Wav2Vec2-"+chat_transcript[:10]+"-"+str(time_stamp)+".txt", 'w') as file:
        file.write(chat_transcript)
    # file_name = chat_transcript+"-"+str(time_stamp)+".wav"
    file_name = r"C:\Users\terre\Documents\PyTorchAudio\PyTorchAudio\audio\Wav2Vec2\Wav2Vec2-"+chat_transcript[:10]+"-"+str(time_stamp)+".wav"
    shutil.copy(audio, str(file_name))

    return chat_transcript

def transcribeWav2Vec2Our(audio,audio2):
    chat_transcript = " "
    
    model = Wav2Vec2ForCTC.from_pretrained(r"C:\Users\terre\Documents\PyTorchAudio\PyTorchAudio\mymodel")
    # model.to("cuda")
    # tokenizer = Wav2Vec2CTCTokenizer("./PyTorchAudio/vocab-my.json", unk_token="[UNK]", pad_token="[PAD]", word_delimiter_token="|")
    tokenizer = Wav2Vec2CTCTokenizer.from_pretrained(r"C:\Users\terre\Documents\PyTorchAudio\PyTorchAudio\mymodel", unk_token="[UNK]", pad_token="[PAD]", word_delimiter_token="|")
   
    # model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
    # tokenizer = Wav2Vec2CTCTokenizer.from_pretrained("facebook/wav2vec2-base-960h")


    feature_extractor = Wav2Vec2FeatureExtractor(feature_size=1, sampling_rate=16000, padding_value=0.0, do_normalize=True, return_attention_mask=False)
    processor = Wav2Vec2Processor(feature_extractor=feature_extractor, tokenizer=tokenizer)

    ## read temp audio file 
    if (audio != None):
        audio_file = open(audio, "rb")
    else :
        audio_file = open(audio2, "rb")
        audio = audio2

    # predict
    audioArray, rate = librosa.load(audio_file, sr = 16000)
    with torch.no_grad():
        input_values = torch.tensor(audioArray, device="cpu").unsqueeze(0) # or cuda
        logits = model(input_values).logits

    pred_ids = torch.argmax(logits, dim=-1)
    chat_transcript = processor.batch_decode(pred_ids)[0]

    # save audio file to disk
    time_stamp = calendar.timegm(time.gmtime())
    with open (r"C:\Users\terre\Documents\PyTorchAudio\PyTorchAudio\audio\FineWav2Vec2\FineWav2Vec2-"+chat_transcript[:10]+"-"+str(time_stamp)+".txt", 'w') as file:
        file.write(chat_transcript)
    # file_name = chat_transcript+"-"+str(time_stamp)+".wav"
    file_name = r"C:\Users\terre\Documents\PyTorchAudio\PyTorchAudio\audio\FineWav2Vec2\FineWav2Vec2-"+chat_transcript[:10]+"-"+str(time_stamp)+".wav"
    shutil.copy(audio, str(file_name))

    return chat_transcript

def video_identity(video):
    return video

def filter_map(min_price, max_price, buildings):
    fig = go.Figure(go.Scattermapbox())

    fig.update_layout(
        mapbox_style="open-street-map",
        hovermode='closest',
        mapbox=dict(
            bearing=0,
            center=go.layout.mapbox.Center(
                lat=37.23917436633742,
                lon=-77.42165931069431
            ),
            pitch=0,
            zoom=15
        ),
    )

    return fig

with gr.Blocks(theme='sudeepshouche/minimalist') as demo:
    
    gr.Markdown("""
    # Whisper VS Wav2Vec2 Translation Comparison \n\n
    1. Speak into the microphone or upload a voice file to give a command.\n\n
    Commands: Track target, engage target, Show threat velocity, Explore,  Monitor, Stop, Left, Right, Up, Down, Get Closer""")

    with gr.Row().style():
        # with gr.Column():
            audio_input = gr.Audio(source="microphone", type="filepath")
            audio_input2 = gr.Audio(source="upload", type="filepath")
            
    gr.Markdown("""Map Interface:""")
    
    with gr.Column():
        map = gr.Plot()
    demo.load(filter_map, [], map)
    
    gr.Markdown("""Video Interface:""")
    
    gr.Interface(video_identity, gr.Video(), "playable_video", \
        examples=[os.path.join(os.path.dirname(__file__), "ashe.mp4")], \
            cache_examples=True)
    
    gr.Markdown("""
    2. Select Mode
    """)

    with gr.Row():
        with gr.Column():
            output = gr.Textbox(label="Whisper Transcript")
            submit_btn = gr.Button("Whisper Result", variant="primary")
            submit_btn.click(fn=transcribe, inputs=[audio_input,audio_input2], outputs=output, api_name="whisper")
        with gr.Column():
            output = gr.Textbox(label="Whisper offline Transcript")
            selectMode = gr.Dropdown(["base.en", "base", "tiny.en", "tiny", "small.en", "small", "medium.en", "medium"], value="small.en", label="Whisper Mode", info="")
            submit_btn = gr.Button("Whisper Result", variant="primary")
            submit_btn.click(fn=transcribeWhisper, inputs=[audio_input,audio_input2,selectMode], outputs=output, api_name="whisper2")
        with gr.Column():
            output = gr.Textbox(label="facebook/wav2vec2-base-960h Transcript offline")
            submit_btn = gr.Button("Wav2Vec2 Result", variant="primary")
            submit_btn.click(fn=transcribeWav2Vec2, inputs=[audio_input,audio_input2], outputs=output, api_name="wav2Vec2")
        with gr.Column():
            output = gr.Textbox(label="Our Fine-Tune Wav2vec2  Transcript offline")
            submit_btn = gr.Button("Wav2Vec2 Result", variant="primary")
            submit_btn.click(fn=transcribeWav2Vec2Our, inputs=[audio_input,audio_input2], outputs=output, api_name="wav2Vec22")
    with gr.Accordion("Examples:"):
        gr.Markdown("Explore the second floor of the main deck.\n\n"
                    "Show top 10 threats location on radar screen.\n\n"
                    "Turn on the fire extinguish at kitchen.")
    
demo.launch(server_name="0.0.0.0", share=True)

