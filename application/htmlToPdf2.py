
def FazerPdf():
    import pdfkit
    pdfkit.from_file('Contrato.html', 'ContratoFinal.pdf')
