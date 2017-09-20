# -*- coding: utf-8 -*-
__author__='BenjaminFernandez'

from bs4 import BeautifulSoup
import requests

url = "https://www.cinesur.com/home.php?id_cine=318"
req = requests.get(url)

statusCode = req.status_code
if statusCode == 200:
    html = BeautifulSoup(req.text,"html.parser")
    #horarios = html.find('div',{'class':'horarios'})
    pelis = html.find_all('div',{'class':['oscuro','claro']},recursive=True)
    for i, peli in enumerate(pelis):
        if hasattr(peli.find('a',{'class':'titulo_peli'}),'getText'):
            titulo = peli.find('a',{'class':'titulo_peli'}).getText().lstrip()
            print(titulo)

            horas=peli.find_all('a',{'class':'sin_estilo'},recursive=True)
            for i, hora in enumerate(horas):
                print('\t',hora.getText())
