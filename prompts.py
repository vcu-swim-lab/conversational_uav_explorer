"""
This module contains the prompts and examples for the few-shot model.
"""
PROMPT_TRANSCRIBE = """You are to pass the audio transcription to the next
chain. Do not alter the transcription in any way.

Transcription: {text}
"""

PROMPT_COMMAND = """You are in control of an Unmanned Aerial Vehicle or UAV.
You are going to be given a sentence command, you need to find the action of 
the sentence. The action will be, "TAKEPICTURE" (Take picture), "TAKEOFF" (Take off), "LAND" (Land) or "GOTO" (Go to).

If the action is not one of those actions return "NONE".

If the action is "TAKEOFF" (Take off), "LAND" (Land), or "NONE" you don't need any further information for the location.
If the action is "GOTO" (Go to) or "TAKEPICTURE" (Take picture), you'll need to find where to carry out the action.

If the action is "GOTO" (Go to) or "TAKEPICTURE" (Take picture) with no location following it, return "NONE".

If you can't find the actions "TAKEPICTURE" (Take picture), "TAKEOFF" (Take off), "LAND" (Land), or "GOTO" (Go to), 
return "NONE".

You need to return the command in this format: <command> \t<goal>

However, if you get a sentence with multiple commands here is what you need to do:
For example take the sentence, "Go to the Walmart in Petersburg and take a picture."
The format of the command needs to be: <first command> \t<goal>\n\n<second command> \t<goal>

Sentence: {sentence}
"""

PROMPT_CHAT_RESPONSE = """You are an AI-powered chatbot integrated into a UAV
(Unmanned Aerial Vehicle) system.
You're friendly, personable, and happy to help. Your purpose is to receive and acknowledge commands from an officer.
The commands are "Go to <location>", "Take picture", "Land", "Takeoff", or similar versions of those commands. Use 2-3
sentences to respond to the officer's commands and ask for clarification only if necessary.
"""

EXAMPLES_FEW_SHOT = [
    # Location only
    {
        "sentence": "Kroger on N Lombardy St.",
        "command": "GOTO \tKroger on N Lombardy St"
    },
    {
        "sentence": "CVS at Main St.",
        "command": "GOTO \tCVS at Main St"
    },
    {
        "sentence": "Short Pump Town Center.",
        "command": "GOTO \tShort Pump Town Center"
    },
    {
        "sentence": "Can Can Brasserie.",
        "command": "GOTO \tCan Can Brasserie"
    },
    {
        "sentence": "Walgreens.",
        "command": "GOTO \tWalgreens"
    },
    {
        "sentence": "Best Buy in Colonial Heights.",
        "command": "GOTO \tBest Buy in Colonial Heights"
    },
    {
        "sentence": "The red house to the left.",
        "command": "GOTO \tred house to the left"
    },
    {
        "sentence": "The Science Museum.",
        "command": "GOTO \tScience Museum"
    },
    {
        "sentence": "South Park Mall.",
        "command": "GOTO \tSouth Park Mall"
    },
    # Commands that don't require a location
    {
        "sentence": "Take off now.",
        "command": "TAKEOFF"
    },
    {
        "sentence": "Take off from where you are.",
        "command": "TAKEOFF"
    },
    {
        "sentence": "Take off.",
        "command": "TAKEOFF"
    },
    {
        "sentence": "Take off at your position.",
        "command": "TAKEOFF"
    },
    {
        "sentence": "Take off from where you are at.",
        "command": "TAKEOFF"
    },
    {
        "sentence": "Lift off.",
        "command": "TAKEOFF"
    },
    {
        "sentence": "Land.",
        "command": "LAND"
    },
    {
        "sentence": "Cease flight.",
        "command": "LAND"
    },
    {
        "sentence": "Stop the flight.",
        "command": "LAND"
    },
    {
        "sentence": "Stop flying.",
        "command": "LAND"
    },
    {
        "sentence": "Take flight.",
        "command": "TAKEOFF"
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
        "command": "NONE"
    },
    {
        "sentence": "Push to.",
        "command": "NONE"
    },
    {
        "sentence": "Advance to.",
        "command": "NONE"
    },
    {
        "sentence": "Make your way to.",
        "command": "NONE"
    },
    {
        "sentence": "Travel to.",
        "command": "NONE"
    },
    {
        "sentence": "Go to.",
        "command": "NONE"
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
        "command": "GOTO \tSonic on West Cary St."
    },
    {
        "sentence": "Check out the gym at Cary St.",
        "command": "GOTO \tgym at Cary St"
    },
    {
        "sentence": "Investigate the Rite Aid on Broad and Belevidere.",
        "command": "GOTO \tRite Aid on Broad and Belevidere"
    },
    {
        "sentence": "Go to Papa Johns at 1200 W Main St.",
        "command": "GOTO \tPapa Johns at 1200 W Main St"
    },
    {
        "sentence": "Go to the orange house on W Grace St.",
        "command": "GOTO \torange house on W Grace St"
    },
    {
        "sentence": "Travel to Cabell Library at VCU.",
        "command": "GOTO \tCabell Library at VCU"
    },
    {
        "sentence": "Take a picture of the park.",
        "command": "TAKEPICTURE \tpark"
    },
    {
        "sentence": "Take a picture of the Kroger on Lombardy St.",
        "command": "TAKEPICTURE \tKroger on Lombardy St"
    },
    # Commands with one action and one location but with extra words
    {
        "sentence": "Please check out the CVS on W Broad St.",
        "command": "GOTO \tCVS on W Broad St"
    },
    # Commands with multiple actions
    {
        "sentence": "Go to the purple house on to the left and take a picture.",
        "command": "GOTO \tpurple house on to the left\nTAKEPICTURE \tpurple house on to the left"
    },
    {
        "sentence": "Go to Kroger on Iron Bridge and take a picture.",
        "command": "GOTO \tKroger on Iron Bridge\nTAKEPICTURE \tKroger on Iron Bridge"
    }
    # Commands with multiple actions and multiple locations
]
