########################################################################################################################
########################################################################################################################
# DATA: 12/07/2020
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
# PROFESSOR: VINÍCIUS QUINTÃO CARNEIRO
# E-MAIL: vinicius.carneiro@ufla.br
# GITHUB: vqcarneiro
########################################################################################################################
# DISCENTE: REBERTH RENATO DA SILVA
# E-MAIL: reberth.silva@estudante.ufla.br
# GITHUB: reberthrenato - https://github.com/reberthrenato
########################################################################################################################
#     REO 01 - LISTA DE EXERCÍCIOS
########################################################################################################################
# EXERCÍCIO 01:
print('-'*100)
print('a) Declare os valores 43.5,150.30,17,28,35,79,20,99.07,15 como um array numpy.')

# Primeiro passo: importar a biblioteca nunmpy:
import numpy as np # importar a biblioteca numpy com a abreviação np
print('-'*100)

# Segundo passo: declarar a lista e confirmar o tipo de estrutura:

Lista = [43.5,150.30,17,28,35,79,20,99.07,15] # Fazer a lista
print('LISTA: ', str(Lista)) # Colocamos o vetor lista como uma string para poder juntar com o texto.
print('TIPO: ') # Apenas um comando para aparecer o tipo acima na tela do print.
print(type(Lista)) # função type mostra o tipo de arquivo que estamos trabalhando.

# Terceiro passo: Transformar a lista em um array numpy:
vetor = np.array(Lista) # tranforma a lista em um vetor array.
print('Vetor: ' + str(vetor)) # para imprimir o vetor temos que transformar ele numa string.
print('TIPO: ')
print(type(vetor)) # tipo de vetor.

print('-'*100)
print('b) Obtenha as informações de dimensão, média, máximo, mínimo e variância deste vetor.')
print('-'*100)

# Dimensão de um vetor:
print('A dimensão do vetor é: ', len(vetor))
# A média de um vetor:
print('A média do vetor é: ', np.mean(vetor))
# O máximo de um vetor:
print('O máximo do vetor é: ', np.max(vetor)) # outra opção seria com a função max.
# O mínimo de um vetor:
print('O mínimo do vetor é: ', np.min(vetor)) # outra opção seria com a função min.
# Variância de um vetor:
print('A variância do vetor é: ', np.var(vetor))

print('-'*120)
print('c) Obtenha um novo vetor em que cada elemento é dado pelo quadrado da diferença entre cada elemento do vetor declarado')
print('na letra a e o valor da média deste.')
print('-'*120)

media_vetor = np.mean(vetor)
for vetor2 in vetor:
    vetor2 = np.array((vetor2-media_vetor)**2)
    print(vetor2)

print('-'*100)
print('d) Obtenha um novo vetor que contenha todos os valores superiores a 30.')
print('-'*100)

bool_maior_30 = vetor>30 # condição: quais os valores são maiores que 30
print('Vetor original: ' + str(vetor)) # variável booleana estrutura de condição
print('Vetor booleano maior que 30: ' + str(bool_maior_30))
vetor_maior_30 = vetor[bool_maior_30] # >30 retorna esses valores, acessa valores dentro dessa condição.
print('Vetor com valores maiores que 30: ' + str(vetor_maior_30))

print('-'*100)
print('e) Identifique quais as posições do vetor original possuem valores superiores a 30')
print('-'*100)

pos_maior_30 = np.where(vetor>30) # vai retornar as posições dos elementes do vetor que são maiores do que 30.
print('Posições do vetor original com valores superiores à 30: ', str(pos_maior_30[0])) # coloca 0 para pegar o novo vetor gerado.

print('-'*100)
print('f) Apresente um vetor que contenha os valores da primeira, quinta e última posição.')
print('-'*100)

