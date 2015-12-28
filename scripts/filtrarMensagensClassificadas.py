#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Guthierrez'

import sys

try:
    source = open(sys.argv[1], 'r')
    target = open(sys.argv[2], 'w')
    filestopwords = open(sys.argv[3])
    stopwords = []
    for word in filestopwords.readlines():
        stopwords.append(word.rstrip())
except IndexError:
    print('Argumentos inválidos, informe os arquivos de entrada e saída')
    sys.exit()

lines = source.readlines()

for index, line in enumerate(lines):
    if '-[' in line and len(line) > 15:
        
        line = line.lower()
        line = line.replace('] ', ' '+str(index+1)+' ] ')

        #Remover caracteres especiais
        for char in line:
            if char in '!#.,();\'\"?:@':
                line = line.replace(char, ' ')
        
        #Separando cada linha em palavras
        words = line.split()
      
        #Retirando stopwords       
        for word in stopwords:
            if word in words:
                while word in words:          
                    words.remove(word)
      
        #Escrevendo a linha no novo arquivo
        target.write(' '.join(words) + '\n')

source.close()
target.close()
filestopwords.close()
