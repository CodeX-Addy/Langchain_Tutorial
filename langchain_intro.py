import getpass
import os
from langchain.chat_models import init_chat_model

## Change the best model as per the availabilty

class HandleLLMSummary():
    def __init__(self):
        self.model = init_chat_model(
            "gemini-2.5-flash", model_provider="google_genai")

    def generate_summary(self, response):
        summary_query = f"Generate a concise summary of the following response: {response.content}"
        return self.model.invoke(summary_query).content

if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = getpass.getpass(
      "Enter API key for Google Gemini: ")

user_input = input("Enter your message to chat: ")

response = HandleLLMSummary().model.invoke(user_input)

print(response.content)

print("\nGenerating summary...\n")
summary = HandleLLMSummary().generate_summary(response)
print(summary)
