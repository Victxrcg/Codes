from pydantic import BaseModel
class Usuario(BaseModel):
    nome: str
    idade:int
    sexo: str
    
usuario = Usuario(nome='Victor',idade=20,sexo="Masculino")
print(usuario.nome)
print(usuario.idade)
print(usuario.sexo)



