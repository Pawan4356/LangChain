from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file -> HF = "your_api_key_here"

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

while True:
    userInput = input("You: ")
    if userInput.lower() in ['exit', 'quit']:
        print("Exiting chat...")
        break
    else:
        print("Bot: " + model.invoke(userInput).content + "\n", end="")