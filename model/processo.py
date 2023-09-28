from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union
from  model import Base, Fase

class Processo(Base):

    __tablename__ = 'processo'

    id = Column("pk_processo", Integer, primary_key=True)
    numeroRegistro = Column(String(140), unique=True)
    data = Column(DateTime, default=datetime.now())
    uf = Column(String(2))
    data_insercao = Column(DateTime, default=datetime.now())

    fases = relationship("Fase")

    def __init__(self,
                numeroRegistro:str,
                uf:str,
                data:Union[DateTime, None] = None,
                data_insercao:Union[DateTime, None] = None):
        """
        Cria um Processo
        """
        self.numeroRegistro = numeroRegistro
        self.data = data
        self.uf = uf
        
        if data_insercao:
            self.data_insercao = data_insercao

    def adiciona_fase(self, fase:Fase):
        """ Adiciona um novo fase ao Processo
        """
        self.fases.append(fase)
