from projeto.models.endereco import Endereco  # type: ignore
from projeto.models.funcionario import Funcionario

class engenheiro(Funcionario):
   def __init__(self,crea:str, nome: str, telefone: str, email: str, salario: float,endereco: Endereco) -> None:
       super().__init__(nome, telefone, email, endereco, salario)
       self.crea = crea 


   def _verificar_salario(self, salario: float) -> float:
        return super()._verificar_salario(salario)

   def _verificar_nome(self, nome: str) -> str:
        return super()._verificar_nome(nome)

   def __str__(self) -> str:
        return (super().__str__() + 
                f"\nCREA: {self.crea}")
   
   