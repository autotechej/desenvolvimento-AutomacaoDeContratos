#Importa a biblioteca de funções
#encoding: utf-8
# -*- coding: utf-8 -*-
import Functions as fct
import teste
import os
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
import htmlToPDF as pdf
#Executa o programa
fct.MenuPrincipal()
teste.escrever_contrato()
if __name__ == "__main__":

    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(CURRENT_DIR, f"{pdf.arquivo}.html")
    print(filename)

    pdf.html_to_pdf(filename, f"{pdf.nomeF}.pdf")