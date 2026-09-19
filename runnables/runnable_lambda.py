from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableLambda

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
prompt = ChatPromptTemplate.from_template("Explain this {topic} in one sentence")

chain = prompt | model | StrOutputParser()

upper = RunnableLambda(lambda x: x.upper())
result = chain | upper

print(result.invoke({"topic": "APIs"}))
 
