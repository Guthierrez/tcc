# -*- coding: utf-8 -*-

import sqlite3

__author__ = 'Guthierrez'

import sys

try:
    target = open(sys.argv[1], 'w')
except IndexError:
    print('Argumentos inválidos, informe os arquivos de entrada e saída')
    sys.exit()

conn = sqlite3.connect("database/reclamacoes.db")
cursor = conn.cursor()
result = cursor.execute("SELECT mensagem FROM reclamacoes").fetchall()

for index, row in enumerate(result):
	target.write(str(index+1) + '-[] ' + row[0].encode('utf8') + '\n')

print('Done!')