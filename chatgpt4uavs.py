# Setup ChatGPT
pip install langchain
pip install openai

# Necessary imports
import os
from langchain.llms import OpenAI

# API Key
os.environ["OPENAI_API_KEY"] = "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"

# Initializing OpenAI as the large language model
llm = OpenAI(temperature=0.9)
# Testing
text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text))

# Necessary Imports
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

# The following algorithm will be an implementation of the Command Breakdown, with Whisper translating the command to text.

# Installing Library
!pip install -U openai-whisper

# THE WHISPER PART CURRENTLY IS TEMPORARY, SEPERATE SITE FOR VOICE INPUT COMING SOON!!!!!
# This is where the model of Whisper used is selected.
# Importing Whisper and picking the model. 
import whisper
model = whisper.load_model("base")

# This is where the path is put down to the audio file, so it can be transcribed.
result = model.transcribe("pretend/this/is/a/path/for/now")
transcription = result["text"]

# Creating a Prompt and Chain with the transcription so it can be passed to the offical Command Prompt via Simple Sequential chain
# Transcription Prompt
transcribe_prompt = """You are to pass the aubio transcription to the next
chain. Do not alter the transciption in any way.

Transcription: {text}
"""

# Creating transcription chain
sentence_chain = LLMChain(llm = llm,
                       prompt =  transcribe_prompt,
                        output_key = "sentence")

"""Hypothetical chain testing."""

# Transcription Test
holder4 = sentence_chain.run(transcription)
print(holder4)

# Passing the transcription to the Command Prompt Template.

# Action Prompt
prompt_command2 = """You are going to get a sentence command, you need to find
the action of the sentence. The action will be, Take Picture, Monitor or
Explore. You need to find the subject and the location of the sentence
subject. If you can't find an action or location, answer with "none". If the
action is Take Picture, you need to also find the photo type and the amount
of photos needed to be taken. If there is no photo amount answer "1" but ONLY
if the action is Take Picture, otherwise answer "none". If there is no photo
type answer "none".

Sentence: {sentence}

Action:

Location:

Photo Type:

Photo Amount
"""

command2 = PromptTemplate(
    input_variables = ["sentence"],
    template = prompt_command
)

# Action Chain Creation
command_chain2 = LLMChain(llm = llm,
                        prompt = command2,
                        output_key = "breakdown2")

# Necessary import for the Simple Sequential Chain.
from langchain.chains import SimpleSequentialChain

# Connecting the two created chains via the SimpleSequentialChain.
sentence_command_chain = SimpleSequentialChain(
    chains=[sentence_chain, command_chain2], verbose = True
)

# Testing to make sure the output of the sentence chain was used as the input for the second implementation of the command chain.
# Conection Test
holder5 = sentence_command_chain.run(transcription)
print(holder5)


# UAV Prompt Creation
"""Implementation will be here shortly."""