# PRIMEIRA POSIÇÃO:
print('Vetor: ' + str(vetor)) # para imprimir o vetor temos que transformar ele numa string.
primeiro_pos = vetor[0] # com esse comando conseguimos acessar posições específicas dentro do vetor.
print('Valor da PRIMEIRA POSIÇÃO: ' + str(primeiro_pos))

# QUINTA POSIÇÃO:
quinto_pos = vetor[4] # para acessar qualquer valor dentro do intervalo, basta subtrair 1 porque o 0 é contabilizado.
print('Valor da QUINTA POSIÇÃO: ', str(quinto_pos))

# ÚLTIMA POSIÇÃO:
ultima_pos = vetor[-1] # TODAS AS VEZES que queremos o último valor devemos colocar -1
print('Valor da ÚLTIMA POSIÇÃO: ', str(ultima_pos))

print('-'*100)
print('g) Crie uma estrutura de repetição usando o for para apresentar cada valor e a sua respectiva posição durante as iterações')
print('-'*100)

print('Vetor: ' + str(vetor)) # para imprimir o vetor
print('Número de elementos do vetor: ' + str(len(vetor)))
it = 0
for n in range(0, len(vetor), 1): # A primeira posição é 0, o comprimento com len e os passos de um em um.
    it = it + 1
    print('Iteração: ' + str(it))
    print('Na posição ' + str(n) + ' há o elemento: ' + str(vetor[int(n)])) # tem que transformar o i em inteiro, porque é floot.
    #time.sleep(1.0) # só para ver o looping

print('-'*100)
print('h) Crie uma estrutura de repetição usando o for para fazer a soma dos quadrados de cada valor do vetor.')
print('-'*100)

print('Vetor: ' + str(vetor))
SQ = 0
it = 0
for i in vetor:
    it = it + 1
    SQ = SQ + i**2
    print('Iteração: {} Elemento do vetor: {} Somatário: {} '. format(it, i, SQ))

print('-'*100)
print('i) Crie uma estrutura de repetição usando o while para apresentar todos os valores do vetor')
print('-'*100)

cont = -1
print(' Nesse caso, ocorre a impressão de números até que apareça o 7. ')
while cont != 7: # contador é o número que queremos que termina a contagem.
    cont += 1
    print('Contador = ', cont) # vai ser executado repetidamente dentro do código até encontrar o valor 7.

print('-'*100)
print('j) Crie um sequência de valores com mesmo tamanho do vetor original e que inicie em 1 e o passo seja também 1.')
print('-'*100)

print('Sequência: {}'.format(list(range(1, len(vetor), 1))))

print('-'*100)
print('h) Concatene o vetor da letra a com o vetor da letra j.')
print('-'*100)

vetor_02 = list(range(1, len(vetor), 1))
vetor_concatenado = np.concatenate((vetor, vetor_02), axis=0)
print(vetor_concatenado)

########################################################################################################################
########################################################################################################################
########################################################################################################################

# EXERCÍCIO 02:
print('-'*100)
print('a) Declare a matriz abaixo com a biblioteca numpy.')
#      1 3 22
#      2 8 18
#      3 4 22
#      4 1 23
#      5 2 52
#      6 2 18
#      7 2 25
print('-'*100)
matriz = np.array([[1, 3, 22], [2, 8, 18], [3, 4, 22], [4, 1, 23], [5, 2, 52], [6, 2, 18], [7, 2, 25]])
print(' MATRIZ:')
print(matriz)

print('-'*100)
print('b) Obtenha o número de linhas e de colunas desta matriz')
print('-'*100)
# Obtendo a dimensão de uma matriz:
nl,nc = np.shape(matriz) # dimensão das matrizes.
print('Número de linhas: ' + str(nl))
print('Número de colunas: ' + str(nc))

print('-'*100)
print('c) Obtenha as médias das colunas 2 e 3.')
print('-'*100)

sub_matriz_col2 = matriz[:,1]
media_col2 = np.average(sub_matriz_col2)
print('Coluna 2: {} Média: {}'.format(sub_matriz_col2,media_col2))

