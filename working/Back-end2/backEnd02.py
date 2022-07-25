import os
import sys

from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
arquivo = str(input("Digite o nome do arquivo:\n"))
nomeF = str(input("Digite o nome final do arquivo em pdf\n"))


def html_to_pdf(html, pdf):
    app = QtWidgets.QApplication(sys.argv)

    page = QtWebEngineWidgets.QWebEnginePage()

    def handle_print_finished(filename, status):
        print("Terminado!", filename, status)
        QtWidgets.QApplication.quit()

    def handle_load_finished(status):
        if status:
            page.printToPdf(pdf)
        else:
            print("Falhou")
            QtWidgets.QApplication.quit()

    page.pdfPrintingFinished.connect(handle_print_finished)
    page.loadFinished.connect(handle_load_finished)
    page.load(QtCore.QUrl.fromLocalFile(html))
    app.exec_()

if __name__ == "__main__":

    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(CURRENT_DIR, f"{arquivo}.html")
    print(filename)

    html_to_pdf(filename, f"{nomeF}.pdf")
    