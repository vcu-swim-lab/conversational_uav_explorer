# Creating a Prompt and Chain with the transcription so it can be passed to the official Command Prompt via
# Simple Sequential chain Transcription template
prompt_transcribe = """You are to pass the audio transcription to the next
chain. Do not alter the transcription in any way.

Transcription: {text}
"""

# Prompt template
prompt_command = """You are in control of an Unmanned Aerial Vehicle or UAV. 
You are going to be given a sentence command, you need to find the action of 
the sentence. The action will be, Take Picture, Take Off, Land or Go To. 
If the action is "Take Off" or "Land" you don't need any further information
for the location. If the action is "Take Picture" or "Go To" you'll need to 
find where to carry out the action. You need to find. If you can't find an 
action or location, answer with "none". You need to return the command
in this format: command <command> \t <goal>

Sentence: {sentence}
"""

prompt_chat_response = """You are an AI-powered chatbot integrated into a UAV
(Unmanned Aerial Vehicle) system. Your purpose is to receive and execute
commands from an officer. Your role is to understand and carry out these commands
efficiently. You must acknowledge the command if you understand it. Use 2-3 
sentences to respond to the officer's instructions, ask for clarification if 
needed, and provide updates on the execution status of the given commands.
"""

# Creating examples for each command that the llm can use to help format our commands.
# Also passing the transcription to the Command Prompt Template.
examples_few_shot = [
    {
    "sentence": "Take off now.",
    "command": "command: take off"""
    },
    {
    "sentence": "Take off from where you are.",
    "command": "command: take off"
    },
    {
    "sentence": "Go up and go",
    "command": "command: take off"
    },
    {
    "sentence": "Lift off.",
    "command": "command: take off"
    },
    {
    "sentence": "Land now.",
    "command": "command: land"
    },
    {
    "sentence": "Go to the ground where you are.",
    "command": "command: land"
    },
    {
    "sentence": "Take a picture.",
    "command": "command: take picture"
    },
    {
    "sentence": "Take a picture when you can please.",
    "command": "command: take picture"    
    },
    {
    "sentence": "Go to the 7/11 across the street.",
    "command": "command: go to \t7/11 across the street"
    },
    {
    "sentence": "Go to the yellow house two houses to the right of here.",
    "command": "command: go to \tyellow house two houses to the right of here"""
    },
    {
    "sentence": "Go to.",
    "command": "None"
    },
    {
    "sentence": "Go to the Walmart on Iron Bridge Road.",
    "command": "command: go to \tWalmart on Iron Bridge Road"""
    }
]