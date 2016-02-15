#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Guthierrez'

import sys
from unidecode import unidecode

try:
    source = open(sys.argv[1], 'r')
    word = sys.argv[2]
except IndexError:
    print('Argumentos inválidos, informe os arquivos de entrada e saída')
    sys.exit()

lines = source.readlines()
count = 0.0
for line in lines:
	if word in line.split():
		count+=1
print((count/24421)*100)