import { OpenAI } from "langchain/llms/openai";
import { PromptTemplate } from "langchain/prompts";
import { FewShotPromptTemplate } from "langchain/prompts/few_shot";
import { LLMChain, SimpleSequentialChain } from "langchain/chains";


class FewShot {
    constructor() {
        // Initializes object with model name and temperature
        this.llm = new OpenAI({ modelName: "text-davinci-003", temperature: 0.0 });
    }

    getTranscription(text) {
        // Returns the transcription chain
        const transcribePrompt = new PromptTemplate({
            inputVariables: ["text"],
            template: PROMPT_TRANSCRIBE
        });

        const sentenceChain = new LLMChain({
            llm: this.llm,
            prompt: transcribePrompt,
            outputKey: "sentence"
        });

        return sentenceChain;
    }

    formatCommand(chain) {
        // Returns the sentence command chain
        const command = new PromptTemplate({
            inputVariables: ["sentence", "command"],
            template: "sentence: {sentence}\n{command}"
        });

        const fewShotPrompt = new FewShotPromptTemplate({
            examples: EXAMPLES_FEW_SHOT,
            examplePrompt: command,
            suffix: "sentence: {sentence}",
            inputVariables: ["sentence"]
        });

        const commandChain = new LLMChain({
            llm: this.llm,
            prompt: fewShotPrompt,
            outputKey: "output"
        });

        const sentenceChain = chain;

        const sentenceCommandChain = new SimpleSequentialChain({
            chains: [sentenceChain, commandChain],
            verbose: true
        });

        return sentenceCommandChain;
    }

    getCommand(text) {
        // Returns the command
        const command = this.formatCommand(this.getTranscription(text));
        return command.run(text);
    }
}