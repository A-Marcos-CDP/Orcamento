# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:26:55 2020

@author: A. Marcos
@title: Contador
"""

import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt
import xlsxwriter as xlsw
import eel

open("web/Out.html", "w").close()

eel.init('web')

def transfer(plan, atual):
    vac=[]
    ins=pd.read_excel(("{}").format(plan), usecols = "B", header=None, skiprows=atual, nrows=1)
    insert=ins[1][0]
    if insert != 'FIM':
        ins2=pd.read_excel(("{}").format(plan), usecols = "C", header=None, skiprows=atual, nrows=1)
        insert2=ins2[2][0]
        ins3=pd.read_excel(("{}").format(plan), usecols = "D", header=None, skiprows=atual, nrows=1)
        insert3=ins3[3][0]
        vac.append(insert)
        vac.append(insert2)        
        vac.append(insert3)
        lista_comp.append(vac)
        atual=atual+1
        transfer(plan, atual)
        
def contab(lista_comp):
        for i in range(0, len(lista_comp), 1):
            x=lista_comp[i][0]
            if x in lista_check:
                y=finder(lista_cont, x)
                z=lista_comp[i][1]
                lista_cont[y][1]=lista_cont[y][1]+z
            else:
                lista_check.append(lista_comp[i][0])
                lista_cont.append(lista_comp[i])


def finder(lista, nome):
    for i in range (0, len(lista), 1):
        if lista[i][0] == nome:
            return i
                
                
lista_check=[]
lista_cont=[]
lista_comp=[]

plan="Orçamento.xlsx"
out="Orçamento - Saída.xlsx"


@eel.expose
def direct(name,output):
    plan=(r'{}'.format(name))
    out=(r'{}'.format(output))


@eel.expose
def getDone():
    transfer(plan, 4)
    contab(lista_comp)

    df=pd.DataFrame(lista_cont)
    print(df)
    writer=out

    html=df.to_html()
    with open("web/Out.html", "w", encoding="utf-8") as file:
        file.writelines('<meta charset="UTF-8">\n')
        file.writelines('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">\n')
        file.write(html)

    df.to_excel(writer, sheet_name='Saída', startrow=1, startcol=1, header=False, index=False)




eel.start('index.html', size=(1000, 600))