from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    pregunta: str
    respuesta: str
    evidencia: str 

class PromptModel(BaseModel):
    prompt: List[Item]