sub_matriz_col3 = matriz[:,2]
media_col3 = np.average(sub_matriz_col3)
print('Coluna 3: {} Média: {}'.format(sub_matriz_col3,media_col3))

print('-'*100)
print('d) Obtenha as médias das linhas considerando somente as colunas 2 e 3')
print('-'*100)

sub_matriz_lin1 = matriz[[0],[1,2]]
media_matriz_lin1 = np.average(sub_matriz_lin1)
print('A média da linha 1 considerando coluna 2 e 3: {}'.format(media_matriz_lin1))

submatriz_lin2 = matriz[1,[1,2]]
media_matriz_lin2 = np.average(submatriz_lin2)
print('A média da linha 2 considerando coluna 2 e 3: {}'.format(media_matriz_lin2))

submatriz_lin3 = matriz[2,[1,2]]
media_matriz_lin3 = np.average(submatriz_lin3)
print('A média da linha 3 considerando coluna 2 e 3: {}'.format(media_matriz_lin3))

submatriz_lin4 = matriz[3,[1,2]]
media_matriz_lin4 = np.average(submatriz_lin4)
print('A média da linha 4 considerando coluna 2 e 3: {}'.format(media_matriz_lin4))

submatriz_lin5 = matriz[4,[1,2]]
media_matriz_lin5 = np.average(submatriz_lin5)
print('A média da linha 5 considerando coluna 2 e 3: {}'.format(media_matriz_lin5))

submatriz_lin6 = matriz[5,[1,2]]
media_matriz_lin6 = np.average(submatriz_lin6)
print('A média da linha 6 considerando coluna 2 e 3: {}'.format(media_matriz_lin6))

submatriz_lin7 = matriz[6,[1,2]]
media_matriz_lin7 = np.average(submatriz_lin7)
print('A média da linha 7 considerando coluna 2 e 3: {}'.format(media_matriz_lin7))

print('-'*100)
print('e) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença e a terceira peso')
print('de 100 grãos. Obtenha os genótipos que possuem nota de severidade inferior a 5.')
print('-'*100)

sub_matriz_col2 = matriz[:,1]
valores_menores_5 = np.where(sub_matriz_col2<5)
print('Posições dos genóticos com severidade menor que 5: {}'.format(valores_menores_5[0]))
x_valores_menores_5 = sub_matriz_col2<5
sub_matriz_col1 = matriz[:,0]
gen_valores_menores_5 = sub_matriz_col1[x_valores_menores_5]
print('Os genótipos com notas de severidade menor que 5 são: {}'.format(gen_valores_menores_5))

print('-'*100)
print('f) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença e a terceira peso de 100 grãos. ')
print('Obtenha os genótipos que possuem nota de peso de 100 grãos superior ou igual a 22.')
print('-'*100)

sub_matriz_col3 = matriz[:, 2]
valores_maiores_22 = np.where(sub_matriz_col3>=22)
print('As posições na matriz dos genótipos que possuem peso de 100 grãos superior ou igual a 22: {}'.format(valores_maiores_22[0]))
x_valores_maiores_22 = sub_matriz_col3>=22
sub_matriz_col1 = matriz[:, 0]
genotipos_peso_maior22 = sub_matriz_col1[x_valores_maiores_22]
print('Os genótipos com peso de 100 grãos superior ou igual a 22: {}'.format(genotipos_peso_maior22))

print('-'*100)
print('g) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença e a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de severidade igual ou inferior a 3 e peso de 100grãos igual ou superior a 22.')
print('-'*100)

print('Posições nota inferior ou igual a 4 são, {}, Posições peso de 100 grãos superior ou igual a 22: {}'.format(valores_menores_5[0], valores_maiores_22[0]))
gen = sub_matriz_col1[x_valores_menores_5 & x_valores_maiores_22]
print('Genótipos peso de 100 grãos superior ou igual a 22 e nota de severidade de doença inferior ou igual a 3: {}'.format(gen))


