import PySimpleGUI as sg

layout = [
    [sg.Text('Bem-vindo ao sistema automatizado da Autotech para geração de contratos. Insira os dados conforme solicitados.')],
    [sg.Text('Insira o Nome do Cliente:'), sg.InputText()],
    [sg.Text('Insira o CNPJ do Cliente:'), sg.InputText()],
    [sg.Text('Insira Endereço do Cliente:'), sg.InputText()],
    [sg.Text('Insira o CEP do Cliente:'), sg.InputText()],
    [sg.Text('Insira a Cidade, Estado do Cliente:'), sg.InputText()],
    [sg.Text('Insira o Nome do Presidente da Empresa:'), sg.InputText()],
    [sg.Text('Insira o CPF do Presidente:'), sg.InputText()],
    [sg.Text('Insira o RG do Presidente:'), sg.InputText()],
    [sg.Text('Insira o Endereço do Presidente:'), sg.InputText()],
    [sg.Text('Insira a descrição do sistema:'), sg.InputText()],
    [sg.Text('Insira o objetivo do sistema:'), sg.InputText()],
    [sg.Text('Insira a descrição mais detalhada do sistema:'), sg.InputText()],
    [sg.Text('Insira o Prazo:'), sg.InputText()],
    [sg.Text('Insira o valor do serviço:'), sg.InputText()],
    [sg.Text('Insira os detalhes da forma de pagamento:'), sg.InputText()],
    [sg.Text('Insira o valor de juros(Caso o pagamento não seja efetuado no prazo):'), sg.InputText()],
    [sg.Text('Insira o email do cliente e da EJ:'), sg.InputText()],
    [sg.Text('Insira o nome da empresa cliente:'), sg.InputText()],
    [sg.Text('Insira o nome do representante da empresa:'), sg.InputText()],
    [sg.Text('Insira o CPF do representante da empresa:'), sg.InputText()],
    [sg.Text('Insira o nome do Presidente da EJ:'), sg.InputText()],
    [sg.Text('Insira o CPF do Presidente da EJ:'), sg.InputText()],
    [sg.Text('Insira o nome da Testemunha 1:'), sg.InputText()],
    [sg.Text('Insira o CPF da Testemunha 1:'), sg.InputText()],
    [sg.Text('Insira o nome da Testemunha 2:'), sg.InputText()],
    [sg.Text('Insira o CPF da Testemunha 2:'), sg.InputText()],
    [sg.Text('Insira o CNPJ da EJ:'), sg.InputText()],
    [sg.Text('Insira o CEP da EJ:'), sg.InputText()],
    [sg.Text('Insira o RG do Presidente da EJ:'), sg.InputText()],
    [sg.Text('Insira o endereço do Presidente da EJ:'), sg.InputText()],
    [sg.Text('Insira o Titular do Pagamento:'), sg.InputText()],
    [sg.Text('Insira a Agência do Pagamento:'), sg.InputText()],
    [sg.Text('Insira a Conta do Pagamento:'), sg.InputText()],
    [sg.Text('Insira o CNPJ do Pagamento:'), sg.InputText()],
    [sg.Text('Insira o Banco do Pagamento:'), sg.InputText()],
    [sg.Text('Insira a data que o contrato foi finalizado:'), sg.InputText()],
    [sg.Button('ok')]
]
window = sg.Window('Número de controle', layout)
event, values = window.read()
print(event, values)

Nome_Cliente = values[0]
CNPJ_Cliente = values[1]
Endereco_Cliente = values[2]
CEP_Cliente = values[3]
Cidade_Estado_Cliente = values[4]
Presidente_Empresa = values[5]
CPF_Presidente_Empresa = values[6]
RG_Presidente_Empresa = values[7]
Endereco_Presidente_Empresa = values[8]
Descricao_Sistema = values[9]
Objetivo_Sistema = values[10]
Descricao2_Sistema = values[11]
Prazo = values[12]
Valor_Servico = values[13]
Detalhes_Pagamento = values[14]
Juros = values[15]
Email_EJ_Cliente = values[16]
Empresa_Cliente = values[17]
Representante_Cliente = values[18]
CPF_Representante = values[19]
Presidente_EJ = values[20]
CPF_Pesidente_EJ = values[21]
Testemunha1 = values[22]
CPF_Testemunha1 = values[23]
Testemunha2 = values[24]
CPF_Testemunha2 = values[25]
Cnpj_EJ = values[26]
Cep_EJ = values[27]
RG_Presidente_EJ = values[28]
Endereco_Presidente_EJ = values[29]
Titular_Pagamento = values[30]
Agencia_Pagamento = values[31]
Conta_Pagamento = values[32]
CNPJ_Pagamento = values[33]
Banco_Pagamento = values[34]
data = values[35]