#Importa a biblioteca de funções
#encoding: utf-8
# -*- coding: utf-8 -*-
import Functions as fct
import teste
import htmlToPDF as pdf
#Executa o programa
fct.MenuPrincipal()
teste.escrever_contrato()
pdf.html_to_pdf("application/Contrato.html", "ContratoFinal.pdf")