print('-'*100)
print('h) Crie uma estrutura de repetição com uso do for (loop) para apresentar na tela cada uma das posições da matriz e o seu respectivo valor. Utilize um iterador para mostrar ao usuário quantas vezes está sendo repetido. ')
print('Apresente a seguinte mensagem a cada iteração "Na linha X e na coluna Y ocorre o valor: Z". Nesta estrutura crie uma lista que armazene os genótipos com peso de 100 grãos igual ou superior a 25')
print('-'*100)

contador = 0
genotipos = []
for i in np.arange(0,nl,1):
    if matriz[i, 2] >= 25:
        genotipos.append(matriz[i, 0])
    for j in np.arange(0,nc,1):
        contador = contador + 1
        print('Iteração: '+ str(contador))
        #como em numpy a linha e coluna se inicia por 0, somei +1 ao indexador pra facilitar a visualização
        print('Na linha ' + str(i+1) + ' e na coluna ' + str(j+1) + ' ocorre o valor: ' + str(matriz[int(i),int(j)]))
print ("Lista dos genótipos com peso de 100 grãos igual ou superior a 25")
print (genotipos)



print('-'*100)
# Exercício 3
print('-'*100)
print('a) Crie uma função em um arquivo externo (outro arquivo .py) para calcular a média e a variância amostral um vetor qualquer, baseada em um loop (for).')
print('-'*100)

from Questao3 import media, var_amostral # como foi criado no mesmo repositório basta colocar o from. Se fosse de outro deveria utilizar o endereço do arquivo.
print('-'*100)

print('-'*100)
print('b) Simule três arrays com a biblioteca numpy de 10, 100, e 1000 valores e com distribuição normal com média 100 e variância 2500. Pesquise na documentação do numpy por funções de simulação.')
print('-'*100)

vetor10 = np.random.normal(100,50,10)
vetor100 = np.random.normal(100,50,100)
vetor1000 = np.random.normal(100,50,1000)


print('Vetor 10:')
print(vetor10)
print('Vetor 100: ')
print(vetor100)
print('Vetor 1000: ')
print(vetor1000)


print('-'*100)
print('c) Utilize a função criada na letra a para obter as médias e variâncias dos vetores simulados na letra b.')
print('-'*100)

print('Vetor 10: média {}, variância {}'.format(media(vetor10), var_amostral(vetor10)))
print('Vetor 100: média {}, variância {}'.format(media(vetor100), var_amostral(vetor100)))
print('Vetor 1000: média {}, variância {}'.format(media(vetor1000), var_amostral(vetor1000)))

print('-'*100)
print('d) Crie histogramas com a biblioteca matplotlib dos vetores simulados com valores de 10, 100, 1000 e 100000')
print('-'*100)

import matplotlib.pyplot as plt

plt.style.use('dark_background')
count, bins, ignored = plt.hist(vetor10, 30, density=True)
plt.plot(bins, 1/(50 * np.sqrt(2 * np.pi)) *
np.exp( - (bins - 100)**2 / (2 * 50**2) ),linewidth=5, color='b')
plt.title('Vetor 10')
plt.show()

count, bins, ignored = plt.hist(vetor100, 30, density=True)
plt.plot(bins, 1/(50 * np.sqrt(2 * np.pi)) *
np.exp( - (bins - 100)**2 / (2 * 50**2) ),linewidth=5, color='y')
plt.title('Vetor 100')
plt.show()

count, bins, ignored = plt.hist(vetor1000, 30, density=True)
plt.plot(bins, 1/(50 * np.sqrt(2 * np.pi)) *
np.exp( - (bins - 100)**2 / (2 * 50**2) ),linewidth=5, color='g')
plt.title('Vetor 1000')
plt.show()

