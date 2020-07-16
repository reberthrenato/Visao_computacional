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





