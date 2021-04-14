# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 17:39:21 2021

@author: arthur
Le os dados baixados de uma pasta (\downloads) e os reescreve e processa na pasta \saida
Renomeia os dados diarios baixados. O arquivo com "estacao_bruto" é o arquivo baixado
renomeado com o código da estação, o arquivo com o nome da estação é o dados processado,
que nomeia as colunas e tira alguns espaços em branco do arquivo (davam problema
na hora de montar os dataframes)
"""

#import requests, bs4

import pandas as pd
import os

#variaveis iniciais - pasta de entrada e saida
source = os.getcwd() + '\downloads'
goal = os.getcwd() + '\sai'

individual_path = []
files = []
file_name = []
#le os arquivos de entrada
for r, d, f in os.walk(source):
    for file in f:
        if 'txt' in file:
#            Para plotar com caminho:
            files.append(os.path.join(file))
#           (r, file) plota com o caminho. Sem o r plota só o nome do arquivo
            individual_path.append(os.path.join(r, file))

#line = individual_path[0]
for line in individual_path:
    abre1 = open(line, "r")
    abre1 = ''.join([i for i in abre1]) \
        .replace("  ", " ")
    data_base0 = open("output_temp.csv","w")
    data_base0.writelines(abre1)
    data_base0.close()
    data_base = pd.read_csv('output_temp.csv', delimiter = ' ', header=None, encoding = 'latin-1') #ABRE O ARQUIVO SE ESTIVER DISPONIVEL
    data = data_base.rename(columns={0: 'Estacao', 1: 'Ano', 2: 'Mes', 3: 'Dia', 6: 'Nivel', 7: 'Vazao'})
    data['Nivel'] = data['Nivel'].fillna('-')
    data = data.drop([4, 5, 8], axis = 1)
    codigo = data['Estacao'][1]
    print(codigo)
    corrige_vazao = data['Vazao']
    corrige_vazao = corrige_vazao.str.replace(',','.')
    data['Vazao'] = corrige_vazao
    data = data.drop(['Estacao'], axis = 1)
    goal_file = goal + '\\' + str(codigo) + '.csv'
    data.to_csv(goal_file, encoding = 'latin-1', index=False)
    goal_file = goal + '\\' + 'bruto' + str(codigo) + '.csv'
    os.renames(line, goal_file)