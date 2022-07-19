from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from ..config.database import Base

class AtividadesModel(Base):
    __tablename__ = "tbl_atividades"

    id = Column(Integer, primary_key =True,autoincrement = True)
    nome = Column(String, nullable=False)
    dataDeCriacao = Column(DateTime, nullable = False)
    dataDeEdicao = Column(DateTime, nullable = True)
    
    id_user = Column(Integer, ForeignKey("tbl_users.id"))