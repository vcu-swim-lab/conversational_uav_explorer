# Necessary imports
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from prompts import prompt_transcribe, prompt_command

# API Key
os.environ["OPENAI_API_KEY"] = "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"

# Initializing OpenAI as the large language model
llm = OpenAI(temperature=0.0)


def get_transcription(text):
    # Transcription prompt
    transcribe_prompt = PromptTemplate(
        input_variables=["text"],
        template=prompt_transcribe
    )

    # Creating transcription chain
    sentence_chain = LLMChain(llm=llm,
                              prompt=transcribe_prompt,
                              output_key="sentence")

    return sentence_chain


# Method takes in the transcription chain to link them together with a sequential chain, which is then returned.
def format_command(chain):
    # Prompt Creation
    command = PromptTemplate(
        input_variables=["sentence"],
        template=prompt_command
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
    command = format_command(get_transcription(text))
    return command.run(text)

