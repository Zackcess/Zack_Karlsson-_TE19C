'''
#4 "Do not worry about your difficulties in Mathematics. I can assure you mine are still greater."
vokaler = "aeiouy"
mening="Do not worry about your difficulties in Mathematics. I can assure you mine are still greater."
vokalerna = []

for ord in mening: #Varje ord gås igenom mening
    for vokal in vokaler: #Varje ord i vokaler
        if ord == vokal:#Går igenom varje ord och om det finns en vokal i det, ifall det ger till vokaler
            vokalerna.append(ord)

print(f"Antalet vokaler är {len(vokalerna)}")
print("\n")
print(f"Vokalerna är: {vokalerna}")
'''
'''
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
'''
'''
n = int(input("Mata in ett tal: "))
def addition_summa(n):
    s=(2*n+1)
    return s
print(f"Summan av talen blir: {addition_summa(n)}")
'''
'''
def triangelArea(bas, höjd):
    area = (bas*höjd)/2
    return area
area1=triangelArea(2,4)
area2=triangelArea(10,12)
print(f"Arean på en triangel med bas 2 l.e. och höjd 4 l.e. är: {area1}a.e.")
print(f"Arean på en triangel med bas 10 l.e. och höjd 12 l.e. är: {area2}a.e.")
'''
'''
#1c
n =int(input("Antal tal du vill ha: "))
a1=int(input("Ange startal: "))
an =int(input("Ange sluttal: "))

def aritmetisk_summa(n,a1,an):
    summa=(n*(a1 + an))/2
    return summa
print(f"Aritmetiska summan är: {aritmetisk_summa(n,a1,an)}")
'''
'''
#2a
n=int(input("Ange ett tal: "))
def summatal(n):
    s=2*n+1
    return s
print(f"Summa av tal blir: {summatal(n)}")
'''
'''
#b
n=int(input("Ange ett tal: "))
s1=int(input("Ange ett startvärde: "))
def summatal(s1,n):
    s=2*n+s1
    return s
print(f"Summa av tal blir: {summatal(s1,n)}")
'''
'''
#4
antal_tusenlappar = 0
antal_femhundralappar = 0
antal_tvåhundralappar = 0
antal_hundralappar = 0
antal_femtiolappar = 0
antal_tjugolappar = 0
antal_tiokronor = 0
antal_femkronor = 0
antal_enkronor = 0
summa=int(input("Ange en summa som du behagar: "))
while summa >0:
    def summa(x):
        if x%1000:
            x=-1000
            antal_tusenlappar=+1
print(mängd)
            



print(f"antal tusenlappar{tusenlapp(p)}")
'''
'''
#2a
import math
n=int(input("Skriv ett tal: "))


def nummer(n):
  total = 0
  for i in range (1,n*2+2,2):
    total += i
  return total

print(f"Totalen blir:{nummer(n)}")
'''
'''
#2b
s=int(input("Ange ett startvärde: "))
n=int(input("Skriv ett tal: "))
def nummer(n,s):
  total = 0
  for i in range (s,n*2+2,2):
    total += i
  return total
print(f"Totalen blir:{nummer(n,s)}")


summa=int(input("Ange en summa du vill ha i sedlar: "))
def sedlar(summa):
    Tusenlappar = 0
    Femhundralappar = 0
    Tvåhundralappar = 0
    Hundralappar = 0
    Femtiolappar = 0
    Tjugolappar = 0
    Tior = 0
    Femkronor = 0
    Enkronor = 0
    if summa%1000:
        Tusenlappar+=1
        summa-=1000  
    return Tusenlappar

    elif summa%200:
        Tvåhundralappar+=1
        summa-=200
        
    elif summa%100:
        Hundralappar+=1
        summa-=100
        
    elif summa%20:
        Tjugolappar=+1
        summa-=20
        
    elif summa%10:
        Tior+=10
        summa-=10
        
    elif summa%5:
        Femkronor+=1
        summa-=5
        
    elif summa%1:
        Enkronor+=1
        summa-=1
       

print(f"Antal Tusenlappar: {sedlar(summa)}")

'''
