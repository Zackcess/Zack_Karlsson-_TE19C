#Funktioner inparameter return sats lokala variabler

def medelvärde(a,b,c,d):
    medel=(a+b+c+d)/4#lokal variabel
    return medel

print()
print(f"{medelvärde(1,2,3,4)}")
print(f"{medelvärde(10,20,30,40)}")

#räkna ord
def räkna_ord(text):
    ord=text.split()
    antal_ord=len(ord)
    return antal_ord 

citat="I stand on the shoulders of giants"
print(f"antal ord i citatet: {räkna_ord(citat)}")
import numpy as np
import math 
import matplotlib.pyplot as plt
def räkna_tal(a):
    tal=11/(1+3.4*np.exp(-0.03*a))
    return tal
print(f"Svar antal människor i miljarder 1950: {räkna_tal(0)} miljarder")

#b stoppar man in ett stort värde slutar det på 11, vilket måste vara den övre gränsen
år=500
a=np.arange(år)
plt.plot(a, räkna_tal(a))
plt.grid()
plt.show()
plt.ylabel("antal människor i miljarder")
plt.xlabel("År efter 1950")
plt.title("Modell för population")
print(f"övregräns: {räkna_tal(år)}")