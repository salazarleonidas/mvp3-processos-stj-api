from pydantic import BaseModel

from typing import Optional, List
from  model import Base, Fase

class FaseSchema(BaseModel):
    """ Define como uma nova fase a ser inserido deve ser representado
    """
    numeroRegistro: str = '2023/0104863-0'
    fase: str = "Juntada de Certidão : Ausência de CPF/CNPJ (581)"


class FaseBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no registro do processo.
    """
    numeroRegistro: str = "0000/0000000-0"


class FaseViewSchema(BaseModel):
    """ Define como uma fase será retornado: fase.
    """
    numeroRegistro: str = '2023/0104863-0'
    fase: str = 'Juntada de Certidão : Ausência de CPF/CNPJ (581)'


def apresenta_fase(fase: Fase):


    """ Retorna uma representação do Fase seguindo o schema definido em
        FaseViewSchema.
    """
    return {
        "numeroRegistro": fase.numeroRegistro,
        "fase": fase.fase,
    }



class ListagemFasesSchema(BaseModel):
    """ Define como uma listagem de fases será retornada.
    """

    fases:List[FaseSchema]


def apresenta_fases(fases: List[Fase]):
    """ Retorna uma representação do processo seguindo o schema definido em
        ProcessoViewSchema.
    """
    result = []
    for fase in fases:
        result.append({
            "numeroRegistro": fase.numeroRegistro,
            "fase": fase.fase
        })

    return {"fases": result}
