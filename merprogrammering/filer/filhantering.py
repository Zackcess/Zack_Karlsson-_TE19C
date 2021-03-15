'''
with open("filer/Stora forskare.txt", "r") as f1:
    for rad  in f1:
        print(rad, end="")

före1800=[]
with open("Stora forskare.txt", "r") as f1:
    for rad in f1:
        rad = rad.strip("\n")
        print(rad)
        år=int(rad[-10:-6])
        if år <1800:
            före1800.append(rad[0:-11])


with open("Stora forskare.txt", "r") as f1, open("Stora forskare 2.txt", "w") as f2:
    for rad in f1:
        rad=rad.strip(" ")
        f2.write(rad)
    
    f2.write("Andrew wile 1953-04-11\n")
#1
x=0
import random as rnd
tärningskast=[rnd.randint(1,6) for k in range(10)]
with open("diceRoll.txt","w") as f1:
    f1.write(f"Simulera 10 tärningskast: {tärningskast}\n")
    f1.write(f"Kasten sorterat: {sorted(tärningskast)}\n")    
    f1.write(f"Antal femmor: {tärningskast.count(5)}")


talLista=[i for i in range(10)]
with open("tal.txt", "w") as f:
    for tal in talLista:
        f.write(f"{tal} ")

#2
lst=[]
with open("Provresultat.txt", "r") as f1:
    for rad in f1:
        print(rad, end="\n")
        rad=rad.strip("\n")
        lst.append(rad)
    lst.sort()
    print(*lst, sep='\n',end="\n")

#3 funkar inte för svår
ma2a=[]
ma2c=[]
betyglista=[]
import matplotlib.pyplot as plt
import numpy as np
with open("NPvt19Ma2A.txt", "r") as f1, open("NPvt19Ma2C.txt", "r") as f2:
    for rad in f1:
        rad=rad.replace("%", " ")
        ma2a.append(rad)
    for i in range(6):
        betyglista= ma2a[i][1:6]
        print(betyglista)
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    
    plt.pie(betyglista, colors=colors)
    plt.axis('equal')
    plt.show()

    for rad in f2:
        rad=rad.replace("%", " ")
        ma2c.append(rad)
    for i in range(6):
        print(ma2c[i][1:6])
'''
#4 Denna funkar mer, lite långkod dock 
import random as rnd

fil = open("simulering.txt","x")

exponent = int(input("Ange en exponent för 10^x: "))

antal_ettor = 0
antal_tvåor = 0
antal_treor = 0
antal_fyror = 0
antal_femmor = 0
antal_sexor = 0

simulator_start = 0

while simulator_start < exponent:
    simulator_start = simulator_start + 1
    for i in range(10**simulator_start):
        dice = rnd.randint(1,6)
        if dice == 6:
            antal_sexor = antal_sexor + 1
        elif dice == 5:
            antal_femmor = antal_femmor + 1
        elif dice == 4:
            antal_fyror = antal_fyror + 1
        elif dice == 3:
            antal_treor = antal_treor + 1
        elif dice == 2:
            antal_tvåor = antal_tvåor + 1
        else:
            antal_ettor = antal_ettor + 1

    sannolikhet_ettor = antal_ettor/(10**simulator_start)
    sannolikhet_tvåor = antal_tvåor/(10**simulator_start)
    sannolikhet_treor = antal_treor/(10**simulator_start)
    sannolikhet_fyror = antal_fyror/(10**simulator_start)
    sannolikhet_femmor = antal_femmor/(10**simulator_start)
    sannolikhet_sexor = antal_sexor/(10**simulator_start)

    fil.write(f"\nVid {10**simulator_start} kast ar : \nAntal ettor = {antal_ettor}, sannolikhet {sannolikhet_ettor} \nAntal tvaor = {antal_tvåor} , sannolikhet {sannolikhet_tvåor} \nAntal treor = {antal_treor}, sannolikhet {sannolikhet_treor} \nAntal fyror = {antal_fyror}, sannolikhet {sannolikhet_fyror} \nAntal femmor = {antal_femmor}, sannolikhet {sannolikhet_femmor} \nAntal Sexor = {antal_sexor}, sannolikhet {sannolikhet_sexor}")
    fil.write(f"\n")
    # print(f"Vid {10**simulator_start} kast är : Antal ettor = {antal_ettor}, sannolikhet {sannolikhet_ettor} Antal tvåor = {antal_tvåor} , sannolikhet {sannolikhet_tvåor} Antal treor = {antal_treor}, sannolikhet {sannolikhet_treor} Antal fyror = {antal_fyror}, sannolikhet {sannolikhet_fyror} Antal femmor = {antal_femmor}, sannolikhet {sannolikhet_femmor} Antal Sexor = {antal_sexor}, sannolikhet {sannolikhet_sexor}")
