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
        "sentence": "Go to",
        "command": "None"""
    },
    {
        "sentence": "Travel to",
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
    },
    {
        "sentence": "Go to the bank on the corner.",
        "command": "command: go to \tbank on the corner"""
    },
    {
        "sentence": "Travel to the bank.",
        "command": "command: go to \tbank"""
    },
    {
        "sentence": "Travel.",
        "command": "None"""
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
        "sentence": "Travel to the purple house on the left side.",
        "command": "command: go to \tpurple house on the left side"""
    },
    {
        "sentence": "Travel to the Barnes and Noble on West Broad.",
        "command": "command: go to \tBarnes and Noble on West Broad"""
    },
    {
        "sentence": "Travel to that place.",
        "command": "None"""
    },
    {
        "sentence": "Travel to there.",
        "command": "None"""
    },
    {
        "sentence": "Travel there.",
        "command": "None"""
    },
    {
        "sentence": "Travel over there.",
        "command": "None"""
    },
    {
        "sentence": "Travel to the bank on the corner.",
        "command": "command: go to \tbank on the corner"""
    },
    {
        "sentence": "Travel to the Walmart on W Broad St.",
        "command": "command: go to \tWalmart on W Broad St"""
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
        "sentence": "Fly to the parking garage across the street.",
        "command": "command: go to \tparking garage across the street"
    },
    {
        "sentence": "Fly to the Sonic on West Cary St.",
        "command": "command: go to \tSonic on West Cary St."
    },
    {
        "sentence": "Check out the pizza shop next to the red house over there.",
        "command": "command: go to \tpizza shop next to the red house over there."
    },
    {
        "sentence": "Check out the Cary St Gym.",
        "command": "command: go to \tthe Cary St Gym"
    },
    {
        "sentence": "Check out",
        "command": "None"
    },
    {
        "sentence": "Travel to",
        "command": "None"
    },
    {
        "sentence": "Get to",
        "command": "None"
    },
    {
        "sentence": "Navigate to",
        "command": "None"
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
        "sentence": "Investigate the green house to the left.",
        "command": "command: go to \tgreen house to the left"
    },
    {
        "sentence": "Investigate the Rite Aid on Broad and Belevidere.",
        "command": "command: go to \tRite Aid on Broad and Belevidere"
    }
]
