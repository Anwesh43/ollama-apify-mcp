from services.ollama_service import OllamaService
from dotenv import load_dotenv
from models.message import Message 
load_dotenv()

ollamaService = OllamaService()

#print(ollamaService.getModels())
#print(ollamaService.getModelDetails("gemma3:12b"))
#print(ollamaService.generateResponse("gemma3:12b", "Give a short story involving boat and old man in 100 words"))

messages = [Message(role = "system", content = "You are a helpful ai agent that will help in calculation"), Message(role = "user", content = "What is 2 + 2")]

print(ollamaService.chatResponse("gemma3:12b", messages=messages))