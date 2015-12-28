#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Guthierrez'

import sys
import math

def calcularPesoPalavra(ocorrenciasNaMensagem, tamanhoMensagem, numTotalMensagens, qtdMensagensComPalavra):
    tf = ocorrenciasNaMensagem/tamanhoMensagem
    idf = math.log10(numTotalMensagens/qtdMensagensComPalavra)
    return tf*idf

try:
    origem = open(sys.argv[1], 'r')
    destino = open(sys.argv[2], 'w')
except IndexError:
    print('Argumentos inválidos, informe os arquivos de entrada e saída')
    sys.exit()

id = 1
qtdMensagensComPalavra = {}
registroPalavras = {}
linhas = origem.readlines()
numTotalMensagens = len(linhas)

#Percorre cada mensagem do arquivo
for index, linha in enumerate(linhas):
    classe = linha[:linha.index(']')+1].rstrip('\n') #Classe e autor da mensagem
    mensagem = linha[linha.index(']')+2:].rstrip('\n') #Conteúdo da mensagem
    palavrasVerificadas = [] #Palavras já percorridas em uma mensagem
    tamanhoMensagem = len(mensagem.split(' ')) #Tamanho de cada mensagem
    linhaParaTeste = ''
    casoDeTeste = {}
    
    #Percorre cada palavra da mensagem
    for palavra in mensagem.split(' '):
        ocorrenciasNaMensagem = 0
        ocorrenciasNoArquivo = 0
        
        #Se a palavra na mensagem é encontrada pela primeira, verifica-se a quantidade de ocorrências na mensagem
        if palavra not in palavrasVerificadas:
           ocorrenciasNaMensagem = mensagem.split(' ').count(palavra)
           palavrasVerificadas.append(palavra)

           #Se a palavra não está no dicionário global de palavras, insere-se a palavra e atribui um id
           if palavra not in registroPalavras:
               registroPalavras[palavra] = id
               id+=1
               
               #Contagem de quantas mensagens possuem uma determinada palavra
               for msg in linhas:
                   palavrasMensagem = msg[msg.index(']')+2:].rstrip('\n').split(' ')
                   if palavra in palavrasMensagem:
                       ocorrenciasNoArquivo +=1
               qtdMensagensComPalavra[palavra] = ocorrenciasNoArquivo
           casoDeTeste[registroPalavras[palavra]]=calcularPesoPalavra(ocorrenciasNaMensagem, tamanhoMensagem, numTotalMensagens, qtdMensagensComPalavra[palavra])
    
    #Constrói a linha de teste com as features ordenadas
    for id in sorted(casoDeTeste):
        linhaParaTeste += str(id) + ':' + str(casoDeTeste[id]) + ' '

    #Escreve a linha no arquivo    
    destino.write(classe + ' ' + linhaParaTeste + " #"+ str(index+1) + '\n')
    print(str(index+1))
for id in sorted(qtdMensagensComPalavra, key=qtdMensagensComPalavra.get, reverse=False):
    print(id, qtdMensagensComPalavra[id])

