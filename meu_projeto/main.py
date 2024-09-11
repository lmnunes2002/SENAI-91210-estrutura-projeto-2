import os
from models.funcionarios import Funcionario
from models.funcionarios import Endereco
from models.enums.unidade_federativa import Unidadefederativa
from models.enums.setor import Setor
from models.enums.sexo import Sexo

os.system("cls||clear")

endereco_1 = Endereco("Rua A", "17", "Lado do posto", "12345-678", "Salvador", Unidadefederativa.BAHIA)
funcionario_1 = Funcionario("Lucas", 22, Sexo.MASCULINO, Setor.ENGENHARIA, endereco_1)

print(funcionario_1)