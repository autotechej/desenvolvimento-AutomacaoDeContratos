#
#
#   Projeto desenvolvido pela Autotech - Empresa Junior de Automação do IFCE Fortaleza
#
#

#import interface

from classes import *
from functions import *

#
#
#
#

contratada = empresa()
contratante = empresa()

askForData(contratante,contratada)


print('Nome da empresa contratante: {}'.format(contratante.nome))


