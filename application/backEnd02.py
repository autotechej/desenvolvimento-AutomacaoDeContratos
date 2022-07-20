import os
import sys

from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
arquivo = str(input("Digite o nome do arquivo:\n"))        #nome do arquivo .html de entrada sem o final
nomeF = str(input("Digite o nome final do arquivo em pdf\n"))   #nome doarquivo .pdf de saida sem o final


def html_to_pdf(html, pdf):      #função principal
    app = QtWidgets.QApplication(sys.argv)

    page = QtWebEngineWidgets.QWebEnginePage()

    '''def handle_print_finished(filename, status): #aqui é pra dizer no print se deu certo ou não
        print("Terminado!", filename, status)
        QtWidgets.QApplication.quit()

    def handle_load_finished(status):   
        if status:
            page.printToPdf(pdf)
        else:
            print("Falhou")
            QtWidgets.QApplication.quit()
'''
   
    page.load(QtCore.QUrl.fromLocalFile(html))
    app.exec_()

if __name__ == "__main__":

    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(CURRENT_DIR, "Contrato.html")

    html_to_pdf(filename, "ContratoFinal.pdf")   #chamando a função para teste, pode usar "nome_do_arquivo para usar um arquivo fixo"
    