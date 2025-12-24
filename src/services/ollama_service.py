
from .base_http_client import BaseHttpClient
import os 
from ..models.message import Message 
from typing import List, Dict 

class OllamaService:
    def __init__(self):
        self.client = BaseHttpClient(os.environ.get("OLLAMA_BASE_URL", ""))
        self.api_key = os.environ.get("OLLAMA_API_KEY", "")
    
    def getModels(self) -> List[Dict]:
        data = self.client.getCall("/tags", headers = {
            "Authorization": f"Bearer {self.api_key}"
        })
        models = data["models"]
        #print("MODELS", models)
        result = []
        for model in models:
            data = {}
            data["name"] = model["name"]
            data["size"] = model["size"]
            result.append(data)
        return result 
    
    def getModelDetails(self, model_name : str):
        modelDetails = self.client.postCall("/show", {"model": model_name},  headers = {
            "Authorization": f"Bearer {self.api_key}"
        })
        return modelDetails
    
    def createEmbedding(self, model_name : str, input : str):
        embeddingResponse = self.client.postCall("/embed", {
            "model": model_name,
            "input": input
        }, headers = {
            "Authorization": f"Bearer {self.api_key}"
        })
        return embeddingResponse
    
    def generateResponse(self, model_name : str, prompt : str):
        response = self.client.postCall("/generate", {
            "model": model_name,
            "prompt": prompt,
            "stream": False 
        }, headers = {
            "Authorization": f"Bearer {self.api_key}"
        })
        return response
    
    def chatResponse(self, model_name : str, messages : List[Message]):
        messagesArr = []
        for message in messages:
            messageResponse = {}
            messageResponse["role"] = message.role 
            messageResponse["content"] = message.content 
            messagesArr.append(messageResponse)
        response = self.client.postCall("/chat", {
            "messages": messagesArr,
            "model": model_name,
            "stream": False
        }, headers = {
            "Authorization": f"Bearer {self.api_key}"
        })
        return response 
    
ollama_service_instance = OllamaService()