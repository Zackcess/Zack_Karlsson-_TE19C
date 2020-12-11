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


#1a
def aritmetisk_summa(n,a1,an):
    summa=(n*(a1 + an))/2
    return summa
print(f"Aritmetiska summan är: {aritmetisk_summa(10,1,10)}")
#1b
def aritmetisk_summa(n,a1,an):
    summa=(n*(a1 + an))/2
    return summa
print(f"Aritmetiska summan är: {aritmetisk_summa(100,1,100)}")
#1c
n =int(input("Antal tal du vill ha: "))
a1=int(input("Ange startal: "))
an =int(input("Ange sluttal: "))

def aritmetisk_summa(n,a1,an):
    summa=(n*(a1 + an))/2
    return summa
print(f"Aritmetiska summan är: {aritmetisk_summa(n,a1,an)}")
#2a
n=int(input("Skriv ett sluttal: "))


def nummer(n):
  total = 0
  for i in range (1,n*2+2,2):
    total += i
  return total

print(f"Totalen blir:{nummer(n)}")
#2b
s=int(input("Ange ett startvärde: "))
n=int(input("Skriv ett tal: "))
def nummer(n,s):
  total = 0
  for i in range (s,n*2+2,2):
    total += i
  return total
print(f"Totalen blir:{nummer(n,s)}")

#3
import math
y2=int(input("Ange ett y-värde: "))
x2=int(input("Ange ett x-värde: "))
y1=int(input("Ange ett till y-värde: "))
x1=int(input("Ange ett till x-värde: "))
def avstånd(y2,x2,y1,x1):
    summa=math.sqrt((y2-y1)**2+(x2-x1)**2)
    return summa
print(f"Avståndet är: {avstånd(y2,x2,y1,x1)}")

#4
def pengar(summa):

    antal_tusenlappar = 0
    antal_femhundralappar = 0
    antal_tvåhundralappar = 0
    antal_hundralappar = 0
    antal_femtiolappar = 0
    antal_tjugolappar = 0
    antal_tiokronor = 0
    antal_femkronor = 0
    antal_enkronor = 0

    while summa > 0:

        if summa >= 1000:
            summa -= 1000
            antal_tusenlappar += 1
            pass

        elif summa >= 500:
            summa -= 500
            antal_femhundralappar += 1
            pass

        elif summa >= 200:
            summa -= 200
            antal_tvåhundralappar += 1
            pass

        elif summa >= 100:
            summa -= 100
            antal_hundralappar += 1
            pass

        elif summa >= 50:
            summa -= 50
            antal_femtiolappar += 1
            pass

        elif summa >= 20:
            summa -= 20
            antal_tjugolappar += 1
            pass

        elif summa >= 10:
            summa -= 10
            antal_tiokronor += 1
            pass

        elif summa >= 5:
            summa -= 5
            antal_femkronor += 1
            pass

        elif summa >= 1:
            summa -= 1
            antal_enkronor += 1
            pass


    print(antal_tusenlappar, "tusenlappar")
    print(antal_femhundralappar, "femhundralappar")
    print(antal_tvåhundralappar, "tvåhundralappar")
    print(antal_hundralappar, "hundralappar")
    print(antal_femtiolappar, "femtiolappar")
    print(antal_tjugolappar, "tjugolappar")
    print(antal_tiokronor, "tiokronor")
    print(antal_femkronor, "femkronor")
    print(antal_enkronor, "enkronor")


pengar(3293)