from pydantic import BaseModel

class Pessoa(BaseModel):
    nome: str
    idade: int
    cidade: str