vetor100000 = np.random.normal(100,50,100000)
count, bins, ignored = plt.hist(vetor100000, 30, density=True)
plt.plot(bins, 1/(50 * np.sqrt(2 * np.pi)) *
np.exp( - (bins - 100)**2 / (2 * 50**2) ),linewidth=5, color='r')
plt.title('Vetor 100000')
plt.show()
print('Gráficos dos vetores 10, 100, 1000 e 100000 foram gerados, respectivamente')


## Questão 4 ##

print('-'*100)
print('a- O arquivo dados.txt contém a avaliação de genótipos (primeira coluna) em repetições (segunda coluna) quanto a '
      'quatro variáveis (terceira coluna em diante). Portanto, carregue o arquivo dados.txt com a biblioteca numpy, '
      'apresente os dados e obtenha as informações de dimensão desta matriz. ')
print('-'*100)

# Primeiro passo: colocar o arquivo dados (1).txt na pasta do pycharm.
print('-'*100)
dados = np.loadtxt('dados (1).txt') # Posteriormente, chamar carregamos os dados com a função p.loadtxt do numpy.
# E criamos uma variável para receber esses dados.
print('Avaliação dos genótipos: ')
print('-'*100)

print('   Gen    Rep     V1     V2     V3     V4     V5')
print(dados)
print('-'*100)

nl_dados, nc_dados = np.shape(dados) # Após feito isso, colocamos
# a função np.shape para obter o número de linhas e número de colunas, criando duas variáveis para colocar essas informações.
print('Número de linhas: {}'.format(nl_dados))
print('Número de colunas: {}'.format(nc_dados))
print('-'*100)


print('-'*100)
print('b- Pesquise sobre as funções np.unique e np.where da biblioteca numpy')
print('-'*100)

'''
help(np.where)
NP.WHERE: garante localizar qualquer posição em um array numpy de acordo com uma condição pré-determinada. Ela pode nos 
devolver a condição for especificada ela retorna tuplas. Também pode encontrar posições específicas dentro da matriz.
 
help(np.unique)
NP.UNIQUE: retorna os elementos exclusivos classificados de acordo com determinada condição de uma matriz.
Existem três saídas opcionais, além dos elementos exclusivos:
1- os índices da matriz de entrada que fornecem valores únicos
2- os índices da matriz exclusiva que reconstroem a matriz de entrada
3- o número de vezes que cada valor exclusivo aparece na matriz de entrada.
'''
print('-'*100)
print('c- Obtenha de forma automática os genótipos e quantas repetições foram avaliadas ')
print('-'*100)

gen = np.unique(dados[:,0]) # Nesse caso, foi utilizado a função unique para as duas primeiras colunas, sendo criada uma variável para cada coluna. A função np.unique
# retorna os elementos exclusivos classificados de acordo com determinada condição de uma matriz que neste caso vai selecionar os
# elementos diferentes em cada coluna.
rep = np.unique(dados[:,1])
print(" Número de genótipos {} número de repetições {}.".format(gen,rep))

print('-'*100)
print('d- Apresente uma matriz contendo somente as colunas 1, 2 e 4.')
print('-'*100)

''' 
Nesse caso, para apresentar a matriz com as colunas específicas vamos criar uma submatriz
que possui as colunas na posição 0, 1 e 3 e com todas as linhas:.
'''
submatriz_dados= dados[:,[0,1,3]] #:indica tos adn linhas
print('Matriz contendo somente as colunas 1,2 e 4:')
print(submatriz_dados)


print('-'*100)
print('e- Obtenha uma matriz que contenha o máximo, o mínimo, a média e a variância de cada genótipo para a variavel da'
      ' coluna 4. Salve esta matriz em bloco de notas. ')
print('-'*100)

