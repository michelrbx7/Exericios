from .endereco import Endereco # type: ignore
from .funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str,salario: float, endereco: Endereco, ) -> None:
        super().__init__(nome, telefone, email, endereco, salario)
        self.crm = crm # type: ignore


    def _verificar_salario(self, salario: float) -> float:
        return super()._verificar_salario(salario)

    def _verificar_nome(self, nome: str) -> str:
        return super()._verificar_nome(nome)
    
    def __str__(self) -> str:
        return (super().__str__() + 
                f"\nCRM: {self.crm}")

        

