import requests 
from typing import Dict 
class BaseHttpClient:
    def __init__(self, base_url : str):
        self.base_url = base_url
    
    def getCall(self, endpoint : str, headers : Dict):
        response = requests.get(f"{self.base_url}/{endpoint}", headers = headers)
        return response.json() 
    
    def postCall(self, endpoint : str, data : Dict, headers : Dict):
        print("DATA", data)
        response = requests.post(f"{self.base_url}/{endpoint}", json = data, headers = headers)
        return response.json()
    
    def postCallText(self, endpoint : str, data : Dict, headers : Dict):
        print("DATA", data)
        response = requests.post(f"{self.base_url}/{endpoint}", json = data, headers = headers)
        return response.text