submatriz_dados= dados[:,[0,1,3]] # Foi usado a submatriz da questão anterior.
matriz_gerada = np.zeros((len(np.unique(submatriz_dados[:, 0])), 5)) # Após feito isso, criamos uma variável para abrigar a nova matriz (np.zeros).
#Essa matriz possui a dimensão de 5 posições. Destas foi copiado a primeira coluna dos genótipos, para unificar as repetições.
it = 0 # Foi criado um loop com o for para gerar os dados de cada genótipo, de acordo com suas repetições. Nesse caso,
# o it vai ser os genótipos, a cada rodada será somado 1.
for n in range(0, len(np.unique(submatriz_dados[:, 0])), 1):
    it = it + 1
    print('Genótipo: {}'.format(it))
    print('Máxima: {}'.format(np.max((submatriz_dados[submatriz_dados[:, 0] == n + 1])[:, 2])))
    # O max e min, foram obtidos pela função do np. aplicadas a posição 0 da minha matriz, associando com a coluna 3.
    # A cada ciclo a variavel n, vai aumentando 1 (por exemplo, no segundo ciclo 1+1= genotipo 2 (variável).
    print('Mínimo: {}'.format(np.min((submatriz_dados[submatriz_dados[:, 0] == n + 1])[:, 2])))
    print('Média: {}'.format((np.around(np.mean((submatriz_dados[submatriz_dados[:, 0] == n + 1])[:, 2]), 3))))
    # No caso da média e variância, foram usadas np.around para formatar a quantidade de casas decimais.
    # A cada ciclo a variavel n, vai aumentando 1 (por exemplo, no segundo ciclo 1+1= genotipo 2 (variável).
    print('Variância: {}'.format((np.around(np.var((submatriz_dados[submatriz_dados[:, 0] == n + 1])[:, 2]), 3))))
    matriz_gerada[n, 0] = n + 1
    matriz_gerada[n, 1] = np.max((submatriz_dados[submatriz_dados[:, 0] == n + 1])[:, 2])
    matriz_gerada[n, 2] = np.min((submatriz_dados[submatriz_dados[:, 0] == n + 1])[:, 2])
    matriz_gerada[n, 3] = np.around(np.mean((submatriz_dados[submatriz_dados[:, 0] == n + 1])[:, 2]), 3)
    matriz_gerada[n, 4] = np.around(np.var((submatriz_dados[submatriz_dados[:, 0] == n + 1])[:, 2]), 3)
np.savetxt('MatrizReo1.txt', matriz_gerada) #Para salvar, np.savetxt.
print('Matriz Gerada --> Genótipo, Máxima, Mínima, Média e Variância')
print(matriz_gerada)

print('-'*100)
print('f-Obtenha os genótipos que possuem média (médias das repetições) igual ou superior a 500 da matriz gerada na letra anterior.')
print('-'*100)
media_maior_igual_500= matriz_gerada[:,3]>=500 # Na matriz do exercício anterior selecionamos na coluna 4, das médias, os valores boleanos
# que são maiores que 500.
coluna0= matriz_gerada[:,0] # criamos uma variável com a coluna dos genótipos da matriz.
genotipo_maior_igual_500= coluna0[media_maior_igual_500] # relacionamos os valores boleanos com a coluna de genótipos.
print('Os genótipos que apresentam média maior e igual a 500 são: {}'.format(genotipo_maior_igual_500))

print('-'*100)
print('g- Apresente os seguintes graficos: ')

print('-'*100)

#   Gráfico das médias

print('Médias dos genótipos para cada variável. Utilizar o comando plt.subplot para mostrar mais de um grafico por figura')
'''
Nesse caso, são 5 variáveis no vetor original, então foi criado 5 variáveis para abrigar a matriz de cada coluna, para a média.
Com a estrutura for, foi criada uma matriz das médias de cada genótipo para as 5 variáveis.
'''

