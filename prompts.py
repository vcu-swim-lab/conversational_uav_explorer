# Creating a Prompt and Chain with the transcription so it can be passed to the official Command Prompt via
# Simple Sequential chain Transcription template
prompt_transcribe = """You are to pass the audio transcription to the next
chain. Do not alter the transcription in any way.

Transcription: {text}
"""

# Prompt template
prompt_command = """You are in control of an Unmanned Aerial Vehicle or UAV. 
You are going to be given a sentence command, you need to find the action of 
the sentence. The action will be, TAKEPICTURE, TAKEOFF, LAND or GOTO. If the 
action is not one of those actions return "NONE". ONLY give those commands or 
"NONE", NEVER anything else. If the action is "TAKEOFF", "LAND" or "NONE" you 
don't need any further information for the location. If the action is "GOTO" or
"TAKEPICTURE", you'll need to find where to carry out the action. If the action 
is "GOTO" or "TAKEPICTURE" with no location following return "None".

If you can't find the actions Take Picture, Take Off, Land, or Go To, return "NONE". 

You need to return the command in this format: <command> \t<goal>

However, if you get a sentence with multiple commands here is what you need to do:
For example take the sentence, "Go to the Walmart in Petersburg and take a picture."
The format of the command needs to be: <first command> \t<goal>\n\n<second command> \t<goal>

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
        "command": "command: GOTO \tKroger on N Lombardy St"""
    },
    {
        "sentence": "CVS at Main St.",
        "command": "command: GOTO \tCVS at Main St"""
    },
    {
        "sentence": "Short Pump Town Center.",
        "command": "command: GOTO \tShort Pump Town Center"""
    },
    {
        "sentence": "Can Can Brasserie.",
        "command": "command: GOTO \tCan Can Brasserie"""
    },
    {
        "sentence": "Walgreens.",
        "command": "command: GOTO \tWalgreens"""
    },
    {
        "sentence": "Best Buy in Colonial Heights.",
        "command": "command: GOTO \tBest Buy in Colonial Heights"""
    },
    {
        "sentence": "The red house to the left.",
        "command": "command: GOTO \tred house to the left"""
    },
    {
        "sentence": "The Science Museum.",
        "command": "command: GOTO \tScience Museum"""
    },
    {
        "sentence": "South Park Mall.",
        "command": "command: GOTO \tSouth Park Mall"""
    },
    # Commands that don't require a location
    {
        "sentence": "Take off now.",
        "command": "command: TAKEOFF"""
    },
    {
        "sentence": "Take off from where you are.",
        "command": "command: TAKEOFF"
    },
    {
        "sentence": "Take off.",
        "command": "command: TAKEOFF"
    },
    {
        "sentence": "Take off at your position.",
        "command": "command: TAKEOFF"
    },
    {
        "sentence": "Take off from where you are at.",
        "command": "command: TAKEOFF"
    },
    {
        "sentence": "Lift off.",
        "command": "command: TAKEOFF"
    },
    {
        "sentence": "Land now.",
        "command": "command: LAND"
    },
    {
        "sentence": "Cease flight.",
        "command": "command: LAND"
    },
    {
        "sentence": "Stop the flight.",
        "command": "command: LAND"
    },
    {
        "sentence": "Stop flying.",
        "command": "command: LAND"""
    },
    {
        "sentence": "Take flight.",
        "command": "command: TAKEOFF"""
    },
    # Commands that require a location but don't have any
    {
        "sentence": "Take a pic.",
        "command": "NONE"
    },
    {
        "sentence": "Take a photo.",
        "command": "NONE"
    },
    {
        "sentence": "Snap a photo.",
        "command": "NONE"
    },
    {
        "sentence": "Snap a pic.",
        "command": "NONE"
    },
    {
        "sentence": "Proceed to.",
        "command": "NONE"""
    },
    {
        "sentence": "Push to.",
        "command": "NONE"""
    },
    {
        "sentence": "Advance to.",
        "command": "NONE"""
    },
    {
        "sentence": "Make your way to.",
        "command": "NONE"""
    },
    {
        "sentence": "Travel to.",
        "command": "NONE"""
    },
    {
        "sentence": "Go to.",
        "command": "NONE"""
    },
    {
        "sentence": "Take a picture.",
        "command": "NONE"
    },
    {
        "sentence": "Take a picture when you can please.",
        "command": "NONE"
    },
    # Commands with one action and one location
    {
        "sentence": "Fly to the Sonic on West Cary St.",
        "command": "command: GOTO \tSonic on West Cary St."
    },
    {
        "sentence": "Check out the gym at Cary St.",
        "command": "command: GOTO \tgym at Cary St"
    },
    {
        "sentence": "Investigate the Rite Aid on Broad and Belevidere.",
        "command": "command: GOTO \tRite Aid on Broad and Belevidere"
    },
    {
        "sentence": "Go to Papa Johns at 1200 W Main St.",
        "command": "command: GOTO \tPapa Johns at 1200 W Main St"""
    },
    {
        "sentence": "Go to the orange house on W Grace St.",
        "command": "command: GOTO \torange house on W Grace St"""
    },
    {
        "sentence": "Travel to Cabell Library at VCU.",
        "command": "command: GOTO \tCabell Library at VCU"""
    },
    # Commands with one action and one location but with extra words
    {
        "sentence": "Please check out the CVS on W Broad St.",
        "command": "command: GOTO \tCVS on W Broad St"
    },
    # Commands with multiple actions
    {
        "sentence": "Go to the purple house on to the left and take a picture.",
        "command": "command: GOTO \tpurple house on to the left\ncommand: TAKEPICTURE \tpurple house on to the left"
    },
    {
        "sentence": "Fly to Kroger on Iron Bridge and take a picture.",
        "command": "command: GOTO \tKroger on Iron Bridge\ncommand: TAKEPICTURE \tKroger on Iron Bridge"
    },
    {
        "sentence": "Travel to the McDonalds on Route 1 and land.",
        "command": "command: GOTO \tMcDonalds on Route 1\ncommand: LAND"
    },
    {
        "sentence": "Take off, go to the Walgreens on W Hundred Rd, then land.",
        "command": "command: TAKEOFF\ncommand: GOTO \tWalgreens on W Hundred Rd\ncommand: LAND"
    },
    # Commands with multiple actions and multiple locations
    {
        "sentence": "Take a picture of the light blue building on Harrowgate Road, then go to the Wawa on Route 1.",
        "command": "command: TAKEPICTURE \tlight blue building on Harrowgate Road\ncommand: GOTO \tWawa on Route 1"
    },
    {
        "sentence": "Check out the yellow house on Clay St, then go to the Commons on W Main St.",
        "command": "command: GOTO \tyellow house on Clay St\ncommand: GOTO \tCommons on W Main St"
    },
    {
        "sentence": "Investigate the 7/11 on W Grace St, then go to the Barnes and Noble on W Broad St, then take a picture of it.",
        "command": "command: GOTO \t7/11 on W Grace St\ncommand: GOTO \tBarnes and Noble on W Broad S\ncommand: TAKEPICTURE \tBarnes and Noble on W Broad St"
    },
    {
        "sentence": "Go to the grey one story flat on Happy Hill Rd, then go to the Food Lion on the same road, then take a picture of it.",
        "command": "command: GOTO \tgrey one story flat on Happy Hill Rd\ncommand: GOTO \tFood Lion on Happy Hill Rd\ncommand: TAKEPICTURE \tFood Lion on Happy Hill Rd"
    }
]
