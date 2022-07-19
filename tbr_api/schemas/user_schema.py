from pydantic import BaseModel
from ..schemas.atividade_schema import Atividade

class UserBase(BaseModel):
    nome: str
    email: str
    telefone: str
    atividades: list[Atividade]
    
class User(UserBase):
    id: int
    
    class Config:
        orm_mode = True
        
class UserCreate(BaseModel):
    nome: str
    email: str
    telefone: str
    

class UserPut(UserBase):
    pass

class UserPatch(BaseModel):
    nome: str | None
    email: str | None
    telefone: str | None