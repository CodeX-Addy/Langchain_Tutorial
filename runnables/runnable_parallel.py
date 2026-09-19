from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
summary = ChatPromptTemplate.from_template("Summarize this {text}") | model | StrOutputParser()
sentiment = ChatPromptTemplate.from_template("Give a one word sentiment for this: {text}") | model | StrOutputParser()

parallel = RunnableParallel(summary=summary, sentiment=sentiment)
result = parallel.invoke({"text": "Ahh i missed the new iphone offer.."})
print(f"Summary is: {result['summary']} and sentiment is: {result['sentiment']}")
