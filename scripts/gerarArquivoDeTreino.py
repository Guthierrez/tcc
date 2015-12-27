#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Guthierrez'

import sys

ehDaClasse = 0
naoEhDaClasse = 0

try:
    origem = open(sys.argv[1], 'r')
    classe = sys.argv[2]
    treino = open('classe'+sys.argv[2]+'treino.txt', 'w')
    teste = open('classe'+sys.argv[2]+'teste.txt', 'w')
except IndexError:
    print('Argumentos inválidos, informe os arquivos de entrada e saída')
    sys.exit()

for linha in origem.readlines():
    casoDeTeste = linha[linha.index(']')+2:].rstrip('\n')
    if linha.startswith(classe+"-[") or '['+classe+'-[' in linha:
        if ehDaClasse < 2:
            treino.write('1 ' + casoDeTeste + '\n')
            ehDaClasse += 1
        else:
            teste.write('1 ' + casoDeTeste + '\n')
            ehDaClasse = 0
    else:
       if naoEhDaClasse < 2:
            treino.write('-1 ' + casoDeTeste + '\n')
            naoEhDaClasse += 1
       else:
            teste.write('-1 ' + casoDeTeste + '\n')
            naoEhDaClasse = 0

