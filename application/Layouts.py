#Esta é a biblioteca usada para fazer a interface


import PySimpleGUI as sg
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
FontTitle = ("Times New Roman", 60)
FontSubtitle = ("Times New Roman", 20)
font2 = ("Times New Roman", 6)
font3 = ("Times New Roman", 24)

#Essa função aplica o tema à janela

sg.theme('MyCreatedTheme') 

#Aqui se definem os layouts das janelas de interface

#Layout do menu principal
MenuPrincipalLayout = [
    [sg.Text('Autotech', font = FontTitle)],
    [sg.Text('Menu Principal', font = FontSubtitle)],
    [sg.Button('Preencher Novo Contrato', font=font)],
    [sg.Button('Preferências',  font=font)],
    [sg.Button('Sair', font=font)]
]

#Layout do Menu de Contratos
MenuContratosLayout = [
    [sg.Text('Menu de Seleção', font = font3)],
    [sg.Text('')],
    [sg.Button('Contrato de Power BI')],
    [sg.Button('Contrato de Automação de Contratos')],
    [sg.Button('Sair')]
]

#Layout do Menu de Preferências
PreferenciasLayout = [
    [sg.Text('Aqui você pode personalizar sua experiência com o AutoContract')],
    [sg.Text('Selecione a cor que deseja no background(O programa aceita códigos hexadecimais de cores no padrão #000000):'), sg.InputText()],
    [sg.Text('Selecione aqui a cor que deseja nas letras das janelas:'), sg.InputText()]
]

#Layout do Formulário
FormularioLayout1 = [
    [sg.Text('Informações do Cliente', font=font3)],
    [sg.Text('Indique o Nome do Cliente:'), sg.InputText(), sg.Text('                   Indique o Nome da Empresa Cliente:'), sg.InputText()],
    [sg.Text('Indique o CNPJ do Cliente:'), sg.InputText(), sg.Text('                   Indique o Endereço do Cliente:'), sg.InputText()],
    [sg.Text('Indique o CEP do Cliente:'), sg.InputText(), sg.Text('                     Indique a Cidade e o Estado do Cliente:'), sg.InputText()],
    [sg.Text('Indique o Nome do Presidente Cliente:'), sg.InputText(), sg.Text('   Indique o CPF do Presidente Cliente:'), sg.InputText()],
    [sg.Text('Indique o RG do Presidente Cliente:'), sg.InputText(), sg.Text('       Indique o EMAIL do Cliente:'), sg.InputText()],
    [sg.Button('Continuar'), sg.Button('Sair')]
    ]

FormularioLayout2 =[
    [sg.Text('Informações da EJ', font=font3)],
    [sg.Text('Indique o Nome da EJ:'), sg.InputText(), sg.Text('                Indique o CNPJ da EJ: '), sg.InputText()],
    [sg.Text('Indique o CEP da EJ:'), sg.InputText(), sg.Text('                  Indique o Presidente da EJ: '), sg.InputText()],
    [sg.Text('Indique o CPF do Presidente:'), sg.InputText(), sg.Text('       Indique o RG do Presidente: '), sg.InputText()],
    [sg.Text('Indique o Endereço do Presidente:'), sg.InputText(), sg.Text('Indique o EMAIL da EJ: '), sg.InputText()],
    [sg.Button('Continuar'), sg.Button('Sair')]
]

FormularioLayout3 =[
    [sg.Text('Dados Financeiros', font = font3)],
    [sg.Text('Indique o Valor Final do Serviço: '), sg.InputText()],
    [sg.Text('Faça uma breve descrição de como será a forma de pagamento:'), sg.InputText()],
    [sg.Text('Indique o Titular da Conta que o pagamento será efetuado:'), sg.InputText()],
    [sg.Text('Indique o CNPJ da Conta do Pagamento: '), sg.InputText()],
    [sg.Text('Inidique o Banco em que será efetuado o pagamento:'), sg.InputText()],
    [sg.Text('Indique a Agência do Banco(Com dígito):'), sg.InputText()], 
    [sg.Text("Indique a Conta(Com dígito): "), sg.InputText()],
    [sg.Button('Continuar'), sg.Button('Sair')]
]


FormularioLayout4 = [
    [sg.Text('Dados Finais', font=font3)],
    [sg.Text('Faça uma descrição do sistema: '), sg.InputText()],
    [sg.Text('Indique o Número de Controle: '), sg.InputText()], 
    [sg.Text('Data no formato xx/xx/xxxx:'), sg.InputText('xx/xx/xxxx')],
    [sg.Text('Indique o Nome do Representante da Empresa Cliente:'), sg.InputText()], 
    [sg.Text('Indique o CPF do Representante:'), sg.InputText()],
    [sg.Text('Indique o Nome da Testemunha 1'), sg.InputText()], 
    [sg.Text('Indique o CPF da Testemunha 1:'), sg.InputText()],
    [sg.Text('Indique o Nome da Testemunha 2'), sg.InputText()], 
    [sg.Text('Indique o CPF da Testemunha 2:'), sg.InputText()],
    [sg.Text('Faça uma descrição do sistema: '), sg.InputText()],
    [sg.Button('Continuar'), sg.Button('Sair')]
]

FormularioLayout5 = [
    [sg.Text('Dos Prazos', font=font3)],
    [sg.Text('Prazo para Elaboração inicial e planejamento do projeto: '), sg.InputText()],
    [sg.Text('Prazo para a compra e obtenção dos materiais necessários para o projeto: '), sg.InputText()],
    [sg.Text('Prazo para desenvolvimento prático do projeto: '), sg.InputText()],
    [sg.Text('Prazo para compra e obtenção dos materiais necessários para o projeto: '), sg.InputText()],
    [sg.Text('Prazo para instalação do projeto no local solicitado pelo contratante: '), sg.InputText()],
    [sg.Button('Finalizar'), sg.Button('Sair')]
    ]