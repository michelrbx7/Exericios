import pytest
from projeto.models.endereco import Endereco
from projeto.models.medico import Medico

@pytest.fixture
def teste_medico():
    medico1 = Medico("Rau","7847564112", "rau@gmail.com",1000.00,Endereco("avenida gil","27","proximo a vala","54545641","Salvador"))
    return medico1

def test_validar_nome_vazio(teste_medico: Medico):
    with pytest.raises(ValueError,mtach ="O Nome não pode sere vazio"):
        Medico("","7847564112", "rau@gmail.com",1000.00,Endereco("avenida gil","27","proximo a vala","54545641","Salvador"))
    
def test_validar_nome_tipo(teste_medico: Medico):
    with pytest.raises(ValueError,mtach ="O Nome deve ser um texto"):
        Medico(4564231,"7847564112", "rau@gmail.com",1000.00,Endereco("avenida gil","27","proximo a vala","54545641","Salvador"))

def test_validar_email_tipo(teste_medico: Medico):
    with pytest.raises(ValueError,match="Digite um email válido"):
        Medico("Rau","7847564112", "rau@.com",1000.00,Endereco("avenida gil","27","proximo a vala","54545641","Salvador"))   



def test_validar_nome_medico(teste_medico: Medico):
    assert teste_medico.nome == "rau"
    
def test_validar_email_medico(teste_medico: Medico):
    assert teste_medico.email == "rau@gmail.com"   
    

