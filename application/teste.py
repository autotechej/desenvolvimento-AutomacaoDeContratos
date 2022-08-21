#-*- coding: utf-8 -*-
#encoding: utf-8
import Functions as fct
from application.Functions import PresidenteCliente, PresidenteEJ
beta = 'Isso e um beta'
h1 = '{size: 54px; text-align: center;\n\tfont-family: Georgia, \'Times New Roman\', Times, serif;}'
h2 = '{size: 40px; text-align: center;\n\tfont-family: Georgia, \'Times New Roman\', Times, serif;}'
body ='{text-align: justify;\n\tmax-width: 650px;\n\tfont-family: Georgia, \'Times New Roman\', Times, serif;\n\tfont-size: 16px;\n\tpadding: 0;\n\tmargin: 0 auto !important;}'
h4 = '{size: 48px; text-align: center;\n\tfont-family: Georgia, \'Times New Roman\', Times, serif;}'

def escrever_contrato():
    Contratohtml = open('.\Contrato.html', 'w', encoding = 'utf-8')
    Contratohtml.write(f'<!DOCTYPE>\n\t<html>\n\t<meta charset="utf-8">\n\t<meta name="viewport" content="width=297x420" initialscale="1">\n\t<title>Template Autotech</title>\n\t<style>\n\th1 {h1}\n\th2 {h2}\n\th4 {h4}\n\tbody {body}\n\t</style>\n\t<head>\n\t<h1>{fct.NomeEJ}</h1>\n\t<center>\n\t<img src="./LOGO - QUADRADO (5).png" width="200" height="200"</center>\n\t<h2>CONTRATO DE PRESTAÇÃO DE SERVIÇOS</h2>\n\t<h3>CONTROLE: {fct.NumeroControle}</h3>\n\t</head>\n\t<body>\n\t<p><strong>Celebrado consoante a melhor forma de Direito e consoante todas as disposições legais pertinentes à matéria, firmam entre si o presente contrato de prestação de serviços, por justo e acertado, as partes abaixo qualificadas:</strong></p>\n\t<br>\n\t<p><strong>CONTRATANTE: {fct.NomeEmpresa}</strong> pessoa jurídica, de direito privado, denominado <strong>CONTRATANTE</strong>, devidamente constituída como sociedade limitada, inscrita no CNPJ sob o n° {fct.CNPJCliente}, com endereço {fct.EnderecoCliente} , CEP n° {fct.CEPcliente}, {fct.CidadeEstadoCliente}, neste ato representada por seu Presidente <strong>{fct.PresidenteCliente}</strong>, inscrito no CPF sob o n° {fct.CPFPresidenteCliente} e no RG Nº {fct.RGPresidenteCliente}, residente e domiciliado em {fct.EnderecoCliente}.</p>\n\t<p><strong>CONTRATADA: {fct.NomeEJ}</strong>, pessoa jurídica de direito privado, denominada <strong>CONTRATADA</strong>, devidamente constituída como associação civil sem fins lucrativos, inscrita no CNPJ sob o n° {fct.CNPJEJ}, com endereço à , CEP {fct.CEPEJ}, Fortaleza, Ceará, neste ato representada por seu diretor presidente, <strong>{fct.PresidenteEJ}</strong>, inscrito no CPF n° {fct.CPFPresidenteEJ}, portador da identidade nº {fct.RGPresidenteEJ}, residente e domiciliado em {fct.EnderecoPresidenteEJ}.</p>\n<p>Ambas as partes, de comum acordo, resolvem firmar o presente <strong>CONTRATO DE PRESTAÇÃO DE SERVIÇOS</strong>, a ser regulado pelas cláusulas e condições abaixo lançadas, a que reciprocamente se obrigam:</p>\n<h4>I. DO OBJETO CONTRATUAL</h4>\n<p><strong>CLÁUSULA 1ª.</strong> O presente contrato tem por objeto a prestação do serviço de Consultoria, projeto e implementação de sistema de controle personalizado pela <strong>CONTRATADA</strong> em favor da <strong>CONTRATANTE</strong>, sendo esse discriminado na cláusula 2ª deste contrato.</p>\n<h4>II. DOS SERVIÇOS</h4>\n<p>CLÁUSULA 2ª. É atribuição da <strong>CONTRATADA</strong> atuar em favor da <strong>CONTRATANTE</strong> no exercício do serviço compreendido pelas partes abaixo delineadas:</p>\n<p><strong>I.</strong>Formulação de orçamento e planejamento do projeto;<br><strong>II.</strong>Obtenção dos componentes necessários para a fabricação do projeto;<br><strong>III.</strong>Moldagem e estruturação do projeto;<br><strong>IV.</strong>Execução e finalização física do projeto.</p><p><strong>Parágrafo Único. </strong>Considera-se parte integrante e indissociável deste contrato a proposta comercial assinada por ambas as partes.</p><p><strong>§1°.</strong> O sistema a ser desenvolvido consiste em: {fct.DescricaoSistema}</p><h4>III. DOS PRAZOS</h4><p><strong>CLÁUSULA 3ª.</strong> Obriga-se a <strong>CONTRATADA</strong> a atuar diligentemente na execução do objeto contratual, sendo de {fct.Prazo1} dias úteis o prazo para a Elaboração inicial e planejamento do projeto, a contar da data de assinatura do presente contrato, {fct.Prazo2} dias úteis para a compra e obtenção dos materiais necessários para o projeto, {fct.Prazo3} dias úteis para desenvolvimento prático do projeto, a contar do primeiro dia útil transcorrido após o período de compra e obtenção dos materiais necessários para o projeto, {fct.Prazo4} dias úteis para instalação do projeto no local solicitado pelo contratante, totalizando {fct.Prazo5} dias úteis de prazo impreterível para entrega do produto final a <strong>CONTRATANTE</strong>, obrigando-se a <strong>CONTRATANTE</strong> a propiciar condições de desenvolvimento do trabalho, bem como fornecendo à <strong>CONTRATADA</strong> todas as informações necessárias para realização do serviço, sendo essas condições impreteríveis para a perfeita consecução do objeto contratual.</p>\n\t<p><strong>Parágrafo único.</strong> O prazo de execução do serviço pela CONTRATADA ficará suspenso até a entrega pela <strong>CONTRATANTE</strong>das exigíveis condições de desenvolvimento do trabalho, especialmente no que tange à entrega de informações solicitadas ou na efetivação de reunião requerida pela <strong>CONTRATADA</strong>.</p>\n\t<h4>IV. DAS OBRIGAÇÕES DA CONTRATANTE</h4>\n\t<p><strong>CLÁUSULA 4ª.</strong>Obriga-se a<strong>CONTRATANTE</strong>a: </p>\n\t<p><strong>I. </strong>Colocar à disposição da <strong>CONTRATADA</strong> todas as informações, os documentos e os recursos materiais e humanos que sejam necessários à execução do objeto pactuado, devendo especificar os detalhes necessários à perfeita consecução dele, e como ele deve ser entregue;</p>\n\t<p><strong>II. </strong>Efetuar, dentro do período acordado e na forma ajustada, os pagamentos estipulados neste contrato pelo serviço prestado;</p>\n\t<p><strong>III. </strong>Manter atualizados os meios de comunicação e responder, em tempo hábil, os contatos solicitados pela CONTRATADA, visando a soluções de eventuais dúvidas referentes ao serviço, de forma a responsabilizar-se por atrasos no projeto decorrentes de falhas que cause na comunicação;</p>\n\t<p>Promover o acompanhamento dos serviços, comunicando as ocorrências de quaisquer fatos que, a seu critério, exijam medidas corretivas por parte da <strong>CONTRATADA</strong>;Atuar em harmonia com a CONTRATADA, de maneira a garantir os resultados condizentes com a proposta comercial;</p>\n\t<p><strong>IV. </strong>Se necessário, pagar taxas e despesas referentes à execução do serviço em órgãos públicos e privados, os quais serão avisados previamente pela CONTRATADA durante a execução do serviço;</p>\n\t<p><strong>V. </strong>Dar um aviso prévio de, no mínimo, 24 horas antes da data marcada, caso necessite cancelar uma reunião ou visita da CONTRATADA.</p>\n\t<p><strong>a. </strong>Quando do descumprimento deste inciso, torna-se a CONTRATANTE passível de multa estritamente referente aos custos gerados pelo deslocamento e hora de trabalho desperdiçados da CONTRATADA.</p>\n\t<p><strong>b. </strong>Em circunstância de caso fortuito ou força maior, é exigível comprovação da CONTRATANTE em até 24h após o horário da reunião, pela qual se anula, quandoreconhecido pela CONTRATADA o caráter de completa imprevisibilidade, a incidência de multa.</p>\n\t<h4>V. DAS OBRIGAÇÕES DA CONTRATADA</h4>\n\t<p><strong>CLÁUSULA 5ª.</strong> Obriga-se a <strong>CONTRATADA</strong> a:</p>\n\t<p><strong>I. </strong>Desenvolver todos os atos necessários à consecução do objeto contratual de acordo com os parâmetros ajustados, cumprindo fielmente todas as suas obrigações decorrentes deste contrato;</p>\n\t<p><strong>II. </strong>Entregar o serviço no prazo estipulado, adaptando-o no decorrer quando tratar-se de atraso no repasse de informações ou demais fatores que estejam fora do seu âmbito de controle;</p>\n\t<p><strong>III. </strong>Desenvolver todos os atos necessários à consecução do objeto da forma e do modo ajustado, cumprindo fielmente todas as suas obrigações decorrentes deste contrato;</p>\n\t<p><strong>IV. </strong>Manter contato e enviar informações periódicas à <strong>CONTRATANTE</strong>sobre o andamento do serviço, bem como sobre custas geradas, previamente informadas, que precisem ser pagas pela <strong>CONTRATANTE</strong>;</p>\n\t<p><strong>V. </strong>Entrar em contato com a CONTRATANTE em um prazo de até 2(dois) dias úteis após a assinatura do presente instrumento contratual para colher as informações necessárias para a execução do projeto;</p>\n\t<p><strong>VI. </strong>Emitir o comprovante de pagamento em nome da <strong>CONTRATANTE</strong>.</p>\n\t<p><strong>VII. </strong>Garantir o funcionamento do sistema instalado por <strong>TRÊS MESES</strong> a partir da assinatura deste contrato, realizando eventuais visitas de reparo sem custo adicional à <strong>CONTRATANTE</strong>. A resolução de problemas não cobertos por este contrato está passível de cobrança.</p>\n\t<h4>VI. DA SUBCONTRATAÇÃO</h4>\n\t<p><strong>CLÁUSULA 6ª.</strong> Desde que previamente comunicada à <strong>CONTRATANTE</strong> e por esta anuída em termo assinado, poderá a <strong>CONTRATADA</strong> subcontratar, cedendo ou transferindo parte de seu objeto a terceiros, sendo de total responsabilidade da <strong>CONTRATADA</strong> todo o ônus referente a tal subcontratação e ficando a <strong>CONTRATANTE</strong> totalmente isenta de obrigações em relação a esses e a outros colaboradores.</p>\n\t<h4>VII. DO USO DO NOME E DA IMAGEM E DA CONFIDENCIALIDADE</h4>\n\t<p><strong>CLÁUSULA 7ª</strong>. Ao fazer uso da imagem ou do nome da <strong>CONTRATANTE</strong>, a <strong>CONTRATADA</strong> deverá zelar pela imagem organizacional, respeitando a identidade visual fornecida.</p>\n\t<p><strong>Parágrafo único.</strong> A <strong>CONTRATANTE</strong>, em acordo com a <strong>CONTRATADA</strong>, está autorizada a fazer uso da imagem e nome desta para fins exclusivos de divulgação dos serviços da <strong>CONTRATADA</strong>.</p>\n\t<p><strong>CLÁUSULA 8ª</strong>. A <strong>CONTRATADA</strong> manterá as informações confidenciais recebidas da <strong>CONTRATANTE</strong> sob o mais estrito sigilo. Por outro lado, a <strong>CONTRATANTE</strong> manterá sigilo sobre quaisquer pareceres, documentos ou opiniões, por qualquer meio, relacionados às medidas objeto deste contrato, fornecidos pela CONTRATADA, tratando-os como “informações confidenciais”, não sendo permitida sua utilização, circulação, divulgação ou publicação sem o prévio e expresso consentimento da <strong>CONTRATADA</strong>.</p>\n\t<p><strong>CLÁUSULA 9ª</strong>. Reconhece-se, desde logo, que as partes não terão nenhum direito, título ou interesse, por licença ou de outra forma, para usar os documentos ou informações obtidas, obrigando-se a não transmiti-los e nem revelá-los a terceiros, bem como a não distribuir, usar, divulgar ou dispor deles para outra finalidade que não aquela estritamente determinada no presente instrumento contratual.</p>\n\t<p><strong>CLÁUSULA 10ª</strong>. As obrigações referentes à confidencialidade persistem em caráter residual, mesmo quando o contrato não estiver mais vigente.</p>\n\t<h4>VIII. DO VALOR E DAS CONDIÇÕES DE PAGAMENTO</h4>\n\t<p><strong>CLÁUSULA 11ª</strong>. Pelos serviços contratados mediante este documento, a <strong>CONTRATANTE</strong> pagará à <strong>CONTRATADA</strong> o valor total de R$ {fct.ValorFinal}, constituído por {fct.DescricaoPagamento}.</p>\n\t<p><strong>§1°</strong>. O pagamento será realizado pela <strong>CONTRATANTE</strong> mediante depósito ou transferência bancária na conta corrente detalhada a seguir:</p>\n\t<p>TITULAR: {fct.Titular}</p>\n\t<p>CNPJ: {fct.CNPJPagamento}</p>\n\t<p>BANCO: {fct.Banco}</p>\n\t<p>AGÊNCIA: {fct.Agencia}</p>\n\t<p>CONTA: {fct.Conta}</p>\n\t<p></p><strong>§2°</strong>. O investimento previsto neste instrumento deverá ser pago até a data de seu vencimento, sob pena de multa de 10% (dez por cento) do saldo então devido, acrescido de correção monetária equivalente à variação positiva do IGP-M divulgado pela FGV ou, no caso de sua extinção, de outro índice que venha a substituí-lo, mais juros equivalentes a 1% (um por cento) ao mês.</p>\n\t<h4>IX. DA VIGÊNCIA</h4>\n\t<p><strong>CLÁUSULA 12ª</strong>. O presente contrato terá a vigência de seus efeitos iniciada a partir de sua assinatura pelas partes e pelas testemunhas e finalizada quando o serviço contratado for entregue à <strong>CONTRATANTE</strong> e o pagamento for totalmente realizado pela <strong>CONTRATANTE</strong>.</p>\n\t<h4>X. DAS PENALIDADES, MULTAS E EXTINÇÃO DO CONTRATO</h4>\n\t<p><strong>CLÁUSULA 13ª</strong>. Caso o pagamento não seja efetuado até a data prevista, incidirá juros de 1% (um por cento) sobre o(s) valor(es) da(s) prestação(ões) vencida(s), para cada dia de atraso, acrescido de multa de 10% (dez por cento) do saldo então devido e correção monetária equivalente à variação positiva do IGP-M divulgado pela FGV ou, no caso de sua extinção, de outro índice que venha a substituí-lo.</p>\n\t<p><strong>§1º</strong>. Em caso de atraso superior a 01 (um) mês no pagamento de qualquer parcela, será direito da <strong>CONTRATADA</strong> exigir o vencimento antecipado das parcelas restantes, sob penalidade de interrupção dos serviços prestados declarados neste contrato.</p>\n\t<p><strong>§2º</strong>. Deverá ser notificada a intenção de resilir à parte contrária com antecedência mínima de 1/3 (um terço) do prazo previsto para a execução do serviço, sob pena de multa de 10% (dez por cento) do valor total do contrato.</p>\n\t<p><strong>§3º</strong>. A rescisão contratual por descumprimento total ou parcial de qualquer das obrigações contidas no presente instrumento gera multa compensatória de 20% (vinte por cento) do valor total do contrato, a título de indenização, a ser paga pela parte infratora à parte contrária.</p>\n\t<p><strong>§4º</strong>. A eventual aceitação por uma das partes da inexecução pela outra de quaisquer cláusulas deste contrato, a qualquer tempo, deverá ser interpretada como mera liberalidade, não implicando, portanto, em novação ou na desistência de exigir o cumprimento das disposições aqui contidas ou do direito de pleitear, futuramente, a execução total de cada uma das obrigações.</p>\n\t<p><strong>CLÁUSULA 14ª</strong>. É assegurado às partes resilir o presente contrato antes do término do prazo. Caso a CONTRATANTE decida pela resilição , deverá ser pago à <strong>CONTRATADA</strong> 30% (trinta por cento) do valor total do serviço, não havendo devolução de qualquer quantia paga a qualquer título por parte da <strong>CONTRATADA</strong>. Caso a CONTRATADA solicite a resilição unilateral do contrato, é obrigada a devolver 50% (cinquenta por cento) dos valores já pagos até o devido momento pela <strong>CONTRATANTE</strong>.</p>\n\t<p><strong>§1º</strong>. Deverá ser notificada a intenção de resilir à parte contrária com antecedência mínima de ⅓ (um terço) do prazo previsto para a execução do serviço, sob pena de multa de 10% (dez por cento) do valor total do contrato.</p>\n\t<p><strong>§2º</strong>. O resultado do serviço será entregue à <strong>CONTRATANTE</strong> no formato em que estiver, no momento da resilição.</p>\n\t<p><strong>CLÁUSULA 15ª</strong>. Poderá o presente contrato ser considerado rescindido de pleno direito, independentemente de qualquer notificação ou interpelação, na hipótese de descumprimento de quaisquer de seus termos e condições, por ambas as partes ou por uma delas.</p>\n\t<p><strong>CLÁUSULA 16ª</strong>. A extinção do presente contrato ocorrerá pelas seguintes hipóteses:</p>\n\t<p><strong>I. </strong>Perfectibilização do objeto contratual, ou seja, a conclusão do serviço, por parte da <strong>CONTRATADA</strong>, e a efetuação do pagamento integral, por parte da CONTRATANTE;</p>\n\t<p><strong>II. </strong>Resilição do instrumento contratual;</p>\n\t<p><strong>III. </strong>Rescisão do instrumento contratual.</p>\n\t<h4>XI. DAS DISPOSIÇÕES GERAIS</h4>\n\t<p><strong>CLÁUSULA 17ª</strong>. Os endereços eletrônicos de comunicação oficial entre as partes serão: {fct.EMAILEJ} e {fct.EMAILCliente}.</p>\n\t<p><strong>CLÁUSULA 18ª</strong>. O presente contrato não estabelece qualquer sociedade, associação, solidariedade, subsidiariedade ou sucessão entre as partes e não gera vínculo empregatício entre a <strong>CONTRATANTE</strong> e a <strong>CONTRATADA</strong>, ou entre seus prepostos e colaboradores, de qualquer natureza, em qualquer ocasião, a qualquer época.</p>\n\t<p><strong>CLÁUSULA 19ª</strong>. Toda e qualquer alteração contratual deverá ser feita através de Termo Aditivo, devidamente assinado pelas partes envolvidas, o qual será parte integrante e inseparável deste instrumento, sob pena de nulidade da alteração.</p>\n\t<p><strong>CLÁUSULA 20ª</strong>. As partes contratantes resguardam-se na exigência dos direitos e obrigações que lhe reservam o presente instrumento, ressalvados aqueles que venham a ferir a ética ou os princípios morais.</p>\n\t<p><strong>CLÁUSULA 21ª</strong>. Quaisquer mudanças não comunicadas à outra parte que interfiram no cumprimento deste contrato deverão ser compensadas pela parte responsável.</p>\n\t<p><strong>CLÁUSULA 22ª</strong>. A eventual declaração de invalidade, ineficácia de qualquer disposição deste instrumento não terá efeito sobre a validade e a eficácia das demais obrigações aqui expostas, desde que não inviabilize o cumprimento do objeto do presente contrato.</p>\n\t<p><strong>CLÁUSULA 23ª</strong>. Este instrumento de contrato serve como título executivo extrajudicial, nos termos do inciso III, art. 784, do Código de Processo Civil de 2015.</p>\n\t<h4>XII. DO FORO</h4>\n\t<p><strong>CLÁUSULA 24ª</strong>. As partes elegem o Foro da Comarca de Fortaleza, capital do estado do Ceará, para dirimir quaisquer controvérsias oriundas do presente documento.</p>\n\t<p>Por estarem as partes, <strong>CONTRATANTE</strong> e <strong>CONTRATADA</strong>, de pleno acordo com o disposto neste instrumento, assinam-no em 02 (duas) vias de igual teor, na presença de 02 (duas) testemunhas.</p>\n\t<div align="right">Fortaleza, {fct.Data}</div>\n\t<br><br><center>\n\t<p>--------------------------</p>\n\t<p>{fct.NomeEmpresa}</p><p>{fct.NomeRepresentante}</p>\n\t<p>CPF: {fct.CPFRepresentante}</p>\n\t<br><p>--------------------------</p>\n\t<p>AUTOTECH-Empresa Júnior de Automação</p>\n\t<p>fct.{PresidenteEJ}</p>\n\t<p>CPF: {fct.CPFPresidenteCliente}</p>\n\t<p>--------------------------</p>\n\t<p>{fct.Testemunha1}</p>\n\t<p>CPF: {fct.CPFTestemunha1}</p>\n\t<p>{fct.Testemunha2}</p>\n\t<p>CPF: {fct.CPFTestemunha2}</p></center>')
    Contratohtml.close()