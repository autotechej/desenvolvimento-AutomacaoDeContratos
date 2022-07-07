#Esta é a biblioteca usada para fazer a interface

import PySimpleGUI as sg

#Aqui são definidos os parâmetros do tema da interface, nesse caso foram utilizadas as cores da EJ

sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {'BACKGROUND': '#02A69D', 
                                        'TEXT': '#4E2559', 
                                        'INPUT': '#34BF98', 
                                        'TEXT_INPUT': '#4E2559', 
                                        'SCROLL': '#EB7F00', 
                                        'BUTTON': ('#EB7F00', '#4E2559'), 
                                        'PROGRESS': ('# D1826B', '# CC8019'), 
                                        'BORDER': 1, 'SLIDER_DEPTH': 0,
                                        'PROGRESS_DEPTH': 0, }
font = ("Times New Roman", 12)
FontTitle = ("TImes New Roman", 16, )
sg.theme('MyCreatedTheme') 
layout = [
    [sg.Text('AUTOTECH', font = FontTitle)],
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
window = sg.Window('Número de controle', layout)
event, values = window.read()
print(event, values)