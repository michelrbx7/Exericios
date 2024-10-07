from abc import ABC,abstractmethod
from projeto.models.endereco import Endereco # type: ignore


class Funcionario(ABC):
    def __init__(self,nome:str,telefone:str,email:str,endereco:Endereco,salario:float) ->None:
        self.nome = nome
        self. telefone = telefone
        self. email = email
        self. endereco = endereco
        self.salario = self._verificar_salario(salario)

    def _verificar_salario(self, salario:float) -> float:
        
        if not isinstance(salario, float):
            raise TypeError("Digite somente numeros reais com o ponto separando casas decimais.")
        if salario < 0:
            raise ValueError("Digite um numero que seja real e positivo.")
        return salario
    
    

    def __str__(self) ->str:
        return f"\nNome {self.nome} \nTelefone{self.telefone} \nEmail{self.email} \nEndereço{self.endereco}"
