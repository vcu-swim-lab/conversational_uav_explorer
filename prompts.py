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
find where to carry out the action. If you can't find an 
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
        "sentence": "Go to Papa Johns at 1200 W Main St",
        "command": "command: go to \tPapa Johns at 1200 W Main St"""
    },
    {
        "sentence": "Go to the orange house on W Grace St",
        "command": "command: go to \torange house on W Grace St"""
    },
    {
        "sentence": "Travel to Cabell Library at VCU",
        "command": "command: go to \tCabell Library at VCU"""
    },
    {
        "sentence": "Kroger on N Lombardy St",
        "command": "None"""
    },
    {
        "sentence": "CVS at Main St",
        "command": "None"""
    },
    {
        "sentence": "Short Pump Town Center",
        "command": "None"""
    },
    {
        "sentence": "Can Can Brasserie",
        "command": "None"""
    },
    {
        "sentence": "Walgreens",
        "command": "None"""
    },
    {
        "sentence": "Travel to",
        "command": "None"""
    },
    {
        "sentence": "Go to",
        "command": "None"""
    },
    {
        "sentence": "Take off now.",
        "command": "command: take off"""
    },
    {
        "sentence": "Take off from where you are.",
        "command": "command: take off"
    },
    {
        "sentence": "Take off.",
        "command": "command: take off"
    },
    {
        "sentence": "Take off at your position.",
        "command": "command: take off"
    },
    {
        "sentence": "Take off from where you are at.",
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
        "sentence": "Take a picture.",
        "command": "command: take picture"
    },
    {
        "sentence": "Take a picture when you can please.",
        "command": "command: take picture"
    },
    {
        "sentence": "Stop flying",
        "command": "command: land"""
    },
    {
        "sentence": "Take flight",
        "command": "command: take off"""
    },
    {
        "sentence": "Take a pic.",
        "command": "command: take picture"
    },
    {
        "sentence": "Take a photo.",
        "command": "command: take picture"
    },
    {
        "sentence": "Snap a photo.",
        "command": "command: take picture"
    },
    {
        "sentence": "Snap a pic.",
        "command": "command: take picture"
    },
    {
        "sentence": "Fly to the Sonic on West Cary St.",
        "command": "command: go to \tSonic on West Cary St."
    },
    {
        "sentence": "Check out the gym at Cary St.",
        "command": "command: go to \tgym at Cary St"
    },
    {
        "sentence": "Cease flight",
        "command": "command: land"
    },
    {
        "sentence": "Stop the flight",
        "command": "command: land"
    },
    {
        "sentence": "Investigate the Rite Aid on Broad and Belevidere.",
        "command": "command: go to \tRite Aid on Broad and Belevidere"
    },
    {
        "sentence": "Please check out the CVS on W Broad St.",
        "command": "command: go to \tCVS on W Broad St"
    }
]