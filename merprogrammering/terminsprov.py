'''
#1
birds= 8000 #Fåglar start
year=0 #Från år 0
while birds > 800: #Så länge det är fler fåglar än 800
    year+= 1 #Då adderars ett år
    birds/=2 #och fåglarna divideras på två
    print(f"År {year}: antal fåglar: {birds:.0f}") #Slutprodukten beskiver hur fåglarna halveras i fyra år till ett minimum på 500 efter 4 år.
#2

import matplotlib.pyplot as plt #importerar in graf funktionen

def f(x): 
    return x**2-3*+1 #En graf

x= [i for i in range(10)] #lägger up x intervallet 0-9
y= [f(i) for i in x]#Checkar 
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#3
def medelvärde(a,b,c):
    addera = a+b+c
    addera/=3
    return addera
print(medelvärde(1,3,5))

#4
radie=int(input("Ange en radie:" ))
import math
def vol(radie):
    volym=(math.pi*4*radie**3)/3
    return volym
print(round(vol(radie)))

#5 
mening=(input("Mata in en mening: "))
def räkna_ord(mening):
    ord=mening.split()
    antal_ord=len(ord)
    return antal_ord 

print(f"antal ord i mening: {räkna_ord(mening)}")

#6 Den ska visa om det är rätt eller fel och hur långt ifrån det är.
import random as rnd
spela=True
svar=i*num
while spela:
    num=int(input("Skriv in en gångertabell du vill träna: "))
    for i in range (1,11):
        print(num, 'x', i, '=',"?")
        y=int(input("Ditt svar? "))
        if y ==num*i:
            print("duktig pojke")
        elif y<num*i:
            print("inte duktig pojke, för lite")
        elif y>num*i:
            print("inte duktig pojke, för mkt")

    z=input("Vill du spela igen?") 
    if z!="j":
        spela=False

femmor=0
#7
import random as rnd
for t in range(1,1000):
    y=rnd.randint(1,6)
    if y==5:
        femmor+=1
print(f"Antal femmor är: {femmor}")
print(f"Andelen femmor är:{(femmor/1000)*100}% ")
'''
#8

cash=int(input("Ange en summa pengar: "))
def pengar(cash):
    tusenlappar=0
    tvåhundralappar=0
    while cash>1000:
        cash-=1000
        tusenlappar+=1
    if cash%200==0:
        cash-=200
        tvåhundralappar+=1

    return tusenlappar, tvåhundralappar
print(pengar(cash))
#modulus och 