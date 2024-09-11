from models.enums.sexo import Sexo
from models.enums.setor import Setor
from models.enderecos import Endereco

class Funcionario:
    def __init__(self, nome: str, idade: int, sexo: Sexo, setor: Setor, endereco: Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.setor = setor
        self.endereco = endereco

    def __str__(self) -> str:
        return(
            f"Funcinário: "
            f"\nNome: {self.nome}"
            f"\nIdade: {self.idade}"
            f"\nSexo: {self.sexo.value}"
            f"\nSetor: {self.setor.value}"
            f"\n\nEndereço: {self.endereco}"
        )