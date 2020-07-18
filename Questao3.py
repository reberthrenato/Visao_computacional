########################################################################################################################
########################################################################################################################
# DATA: 18/07/2020
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
##### Pacotes da questão 3 #####

import numpy as np

##### Questão 3.a #####
def media (vetor):
    somador = 0
    contagem_de_dados = 0
    it = 0
    for i in vetor:
        somador = somador + i
        it = it + 1
        contagem_de_dados = contagem_de_dados + 1
        mean = somador/contagem_de_dados
    return mean

def var_amostral (vetor):
    somador = 0
    it = 0
    sdq = 0
    for i in vetor:
        somador = somador + i
        it = it + 1
        sdq = sdq + i**2
    var = (sdq - ((somador**2/it)))/(it-1)
    return var

