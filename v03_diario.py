# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 17:39:21 2021

@author: arthur
Baixa as estações baseado em uma lista de entrata, para as vazões mensais.
Esse selenium é meio chatinho de instalar, especialmente ao indicar o endereço do driver navegador.
Usei esse tutotial https://chromedriver.chromium.org/getting-started. Fora isso, é só entrar com
a lista de estações (arquivo csv na mesma pasta do programa). As estações são baixadas na pasta de 
downloads do navegador, como qualquer outro arquivo. Destaco que tentei fazer isso com o Firefox,
o padrão do programa, mas não funcionou.
"""
#import requests, bs4
from selenium import webdriver
import pandas as pd
import os

#define alguns pontos para o download
browser = webdriver.Chrome()
#browser = webdriver.Chrome()
url_real = 'http://www.sih-web.aguasparana.pr.gov.br/sih-web/gerarRelatorioVazoesFluviometricas.do?action=carregarInterfaceInicial'
#browser.get(url_real)

#abre a lista de estacoes e ja cria o laço
path = os.getcwd()
entra_estacoes = path + '\\lista_estacoes.csv'
lista_estacoes_pandas = pd.read_csv(entra_estacoes, delimiter = ',', encoding = 'latin-1')
lista_estacoes = lista_estacoes_pandas['Codigo'].tolist()

for nome_estacao in lista_estacoes:
    #abre a pagina e baixa os dados um a aum
    browser.get(url_real)
    WebElement = browser.find_element_by_id('codEstacao')
    WebElement.send_keys(nome_estacao)
    WebElement = browser.find_element_by_id('anoInicial')
    WebElement.send_keys('1900')
    WebElement = browser.find_element_by_id('anoFinal')
    WebElement.send_keys('2021')
    WebElement = browser.find_element_by_id('TXT')
    WebElement.click()
    WebElement = browser.find_element_by_xpath("//*[@id='conteudo']/div/form/div[2]/input[1]")
    WebElement.click()
    print(nome_estacao)