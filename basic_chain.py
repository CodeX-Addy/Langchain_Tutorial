from langchain.chains import LLMChain
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = Ollama(model="gemma:7b-instruct-q2_K",
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]), temperature=0.8,)

## Basic Q&A Chain
prompt = PromptTemplate(
    input_variables = ["topic"],
    template = "Tell me about this topic {topic}"
)

chain = LLMChain(llm=llm, prompt=prompt)
print(chain.invoke("India"))
