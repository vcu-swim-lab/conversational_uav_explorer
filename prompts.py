# Creating a Prompt and Chain with the transcription so it can be passed to the official Command Prompt via
# Simple Sequential chain Transcription template
prompt_transcribe = """You are to pass the audio transcription to the next
chain. Do not alter the transcription in any way.

Transcription: {text}
"""

# Prompt template
prompt_command = """You are in control of an Unmanned Aerial Vehicle or UAV. 
You are going to be given a sentence command, you need to find the action of 
the sentence. The action will be, Take Picture, Take Off, Land or Go To. If the 
action is not one of those actions return "None. If the action is "Take Off", 
"Land" or "None" you don't need any further information for the location. If 
the action is "Go To" or "Take Picture" you'll need to find where to carry out 
the action. If the action is "Go To" with no location following return "None". If you get 
a location without the actions "Go To" or "Take Picture" return "None". If you 
can't find the actions Take Picture, Take Off, Land, or Go To return "None". When
analyzing the sentence do NOT infer words that are not there. 
For example: "Best Buy in Colonial Heights" is NOT a 
viable command. When
encountering a sentence like the examples return "None." Do not infer any action 
that is not explicitly stated.
You need to return the command in this format: command <command> \t <goal>

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
        "sentence": "Go to Papa Johns at 1200 W Main St.",
        "command": "command: go to \tPapa Johns at 1200 W Main St"""
    },
    {
        "sentence": "Go to the orange house on W Grace St.",
        "command": "command: go to \torange house on W Grace St"""
    },
    {
        "sentence": "Travel to Cabell Library at VCU.",
        "command": "command: go to \tCabell Library at VCU"""
    },
    {
        "sentence": "Kroger on N Lombardy St.",
        "command": "None"""
    },
    {
        "sentence": "CVS at Main St.",
        "command": "None"""
    },
    {
        "sentence": "Short Pump Town Center.",
        "command": "None"""
    },
    {
        "sentence": "Can Can Brasserie.",
        "command": "None"""
    },
    {
        "sentence": "Walgreens.",
        "command": "None"""
    },
    {
        "sentence": "Travel to.",
        "command": "None"""
    },
    {
        "sentence": "Go to.",
        "command": "None"""
    },
    {
        "sentence": "Best Buy in Colonial Heights.",
        "command": "None"""
    },
    {
        "sentence": "The red house to the left.",
        "command": "None"""
    },
    {
        "sentence": "Right where you are.",
        "command": "None"""
    },
    {
        "sentence": "The Science Museum.",
        "command": "None"""
    },
    {
        "sentence": "South Park Mall.",
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
        "command": "None"
    },
    {
        "sentence": "Take a picture when you can please.",
        "command": "None"
    },
    {
        "sentence": "Stop flying.",
        "command": "command: land"""
    },
    {
        "sentence": "Take flight.",
        "command": "command: take off"""
    },
    {
        "sentence": "Take a pic.",
        "command": "None"
    },
    {
        "sentence": "Take a photo.",
        "command": "None"
    },
    {
        "sentence": "Snap a photo.",
        "command": "None"
    },
    {
        "sentence": "Snap a pic.",
        "command": "None"
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
        "sentence": "Cease flight.",
        "command": "command: land"
    },
    {
        "sentence": "Stop the flight.",
        "command": "command: land"
    },
    {
        "sentence": "Investigate the Rite Aid on Broad and Belevidere.",
        "command": "command: go to \tRite Aid on Broad and Belevidere"
    },
    {
        "sentence": "Please check out the CVS on W Broad St.",
        "command": "command: go to \tCVS on W Broad St"
    },
    {
        "sentence": "Proceed to.",
        "command": "None"""
    },
    {
        "sentence": "Push to.",
        "command": "None"""
    },
    {
        "sentence": "Advance to.",
        "command": "None"""
    },
    {
        "sentence": "Make your way to.",
        "command": "None"""
    },
]
