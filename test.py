#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
sys.path.append("../pylinguistics/pylinguistics/")

import Pylinguistics as pl
import pandas as pd



#fapesp=pd.read_csv('fa.csv')

#print(fapesp.loc[267]['texto'])


#text = "An auxiliary verb is most generally understood as a verb that helps another verb by adding grammatical information to it."
#text = "Os benefícios concedidos pela FAPESP para bolsas de doutorado e pós-doutorado no Exterior foram alterados a partir do mês passado. Assim, o valor básico da manutenção passou de US1.400paraUS1700 mensais; o benefício para instalação, em casos de bolsas com duração de seis meses ou mais, foi elevado de US1.000paraUS 1.200 e a ajuda de custo para cobertura de despesas com saúde passou de US100paraUS 150 mensais. \n Foram alterados também os adicionais concedidos a bolsistas com dependentes. Dessa forma, quem tem um dependente recebe agora adicional de US250,contraosUS 200 em vigor até o final de junho; para dois dependentes, o adicional passou de US350paraUS 450; em caso de três dependentes, ele foi elevado de US450paraR 600 e para quatro dependentes ou mais, passou de US500paraUS 700 mensais. \n As bolsas no País permanecem com os mesmos valores vigentes desde fevereiro passado: iniciação científica, R250;aperfeiçoamento,R 500; mestrado I (fase inicial), R700;mestradoIIR750; doutoramento I, R1.050;doutoramentoII,R1.300 e pós-doutoramento R$ 1.900."
#text= "Ia bem em matemática, porém reprovou em física."
#text =  "Todos esses que aí estão atravancando meu caminho, eles passarão... Eu passarinho!"
#text = "O rato roeu a roupa do rei de Roma."
#text = "Esse processo mostra que estamos diante de um novo modelo de interação universidade-empresa para geração de tecnologia e contratações de nível qualificado. Sabemos que no mundo a maior parte das pesquisas é feita nas empresas, mas não dá para a empresa surgir do nada. Mesmo em países como os Estados Unidos é preciso começar na universidade com ideias inovadoras, diz Pereira. Para os contratados, a parceria se transformou em uma grande oportunidade de exercício profissional. Sempre quis trabalhar no ramo empresarial e em desenvolvimento sustentável, diz a bióloga Maria Grassi, 25 anos."
#text = "..."
#text = "O novo presidente do Conselho Superior da FAPESP professor Francisco Romeu Landi -que assumiu o cargo no dia 15 de agosto passado, em substituição ao professor Oscar Sala, um dos mais destacados físicos brasileiros -tem como motivo de maior orgulho, quando eventualmente recorda sua extensa folha de serviços prestados à Educação, à Ciência e à Tecnologia, ter sido diretor da Escola Politécnica da Universidade de São Paulo (USP), de 1990 a 1994. \n Mas há várias outras passagens no currículo desse engenheiro formado pela Politécnica da USP, em 1956, doutorado em Engenharia Química pela mesma instituição, em 1972 e com pós-doutoramento no Laboratório Nacional de Engenharia Civil (LNEC), em Lisboa, Portugal e no Building Research Establishment (BRE), em Garston, Inglaterra, que visivelmente lhe são muito gratificantes. \n “Gosto de ser professor nessa Universidade (a USP) há quase 40 anos. Fico feliz por ter contribuído para estruturar uma boa parte dos laboratórios da Escola Politécnica, organizar sua Pós-graduação e sua Extensão. Nesse último campo, faz bem lembrar que houve momentos em que a Poli tinha quase 300 convênios em andamento com empresas públicas e privadas”, conta ele. \n O currículo do professor Landi inclui participação na montagem de sistemas prediais do antigo Sistema Financeiro de Habitação (SFH) e na estruturação dos laboratórios de análise habitacional do Instituto de Pesquisas Tecnológicas de São Paulo (IPT), onde, aliás, foi vice-presidente do Conselho de Orientação, de 1987 a 1994. Passa pela presidência do Conselho de Instituto de Eletrotécnica e Energia (IEE), de 1990 a 1994 , pela vice-presidência do Instituto Brasileiro de Tecnologia e Qualidade na Construção (ITQC), onde seu mandato se estenderá até o próximo ano e registra ainda, entre vários outros cargos, o de gerente e diretor de empresas de engenharia e indústrias."
#file = open('english/2286.txt', 'r')
text = "Antropólogo formado pela Universidad Nacional de La Plata, Argentina, em 1971 e, até 1986; etnólogo dedicado ao estudo de grupos de índios brasileiros, Guillermo Raul Ruben fez sua travessia para a especialidade que hoje se chama Antropologia Empresarial com um prolongado trabalho de campo, entre 1987 e 1991, junto a umajoint ventureargentino-brasileira do setor metalúrgico – hoje líder no segmento de produção de cozinhas profissionais. \n “Acompanhei nesse período as dificuldades quase intransponíveis para que a empresa decolasse': diz ele. E esse processo era “muito estranho, porque aparentemante ajoint venturetinha todas as condições objetivas para dar certo: capital, tecnologia, produto e mercado. Mas o ‘take-off’ não acontecia “. O pesquisador via os sócios de duas diferentes nacionalidades envolverem-se “em discussões lancinantes, engatilhadas por desconfianças mútuas, que emergiam a despeito dos interesses convergentes e da boa vontade existente de cada lado”. \n Guillermo Ruben, mestre e doutor pela École Pratique des Hautes Études en Sciences Sociales, Universidade de Paris, observou que as diferenças culturais entre os argentinos e os brasileiros expressavam-se em um grande número de concepções diferentes sobre categorias que integram normalmente as discussões no meio empresarial: tempo, trabalho, trabalhador; trabalho feminino, lazer; sindicatos, sociedade, nação etc. O grupo que apresentava tamanha cisão era formado, pelo lado argentino, por dois empresários experientes, mas pelo lado brasileiro, à exceção de um investidor; todos eram profissionais que estavam fazendo sua primeira investida como empresários dos engenheiros e um especialistas da área de marketing. \n Segundo Guillermo Ruben, foi necessária uma inesperada “ameaça externa” para que as diferenças fossem ultrapassadas e a empresa finalmente decolasse.“Essa ameaça foi o confisco do governo Collor; que os obrigou a tomar decisões rápidas. Foi nesse momento, por exemplo, que o grupo brasileiro, que queria manter os escritórios da empresa num espaço luxuoso, separado da fábrica em Alphaville, abriu mão de tal exigência e concordou com a reunião de todas as atividades empresariais exatamente em Alphaville, como desejavam os argentinos”, conta Guillermo Ruben. \n O pesquisador; que se transferiu para o Brasil em 1977, trabalhou inicialmente na Universidade Federal da Paraíba e desde 1980 é professor na UNICAMP, explica que o temático que ora coordena foi propiciado em grande parte pela bagagem prática que acumulou com o acompanhamento do caso dessajoint-venture.A isso ele soma o aprofundamento teórico que o trabalho de orientação de dissertações no campo de nacionalidades e identidades, no mesmo período, lhe possibilitou e, finalmente, o ambiente receptivo ao tema da cultura empresarial na UMCAMP – em 1993, por exemplo, quando ele era chefe do Departamento de Antropologia Social, “a Reitoria apoiou decisivamente a realização de um workshop entre antropólogos e 50 grandes empresários sobre a importância da cultura empresarial na vida dos negócios"


#text = file.read()

#print text

#objpl = Pylinguistics('pt',text.decode('utf-8'))











objpl = pl.text(text.decode('utf-8'))

objpl.setLanguage("pt");


print('Features: %s' %objpl.getFeatures())
#print('POS_TAGS: %s' %objpl.tokens)
print('POS_TAGS: %s' %objpl.postag)
#print(len(objpl.postag))
