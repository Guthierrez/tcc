#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Guthierrez'

import sys

try:
    model = open(sys.argv[1], 'r').readlines()
    documents = open(sys.argv[2], 'r').readlines()
    numberOfDocuments = int(documents.pop(0))
    numberOfTopics = len(documents[0].split())
    topics = []
    for i in range(numberOfTopics):
    	topics.append(open(str(i)+'.txt', 'w'))
    for document in range(numberOfDocuments):
		values = model[document].split()
		values = map(float, values)
		greater = max(values)
		topicOfDocument = values.index(greater)
		topics[topicOfDocument].write(documents[document])


except IndexError:
	print('Argumentos inválidos, informe os arquivos de entrada e saída')
	sys.exit()