from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
prompt = ChatPromptTemplate.from_template("Explain this {topic} in one {word_cnt} words..")

chain = prompt | model | StrOutputParser()

result = chain.invoke({"topic": "gradient descent", "word_cnt" : 20})
print(result)