media_v1 = np.zeros((10,1))   # Foi criado um vetor de zeros com 10 linhas e 1 coluna
media_v2 = np.zeros((10,1))
media_v3 = np.zeros((10,1))
media_v4 = np.zeros((10,1))
media_v5 = np.zeros((10,1))
contador = 0
for i in np.arange(0,30,3):   # percorre as 30 linhas do vetor original de acordo com o número de repetições
    media_v1[contador,0] = np.mean(dados[i:i + 3, 2], axis=0)
    media_v2[contador,0] = np.mean(dados[i:i + 3, 3], axis=0)
    media_v3[contador,0] = np.mean(dados[i:i + 3, 4], axis=0)       #média dos dados, acessando as três rep de cada genótipo.
    media_v4[contador,0] = np.mean(dados[i:i + 3, 5], axis=0)
    media_v5[contador,0] = np.mean(dados[i:i + 3, 6], axis=0)
    contador = contador + 1
genotipos = np.unique(dados[0:30,0:1], axis=0)
medias_variaveis = np.concatenate((genotipos, media_v1, media_v2, media_v3, media_v4, media_v5), axis=1)  #matriz com as medias dos genótipos p as 5 var Axis= 1 organiza as 5 colunas.. se for igual a 0, fica meio que empilhado
print('As médias das variáveis são:')
print(medias_variaveis)



plt.style.use('ggplot')
fig = plt.figure('Gráfico de Médias')
print('-'*100)

#Variável 1

plt.subplot(2,3,1)                          # dimensão da figura, duas linhas, três colunas, posição que o primeiro gráfico vai ocupar.
plt.bar(medias_variaveis[:,0], medias_variaveis[:,1])  # eixo x e y
plt.title('Variável 1')
plt.xticks(medias_variaveis[:,0])           #indicar o nome dos genótipos

#Variável 2

plt.subplot(2,3,2)
plt.bar(medias_variaveis[:,0], medias_variaveis[:,2])
plt.title('Variável 2')
plt.xticks(medias_variaveis[:,0])

##Variável 3

plt.subplot(2,3,3)
plt.bar(medias_variaveis[:,0], medias_variaveis[:,3])
plt.title('Variável 3')
plt.xticks(medias_variaveis[:,0])

##Variável 4
plt.subplot(2,3,4)
plt.bar(medias_variaveis[:,0], medias_variaveis[:,4])
plt.title('Variável 4')
plt.xticks(medias_variaveis[:,0])

#Variável 5

plt.subplot(2,3,5)
plt.bar(medias_variaveis[:,0], medias_variaveis[:,5])
plt.title('Variável 5')
plt.xticks(medias_variaveis[:,0])

plt.show()
nome = 'medias_variáveis_barras'
fig.tight_layout                                         #Adequar tamanho imagem

print('------------------------------------------------------------------------------------------')
print(' ')

#Gráfico dispersão

print('Dispersão 2D da médias dos genótipos (Utilizar as três primeiras variáveis). No eixo X uma variável e no eixo Y outra.')
print(' ')

print('Gráficos - Dispersão')
plt.style.use('ggplot') #tipo de gráfico
fig = plt.figure('Gráficos dispersão') # Título da figura
plt.subplot(2,2,1)                      # 1, 2 - delimitam como seria a figura    1 - posição do gráfico
plt.scatter(medias_variaveis[:,1], medias_variaveis[:,2], s=50, alpha=1, c='red')    #coordenada x- [:,1] coordenada y- [:,2] tamanho- s=50 transparencia- alpha=1

plt.title('Dispersão') #título do gráfico
plt.xlabel('Var 1') #título dos eixos x e y
plt.ylabel('Var 2')
plt.subplot(2,2,2)
plt.scatter(medias_variaveis[:,1], medias_variaveis[:,3], s=50, alpha=1, c='red')

plt.title('Dispersão')
plt.xlabel('Var 1')
plt.ylabel('Var 3')
plt.subplot(2,2,3)
plt.scatter(medias_variaveis[:,2], medias_variaveis[:,3], s=50, alpha=1, c='red')

plt.title('Dispersão')
plt.xlabel('Var 2')
plt.ylabel('Var 3')
fig.tight_layout()
plt.show()

