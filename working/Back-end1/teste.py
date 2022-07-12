beta = 'Isso e um beta'
h1 = '{size: 54px;\n\tfont-family: Georgia, \'Times New Roman\', Times, serif;}'
h2 = '{text-align: center;\n\tfont-family: Georgia, \'Times New Roman\', Times, serif;}'
body ='{text-align: justify;\n\tmax-width: 650px;\n\tfont-family: Georgia, \'Times New Roman\', Times, serif;\n\tfont-size: 16px;\n\tpadding: 0;\n\tmargin: 0 auto !important;}'

Contratohtml = open('Contrato.html', 'w')
Contratohtml.write(f'<!DOCTYPE>\n\t<html>\n\t<meta charset="utf-8/">\n\t<meta name="viewport" content="width=297x420" initialscale="1">\n\t<title>Template Autotech</title>\n\t<style>\n\th1 {h1}\n\th2 {h2}\n\tbody {body}\n\t</style>\n\t<h1>{beta}')
Contratohtml.close()