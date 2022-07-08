#
#
#   Projeto desenvolvido pela Autotech - Empresa Junior de Automação do IFCE Fortaleza
#
#

#import interface

from classes import *
from functions import *

#
#   Leitura dos dados da interface
#

contratada = empresa()
contratante = empresa()
Projeto = projeto()

contratada.nome = "Empresa contratada"
contratada.tipo = "CNPJ"
contratada.id   = "10232"
contratada.nome_repr = "Joao"
contratada.id_repr = "1234"
contratada.endereco.rua = "Rua 1"
contratada.endereco.numero = "25"
contratada.endereco.bairro = "Bairro A"
contratada.endereco.cep = "5000"
contratada.endereco.complemento = "Casa A"
contratada.endereco.cidade = "Fortaleza"
contratada.endereco.estado = "Ceara"
contratada.endereco.rua_repr = "Rua 2"
contratada.endereco.numero_repr = "10"
contratada.endereco.bairro_repr = "Bairro B"
contratada.endereco.cep_repr = "5001"
contratada.endereco.complemento_repr = "Casa B"
contratada.endereco.cidade_repr = "Fortaleza"
contratada.endereco.estado_repr = "Ceara"

contratante.nome = "Cliente"
contratante.tipo = "CNPJ"
contratante.id   = "CNPJ do cliente"
contratante.nome_repr = "Cliente Joao"
contratante.id_repr = "1234"
contratante.endereco.rua = "Rua 1"
contratante.endereco.numero = "25"
contratante.endereco.bairro = "Bairro A"
contratante.endereco.cep = "5000"
contratante.endereco.complemento = "Casa A"
contratante.endereco.cidade = "Fortaleza"
contratante.endereco.estado = "Ceara"
contratante.endereco.rua_repr = "Rua 2"
contratante.endereco.numero_repr = "10"
contratante.endereco.bairro_repr = "Bairro B"
contratante.endereco.cep_repr = "5001"
contratante.endereco.complemento_repr = "Casa B"
contratante.endereco.cidade_repr = "Fortaleza"
contratante.endereco.estado_repr = "Ceara"

Projeto.id = "0001"
Projeto.tipo = "Automação de contratos"
Projeto.valorTotal = 1000
Projeto.numeroParcelas = 2
Projeto.prazo = 30


#
# Leitura do HTML (template escolhido)
#