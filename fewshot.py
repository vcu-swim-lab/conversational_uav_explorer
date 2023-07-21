import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from prompts import prompt_transcribe, prompt_command, examples_few_shot


class FewShot4UAVs:

    def __init__(self) -> None:
        os.environ["OPENAI_API_KEY"] = "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"
        self.llm = OpenAI(temperature=0.0)

    def get_transcription(self, text):
        transcribe_prompt = PromptTemplate(
            input_variables=["text"],
            template=prompt_transcribe
        )

        sentence_chain = LLMChain(llm=self.llm,
                                prompt=transcribe_prompt,
                                output_key="sentence")

        return sentence_chain


    def format_command(self, chain):
        command = PromptTemplate(
            input_variables=["sentence","command"],
            template="sentence: {sentence}\n{command}"
        )

        few_shot_prompt = FewShotPromptTemplate(
            examples=examples_few_shot, 
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

    def to_file(self, text):
        f = open("commands.txt", "a")
        f.write(text)
        f.close()

    def get_command(self, text):
        command = self.format_command(self.get_transcription(text))
        self.to_file(command.run(text))
        return command.run(text)

