from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from  model import Base


class Fase(Base):
    __tablename__ = 'fase'

    id = Column(Integer, primary_key=True)
    numeroRegistro = Column(String(140), ForeignKey("processo.numeroRegistro"), nullable=False)
    fase = Column(String(4000))
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, 
                fase:str,
                numeroRegistro:str,
                data_insercao:Union[DateTime, None] = None):
        """
        Cria uma Fase

        """
        self.fase = fase
        self.numeroRegistro = numeroRegistro
        
        if data_insercao:
            self.data_insercao = data_insercao
