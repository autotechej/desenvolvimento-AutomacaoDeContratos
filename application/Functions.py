#Este arquivo armazena as funções da interface, caso queira rodar a interface só é necessário a função MenuPrincipal()

#Aqui são importados a biblioteca da interface gráfica e a biblioteca criada por mim que contem os Layouts das janelas
import PySimpleGUI as sg
import Layouts as lyt


def Formulario5():
    global FormularioWindow5, event8, values8, Prazo1, Prazo2, Prazo3, Prazo4, Prazo5
    FormularioWindow5 = sg.Window('Autotech AutoContract', lyt.FormularioLayout5)
    event8, values8 = FormularioWindow5.read()
    Prazo1 = values8[0]
    Prazo2 = values8[1]
    Prazo3 = values8[2]
    Prazo4 = values8[3]
    Prazo5 = values8[4]
    if event7 == 'Finalizar':
        FormularioWindow4.close()
    elif event7 == 'Sair' or event7 == sg.WIN_CLOSED:
        FormularioWindow4.close()

#Essa função é declarada primeiro, pois ela será solicitada por outra função pra gerar um fluxo no programa, no entanto ela seria a última a ser executada
def Formulario4():
    global FormularioWindow4, event7, values7, NumeroControle, Data, NomeRepresentante, CPFRepresentante, Testemunha1, CPFTestemunha1, Testemunha2, CPFTestemunha2, DescricaoSistema
    FormularioWindow4 = sg.Window('Autotech AutoContract', lyt.FormularioLayout4)
    event7, values7 = FormularioWindow4.read()
    NumeroControle = values7[0]
    Data = values7[1]
    NomeRepresentante = values7[2]
    CPFRepresentante = values7[3]
    Testemunha1 = values7[4]
    CPFTestemunha1 = values7[5]
    Testemunha2 = values7[6]
    CPFTestemunha2 = values7[7]
    DescricaoSistema = values7[8]
    #Essa função condicional faz o fluxo dos botões no programa
    if event7 == 'Continuar':
        Formulario5()
    elif event7 == 'Sair' or event7 == sg.WIN_CLOSED:
        FormularioWindow4.close()

#Essa função capta e armazena os dados de pagamento
def Formulario3():
    global FormularioWindow3, event6, values6, ValorFinal, DescricaoPagamento, Titular, CNPJPagamento, Banco, Agencia, Conta
    FormularioWindow3 = sg.Window("Autotech AutoContract", lyt.FormularioLayout3)
    event6, values6 = FormularioWindow3.read()
    ValorFinal = values6[0]
    DescricaoPagamento = values6[1]
    Titular = values6[2]
    CNPJPagamento = values6[3]
    Banco = values6[4]
    Agencia = values6[5]
    Conta = values6[6]
    if event6 == 'Continuar':
        FormularioWindow3.close()
        Formulario4()
    elif event6 == 'Sair' or event6 == sg.WIN_CLOSED:
        FormularioWindow3.close()


#Essa função capta e armazena os dados da EJ
def Formulario2():
    global FormularioWindow2, event5, values5, NomeEJ, CNPJEJ, CEPEJ, PresidenteEJ, CPFPresidenteEJ, RGPresidenteEJ, EnderecoPresidenteEJ, EMAILEJ
    FormularioWindow2 = sg.Window("Autotech AutoContract", lyt.FormularioLayout2)
    event5, values5 = FormularioWindow2.read()
    NomeEJ = values5[0]
    CNPJEJ = values5[1]
    CEPEJ = values5[2]
    PresidenteEJ = values5[3]
    CPFPresidenteEJ = values5[4]
    RGPresidenteEJ = values5[5]
    EnderecoPresidenteEJ = values5[6]
    EMAILEJ = values5[7]
    if event5 == 'Continuar':
        FormularioWindow2.close()
        Formulario3()
    elif event5 == 'Sair' or event5 == sg.WIN_CLOSED:
        FormularioWindow2.close()

#Essa função capta e armazena os dados do cliente
def Formulario():
    #Declara as variáveis de forma global para serem usadas em outras funções e locais
    global FormularioWindow, event4, values4, NomeCliente, NomeEmpresa, CNPJCliente, EnderecoCliente, CEPcliente, CidadeEstadoCliente, PresidenteCliente, CPFPresidenteCliente, RGPresidenteCliente, EMAILCliente
    #A função Window cria a janela com o layout especificado
    FormularioWindow = sg.Window("Autotech AutoContract", lyt.FormularioLayout1)
    #event armazena as informações passadas pelos botões em strings
    #values armazena as informações passadas pelas caixas de texto em strings de um dicionário
    #A função read lê os dados da janela(Botões e caixas de texto)
    event4, values4 = FormularioWindow.read()
    NomeCliente=values4[0]
    NomeEmpresa=values4[1]
    CNPJCliente=values4[2]
    EnderecoCliente=values4[3]
    CEPcliente=values4[4]
    CidadeEstadoCliente=values4[5]
    PresidenteCliente=values4[6]
    CPFPresidenteCliente=values4[7]
    RGPresidenteCliente=values4[8]
    EMAILCliente=values4[9]
    if event4 == 'Continuar':
        FormularioWindow.close()
        Formulario2()
        
    elif event4 =='Sair' or event4 == sg.WIN_CLOSED:
        FormularioWindow.close()

#A função que executa a janela do Menu de Contratos
def MenuPreencherContratos():
    global ContratosWindow, event2, values2, TipoContrato
    ContratosWindow = sg.Window("Autotech AutoContract", lyt.MenuContratosLayout, size=(350,200), element_justification='c')
    event2, values2 = ContratosWindow.read()
    #Caso clique em continuar o programa verifica qual o contrato desejado
    if event2 == 'Contrato de Power BI':
        ContratosWindow.close()
        Formulario()

    elif event2 == 'Contrato de Automação de Contratos':
        ContratosWindow.close()
        Formulario()

    #Caso clique sair o programa encerra
    elif event2 == 'Sair' or event2 == sg.WIN_CLOSED:
        ContratosWindow.close()

#A função que executa a janela de preferências do usuário
def MenuPreferencias():
    global PreferenciasWindow, event3, values3
    PreferenciasWindow = sg.Window("Autotech AutoContract", lyt.PreferenciasLayout)
    event3, values3 = PreferenciasWindow.read()

#A função que executa a janela do Menu Principal, dentro dela são executadas as outras
def MenuPrincipal():
    global MenuWindow, event1, values1
    MenuWindow = sg.Window("Autotech AutoContract", lyt.MenuPrincipalLayout, size=(500,300), element_justification='c')
    event1, values1 = MenuWindow.read()
    #Caso clique Preencher Novo Contrato ele abre o menu de contratos
    if event1 == 'Preencher Novo Contrato':
        MenuWindow.close()
        MenuPreencherContratos()
    #Caso clique Preferências ele abre o Menu de Preferências
    elif event1 == 'Preferências':
        MenuWindow.close()
        MenuPreferencias()
    #Caso clique Sair ele encerra o programa
    elif event1 == 'Sair' or event1 == sg.WIN_CLOSED:
        MenuWindow.close()
