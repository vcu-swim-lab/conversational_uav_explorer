import os
from typing import Optional, Tuple

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate, FewShotPromptTemplate
from langchain.chains import LLMChain, SequentialChain, SimpleSequentialChain

# API Key
os.environ["OPENAI_API_KEY"] = "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"

# Initializing OpenAI as the large language model
llm = OpenAI(temperature=0.9)

# The following algorithm will be an implementation of the Command Breakdown, with a gradio web app that will
# transcibe the commands. It will soon be integrated with this program.

# Creating a Prompt and Chain with the transcription so it can be passed to the offical Command Prompt via Simple
# Sequential chain Transcription Prompt
transcribe_prompt = """You are to pass the aubio transcription to the next
chain. Do not alter the transcription in any way.

Transcription: {text}
"""

# Creating transcription chain
sentence_chain = LLMChain(llm=llm,
                          prompt=transcribe_prompt,
                          output_key="sentence")

"""Hypothetical chain testing."""
# Transcription Test
"""holder = sentence_chain.run(transcription)
print(holder)"""

# Creating examples for each command that the llm can use to help format our commands.
# Also passing the transcription to the Command Prompt Template.
examples = [
    {
        "sentence": "Take Off now.",
        "command": """takeoff  rise from the ground"""
    },
    {
        "sentence": "Take Off from where you are.",
        "command": """takeoff  rise from the ground"""
    },
    {
        "sentence": "Take Off and go to the yellow house.",
        "command": """takeoff  rise from the ground"""
    },
    {
        "sentence": "Take Off.",
        "command": """takeoff  rise from the ground"""
    },
    {
        "sentence": "Land now.",
        "command": """land  slowly lower to the the ground where you are"""
    },
    {
        "sentence": "Land where you are.",
        "command": """land  slowly lower to the the ground where you are."""
    },
    {
        "sentence": "Land at the purple house on W Main.",
        "command": """land  fly to the purple house on W Main then slowly lower to the ground."""
    },
    {
        "sentence": "Land.",
        "command": """land  slowly lower to the the ground where you are"""
    },
    {
        "sentence": "Take picture.",
        "command": """pic  take a photo of whatever is in front of you"""
    },
    {
        "sentence": "Take a picture now.",
        "command": """pic  take a photo of whatever is in front of you"""
    },
    {
        "sentence": "Take a photo of the green house on the corner of Cary and Belvidere.",
        "command": """pic  take a photo of the green house on the corner of Cary and Belvidere"""
    },
    {
        "sentence": "Take picture of the front door of the Engineering West Hall.",
        "command": """pic  take a photo of the front door of the Engineering West Hall"""
    },
    {
        "sentence": "Go to the 7/11 across the street.",
        "command": """move  fly to thee 7/11 across the street"""
    },
    {
        "sentence": "Go to the yellow house two houses to the right of here.",
        "command": """move  fly to the yellow house two houses to the right of here"""
    },
    {
        "sentence": "Go to.",
        "command": """move  stay in place no location given"""
    },
    {
        "sentence": "Go to the Walmart on Iron Bridge Road.",
        "command": """move  to the Walmart on Iron Bridge Road"""
    },
]

# Formatter for the examples
example_prompt = PromptTemplate(input_variables=["sentence", "command"], template="Question: {question}\n{answer}")
print(example_prompt.format(**examples[0]))

# Prompt Creation
prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="""You are in control of an Unmanned Aerial Vehicle or UAV. You are going to be given a 
    sentence command, you need to find the action of the sentence. The action will be, Take Picture, 
    Take Off, Land and Go To. If the action is "Take Off" or "Land" you don't need any further information 
    for the location. If the action is "Take Picture" or "Go To" you'll need to find where to carry out the action. 
    You need to find. If you can't find an action or location, answer with "none". You need to return the command 
    in this format: command <command> \\tab <goal>

    Sentence: {sentence}
    """,
    input_variables=["sentence"]
)

# Prompt Testing
print(prompt.format(input="Go to the Cary Street Gym."))

# Chain Creation
command_chain = LLMChain(llm=llm,
                         prompt=prompt,
                         output_key="output")

# Connecting the two created chains via the SimpleSequentialChain.
sentence_command_chain = SimpleSequentialChain(
    chains=[sentence_chain, command_chain], verbose=True
)

# Testing to make sure the output of the sentence chain was used as the input for the second implementation of the
# command chain. Connection Test
"""holder2 = sentence_command_chain.run(imagine_a_transcription_here)
print(holder2)"""

# Saving the commands new format
# final_command = sentence_command_chain.run("imagine_a_transcription_here")

# The next part is to write the output of the final_command variable to a file
# IMPLEMENTATION BELOW SHORTLY
