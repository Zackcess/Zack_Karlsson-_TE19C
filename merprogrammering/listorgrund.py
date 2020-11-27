#listor, indexering, append(), loopa lista, 2D lista, list comprehension.
#Indexering/åtkomstoperatorn
'''
frukter=["äpple", "päron", "vattenmelon", "jordgubbe", "blåbär"]
print(f"Fruktlista:{frukter}")
print(f"Frukter[0]:{frukter[0]}")
print(f"Frukter[-1]:{frukter[-1]}")
print(f"Frukter[3]:{frukter[3]}")
print(f"frukter[::-1]:{frukter[::-1]}")
print("\n")

#Loopat igenom en lista
for frukt in frukter:
    print(f"Frukt: {frukt}")
'''
'''
grönsaker=["tomat", "gruka", "majs", "sallad"]
frukter=["äpple", "päron", "vattenmelon", "jordgubbe", "blåbär"]
fruktsallad=[] #Tom lista

#append lägger till element till lista
for grönsak in grönsaker:
    fruktsallad.append(grönsak)
for frukt in frukter:
    fruktsallad.append(frukt)
print(fruktsallad)
'''

import matplotlib.pyplot as plt
import numpy as np
#list comprehension
y=[2*x-2 for x in range (10)]
x=[x for x in range(10)]
print(f"x:{x}")
print(f"y:{y}")



#2d lista
tabell=[]

for i in range(11):
    rad=[x*i for x in range(11)]#En rad av gånger tabellen
    tabell.append(rad)
    for j in range(11):
        print(f"{tabell[i][j]:3}", end=" ")
    print()
print()
print(f"tabell[3]: {tabell[3]}")
print(f"tabell[3][3]: {tabell[3][3]}")
