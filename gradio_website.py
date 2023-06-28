from transformers import pipeline
import gradio as gr

p = pipeline("automatic-speech-recognition")

def transcribe(audio):
    text = p(audio)["text"]
    return text

gr.Interface(
    fn=transcribe, 
    inputs=gr.Audio(source="microphone", type="filepath"), 
    outputs="text").launch(share=True)