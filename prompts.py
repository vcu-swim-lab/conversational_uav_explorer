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
the action is "Go To" or "Take Picture", you'll need to find where to carry out 
the action. If the action is "Go To" or "Take Picture" with no location following return "None".

If you can't find the actions Take Picture, Take Off, Land, or Go To, return "None". 

You need to return the command in this format: command <command> \t<goal>

However, if you get a sentence with multiple commands here is what you need to do:
For example take the sentence, "Go to the Walmart in Petersburg and take a picture."
The format of the command needs to be: command <first command> \t<goal>\n\n<second command> \t<goal>

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
    # Location only
    {
        "sentence": "Kroger on N Lombardy St.",
        "command": "command: go to \tKroger on N Lombardy St"""
    },
    {
        "sentence": "CVS at Main St.",
        "command": "command: go to \tCVS at Main St"""
    },
    {
        "sentence": "Short Pump Town Center.",
        "command": "command: go to \tShort Pump Town Center"""
    },
    {
        "sentence": "Can Can Brasserie.",
        "command": "command: go to \tCan Can Brasserie"""
    },
    {
        "sentence": "Walgreens.",
        "command": "command: go to \tWalgreens"""
    },
    {
        "sentence": "Best Buy in Colonial Heights.",
        "command": "command: go to \tBest Buy in Colonial Heights"""
    },
    {
        "sentence": "The red house to the left.",
        "command": "command: go to \tred house to the left"""
    },
    {
        "sentence": "The Science Museum.",
        "command": "command: go to \tScience Museum"""
    },
    {
        "sentence": "South Park Mall.",
        "command": "command: go to \tSouth Park Mall"""
    },
    # Commands that don't require a location
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
        "sentence": "Cease flight.",
        "command": "command: land"
    },
    {
        "sentence": "Stop the flight.",
        "command": "command: land"
    },
    {
        "sentence": "Stop flying.",
        "command": "command: land"""
    },
    {
        "sentence": "Take flight.",
        "command": "command: take off"""
    },
    # Commands that require a location but don't have any
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
    {
        "sentence": "Travel to.",
        "command": "None"""
    },
    {
        "sentence": "Go to.",
        "command": "None"""
    },
    {
        "sentence": "Take a picture.",
        "command": "None"
    },
    {
        "sentence": "Take a picture when you can please.",
        "command": "None"
    },
    # Commands with one action and one location
    {
        "sentence": "Fly to the Sonic on West Cary St.",
        "command": "command: go to \tSonic on West Cary St."
    },
    {
        "sentence": "Check out the gym at Cary St.",
        "command": "command: go to \tgym at Cary St"
    },
    {
        "sentence": "Investigate the Rite Aid on Broad and Belevidere.",
        "command": "command: go to \tRite Aid on Broad and Belevidere"
    },
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
    # Commands with one action and one location but with extra words
    {
        "sentence": "Please check out the CVS on W Broad St.",
        "command": "command: go to \tCVS on W Broad St"
    },
    # Commands with multiple actions
    {
        "sentence": "Go to the purple house on to the left and take a pciture",
        "command": "command: go to \tpurple house on to the left\ncommand: take picture \tpurple house on to the left"
    },
    {
        "sentence": "Go to Kroger on Iron Bridge and take a picure",
        "command": "command: go to \tKroger on Iron Bridge\ncommand: take picture \tKroger on Iron Bridge"
    },
    # Commands with multiple actions and multiple locations
]
