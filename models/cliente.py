from dataclasses import dataclass
import datetime


@dataclass

class Cliente:
    id: int
    nome: str
    cpf: str
    telefone: str
    email: str
    endereco: str
    data_nascimento: datetime

    def __str__(self):
        return f"Cliente(id={self.id}, nome={self.nome}, cpf={self.cpf}, telefone={self.telefone}, email={self.email}, endereco={self.endereco}, data_nascimento={self.data_nascimento})"