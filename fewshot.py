"""
This module contains the FewShot4UAVs class which is used to get the transcription and command.
"""

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain
from prompts import PROMPT_TRANSCRIBE, EXAMPLES_FEW_SHOT


class FewShot4UAVs:
    """
    Class used to get the transcription and command.

    Attributes:
        llm: LangChain OpenAI - language model instance

    Methods:
        get_transcription(text)
            Returns the transcription chain.
        format_command(chain)
            Returns the sentence command chain.
        get_command(text)
            Returns the final command.
    """

    def __init__(self) -> None:
        """Initializes the object with all necessary attributes"""
        self.llm = OpenAI(model_name="text-davinci-003", temperature=0.0)

    def get_transcription(self, text):  # pylint: disable=unused-argument
        """
        Returns the transcription chain.

        :param text: str, text to transcribe
        :return: LLM sentence chain
        """
        transcribe_prompt = PromptTemplate(
            input_variables=["text"],
            template=PROMPT_TRANSCRIBE
        )

        sentence_chain = LLMChain(llm=self.llm,
                                  prompt=transcribe_prompt,
                                  output_key="sentence")

        return sentence_chain

    def format_command(self, chain):
        """
        Returns the sentence command chain.

        :param chain: LLM sentence chain
        :return: sentence command chain
        """
        command = PromptTemplate(
            input_variables=["sentence", "command"],
            template="sentence: {sentence}\n{command}"
        )

        few_shot_prompt = FewShotPromptTemplate(
            examples=EXAMPLES_FEW_SHOT,
            example_prompt=command,
            suffix="sentence: {sentence}",
            input_variables=["sentence"]
        )

        command_chain = LLMChain(llm=self.llm, prompt=few_shot_prompt, output_key="output")

        sentence_chain = chain

        sentence_command_chain = SimpleSequentialChain(
            chains=[sentence_chain, command_chain], verbose=True
        )

        return sentence_command_chain

    def get_command(self, text):
        """
        Returns the command

        :param text: str, text to get command
        :return: final command
        """
        command = self.format_command(self.get_transcription(text))
        return command.run(text)
