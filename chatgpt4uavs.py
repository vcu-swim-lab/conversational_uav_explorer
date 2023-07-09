# Necessary imports
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain

# API Key
os.environ["OPENAI_API_KEY"] = "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"

# Initializing OpenAI as the large language model
llm = OpenAI(temperature=0.9)


def get_transcription(text):
    # Creating a Prompt and Chain with the transcription so it can be passed to the official Command Prompt via
    # Simple Sequential chain Transcription template
    transcribe = """You are to pass the aubio transcription to the next
  chain. Do not alter the transcription in any way.

  Transcription: {text}
  """

    # Transcription prompt
    transcribe_prompt = PromptTemplate(
        input_variables=["text"],
        template=transcribe
    )

    # Creating transcription chain
    sentence_chain = LLMChain(llm=llm,
                              prompt=transcribe_prompt,
                              output_key="sentence")

    return sentence_chain


# Method takes in the transcription chain to link them together with a sequential chain, which is then returned.
def format_command(chain):
    # Prompt template
    prompt = """You are in control of an Unmanned Aerial Vehicle or UAV. You are going to be given a
    sentence command, you need to find the action of the sentence. The action will be, Take Picture,
    Take Off, Land and Go To. If the action is "Take Off" or "Land" you don't need any further information
    for the location. If the action is "Take Picture" or "Go To" you'll need to find where to carry out the action.
    You need to find. If you can't find an action or location, answer with "none". You need to return the command
    in this format: command <command> \t <goal>

    Sentence: {sentence}
    """

    # Prompt Creation
    command = PromptTemplate(
        input_variables=["sentence"],
        template=prompt
    )

    # Chain Creation
    command_chain = LLMChain(llm=llm, prompt=command, output_key="output")

    # Initializing chain needed to connect using the parameters
    sentence_chain = chain

    # Connecting the two created chains via the SimpleSequentialChain.
    sentence_command_chain = SimpleSequentialChain(
        chains=[sentence_chain, command_chain], verbose=True
    )

    # Returning the new combined chain
    return sentence_command_chain


# Method to get the actual formatted command
def get_command(text):
    return format_command(get_transcription(text))


# METHOD TESTING
print(get_command("Go to the red house on W Broad St."))

# The next part is to write the output of the final_command variable to a file
# IMPLEMENTATION BELOW SHORTLY
