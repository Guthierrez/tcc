#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Guthierrez'

import sys
from unidecode import unidecode

try:
    source = open(sys.argv[1], 'r')
    target = open(sys.argv[2], 'w')
    filestopwords = open(sys.argv[3])
    stopwords = []
    for word in filestopwords.readlines():
        stopwords.append(word.rstrip())
    stopwords = [unicode(x, 'utf-8') for x in stopwords]
except IndexError:
    print('Argumentos inválidos, informe os arquivos de entrada e saída')
    sys.exit()

lines = source.readlines()


for index, line in enumerate(lines):
    if '-[' in line :
        
        line = line.replace('] ', ' '+str(index+1)+' ] ')
        classe = line[:line.index(']')+1].rstrip('\n') #Classe e autor da mensagem
        mensagem = line[line.index(']')+2:].rstrip('\n') #Conteúdo da mensagem
        mensagem = unicode(mensagem, "utf-8")
        mensagem = unidecode(mensagem)
        mensagem = mensagem.lower()
        aux = []
        
        #Remover caracteres especiais
        for char in mensagem:
            if char in u'!#.,();\'\"?:_/0123456789-[]$|%+=':
                mensagem = mensagem.replace(char, ' ')
        
        #Separando cada linha em palavras
        words = mensagem.split()
      
        #Retirando stopwords       
        for word in stopwords:
            if word in words:
                while word in words:          
                    words.remove(word)

        for word in words:
            if 'http' not in word and 'www' not in word and '@' not in word and len(word) > 2:
                aux.append(word)
        target.write(u' '.join(aux).encode('utf-8').strip() + '\n')
        print(index+1)

source.close()
target.close()
filestopwords.close()
