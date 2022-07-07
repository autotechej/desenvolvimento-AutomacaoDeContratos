#Esta é a biblioteca usada para fazer a interface

import PySimpleGUI as sg
from sqlalchemy import case

#Aqui são definidos os parâmetros do tema da interface, nesse caso foram utilizadas as cores da EJ

sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {'BACKGROUND': 'Black', 
                                        'TEXT': '#02A69D', 
                                        'INPUT': '#02A69D', 
                                        'TEXT_INPUT': '#4E2559', 
                                        'SCROLL': '#EB7F00', 
                                        'BUTTON': ('Black', '#02A69D'), 
                                        'PROGRESS': ('# D1826B', '# CC8019'), 
                                        'BORDER': 1, 'SLIDER_DEPTH': 0,
                                        'PROGRESS_DEPTH': 0, }
font = ("Times New Roman", 12)
FontTitle = ("TImes New Roman", 16)
font2 = ("Times New Roman", 6)

#Essa função aplica o tema à janela

sg.theme('MyCreatedTheme') 

#Aqui se define o layout da janela de interface

#Layout do menu principal
MenuPrincipalLayout = [
    [sg.Button('Preencher Novo Contrato')],
    [sg.Button('Preferências')],
    [sg.Button('Sair')]
]

#Layout do 
MenuContratosLayout = [
    [sg.Text('Você possui dois tipos de contrato: Venda e Prestação de Serviços')],
    [sg.Text('Indique qual tipo de contrato você quer usar:'), sg.InputText()],
    [sg.Button('Continuar'), sg.Button('Sair')]
]

PreferenciasLayout = [
    [sg.Text('Aqui você pode personalizar sua experiência com o AutoContract')],
    [sg.Text('Selecione a cor que deseja no background(O programa aceita códigos hexadecimais de cores no padrão #000000):'), sg.InputText()],
    [sg.Text('Selecione aqui a cor que deseja nas letras das janelas:'), sg.InputText()]
]

layout = [
    [sg.Text('AUTOTECH', font = FontTitle), sg.Text('TM', font = font2)],
    [sg.Text('Bem-vindo ao sistema automatizado da Autotech para geração de contratos. Insira os dados conforme solicitados.',font = font)],
    [sg.Text('Insira o Nome do Cliente:', font = font), sg.InputText(), sg.Text('                            Insira o CNPJ do Cliente:', font = font), sg.InputText()],
    [sg.Text('Insira Endereço do Cliente:', font = font), sg.InputText(), sg.Text('                          Insira o CEP do Cliente:', font = font), sg.InputText()],
    [sg.Text('Insira a Cidade, Estado do Cliente:', font = font), sg.InputText(), sg.Text('              Insira o Nome do Presidente da Empresa:', font = font), sg.InputText()],
    [sg.Text('Insira o CPF do Presidente:', font = font), sg.InputText(), sg.Text('                         Insira o RG do Presidente:', font = font), sg.InputText()],
    [sg.Text('Insira o Endereço do Presidente:', font = font), sg.InputText(), sg.Text('                  Insira a descrição do sistema:', font = font), sg.InputText()],
    [sg.Text('Insira o objetivo do sistema:', font = font), sg.InputText(), sg.Text('                         Insira o Prazo:', font = font), sg.InputText()],
    [sg.Text('Insira a descrição mais detalhada do sistema:', font = font), sg.InputText()],
    [sg.Button('Confirmar')]
    ]

def Formulario():
    global FormularioWindow, event, values
    FormularioWindow = sg.Window("Autotech AutoContract", layout)
    event, values = FormularioWindow.read()
    print(event, values)

def MenuPreencherContratos():
    global ContratosWindow, event2, values2, TipoContrato
    ContratosWindow = sg.Window("Autotech AutoContract", MenuContratosLayout)
    event2, values2 = ContratosWindow.read()
    TipoContrato = values2[0]
    if event2 == 'Continuar':
        if TipoContrato == 'Venda' or TipoContrato == 'Prestação de Serviços':
            Formulario()
    elif event2 == 'Sair':
        ContratosWindow.close()

def MenuPrincipal():
    global MenuWindow, event1, values1
    MenuWindow = sg.Window("Autotech AutoContract", MenuPrincipalLayout)
    event1, values1 = MenuWindow.read()
    if event1 == 'Preencher Novo Contrato':
        MenuPreencherContratos()
        MenuWindow.close()
    elif event1 == 'Preferências':
        MenuPreferencias()
        MenuWindow.close()
    elif event1 == 'Sair':
        MenuWindow.close()


def MenuPreferencias():
    global PreferenciasWindow, event3, values3
    PreferenciasWindow = sg.Window("Autotech AutoContract", PreferenciasLayout)
    event3, values3 = PreferenciasWindow.read()



layout = [
    [sg.Text('AUTOTECH', font = FontTitle), sg.Text('TM', font = font2)],
    [sg.Text('Bem-vindo ao sistema automatizado da Autotech para geração de contratos. Insira os dados conforme solicitados.',font = font)],
    [sg.Text('Insira o Nome do Cliente:', font = font), sg.InputText(), sg.Text('                            Insira o CNPJ do Cliente:', font = font), sg.InputText()],
    [sg.Text('Insira Endereço do Cliente:', font = font), sg.InputText(), sg.Text('                          Insira o CEP do Cliente:', font = font), sg.InputText()],
    [sg.Text('Insira a Cidade, Estado do Cliente:', font = font), sg.InputText(), sg.Text('              Insira o Nome do Presidente da Empresa:', font = font), sg.InputText()],
    [sg.Text('Insira o CPF do Presidente:', font = font), sg.InputText(), sg.Text('                         Insira o RG do Presidente:', font = font), sg.InputText()],
    [sg.Text('Insira o Endereço do Presidente:', font = font), sg.InputText(), sg.Text('                  Insira a descrição do sistema:', font = font), sg.InputText()],
    [sg.Text('Insira o objetivo do sistema:', font = font), sg.InputText(), sg.Text('                         Insira o Prazo:', font = font), sg.InputText()],
    [sg.Text('Insira a descrição mais detalhada do sistema:', font = font), sg.InputText()],
    [sg.Button('Confirmar')]
    ]
#A janela de nome Window é criada com a função abaixo

'''window = sg.Window('Autotech AutoContract', layout)'''

#Essa função lê os dados inseridos na janela. Event é a variável que armazena os dados dos botões e values os dados das caixas de texto

'''event, values = window.read()
print(event, values)'''

MenuPrincipal()