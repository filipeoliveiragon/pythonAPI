from datetime import datetime
from fastapi import HTTPException
from sqlalchemy.orm import Session
from tbr_api.infra.models.atividade_model import AtividadesModel
# from tbr_api.crud.user_crud import listaUsuario
from tbr_api.crud import user_crud
from tbr_api.infra.models.user_model import UserModel
from tbr_api.schemas.atividade_schema import Atividade, AtividadeCreate, AtividadePut, AtividadePatch


# data_atual = datetime.today().strftime('%Y-%m-%d')

def listarAtividades(db: Session) -> Atividade:
    return db.query(AtividadesModel).all()


def criaAtividade(db: Session, atividade_create: AtividadeCreate) -> AtividadesModel:
    user_crud.listaUsuario(db, atividade_create.id_user)
    
    db_atividade = AtividadesModel(**atividade_create.dict())
    
    db_atividade.dataDeCriacao = datetime.now()
    
    db.add(db_atividade)
    db.commit()
    db.refresh(db_atividade)
    return db_atividade


def listaAtividade(db: Session, id: int) -> UserModel:
    db_atividade = db.query(AtividadesModel).filter(AtividadesModel.id == id).first()
    if db_atividade is None:
        raise HTTPException(status_code=404, detail="Atividade não encontrada!")
    return db_atividade


def editaAtividadePut(db: Session, id: int, atividade_put: AtividadePut) -> Atividade:
    db_atividade = db.query(AtividadesModel).filter(AtividadesModel.id == id).first()
    if db_atividade is None:
        raise HTTPException(status_code=404, detail="Atividade não encontrada!")
    
    for key, value in atividade_put.dict().items():
        setattr(db_atividade, key, value)
    
    db_atividade.dataDeEdicao = datetime.now()
    
    db.add(db_atividade)
    db.commit()
    db.refresh(db_atividade)
    
    return db_atividade


def editaAtividadePatch(db: Session, id: int, atividade_patch: AtividadePatch):
    db_atividade = db.query(AtividadesModel).filter(AtividadesModel.id == id).first()
    if db_atividade is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!")
    
    patch_fields = atividade_patch.dict(exclude_unset=True)
    
    for key, value in patch_fields.items():
        setattr(db_atividade, key, value)
        
    db_atividade.dataDeEdicao = datetime.now()
    
    db.add(db_atividade)
    db.commit()
    db.refresh(db_atividade)
    
    return db_atividade

def listaUsuarioAtividade(db: Session, id: int):
    db_atividade = listaAtividade(db, id)
    return user_crud.listaUsuario(db, db_atividade.id_user)


def deletaAtividade(db: Session, id: int):
    db_atividade = db.query(AtividadesModel).filter(AtividadesModel.id == id).first()
    if db_atividade is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrado!")
    
    db.delete(db_atividade)
    db.commit()
    
    return {"message": "Atividade deletada!"}