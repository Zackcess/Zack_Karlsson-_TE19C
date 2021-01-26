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


#8 Hade inte löst den utan facit
def växla(summa):
    kontanter = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
    sedlar = ["Tusenlappar", "Femhundralappar", "Tvåhundralappar", "Femtiolappar", "Tjugolappar", "Tiokronor", "Femkronor", "Enkronor"]

    for i in range(len(kontanter)):
        antal = summa//kontanter[i]
        summa %= kontanter[i]
        print(f"{antal} {sedlar[i]}", end=", ")

växla(2333)



#10
import random as rnd

def skapaKortlek():
    kortnummer=[i for i in range(2,11)]
    klättkort=["J", "Q", "K", "A"]
    kortnummer+=klättkort
    lek=kortnummer*4

    blandaKortlek(lek)
    return lek

Kast=[]
import random as rnd
for i in range(10):
    y=rnd.randint(1,6)
    Kast.append(y) 
    list.sort(Kast)
print(Kast)

Kast=[]
import random as rnd
for i in range(10):
    y=rnd.randint(1,6)
    Kast.append(y) 
    list.sort(Kast)
    list.reverse(Kast)
print(Kast)

import matplotlib.pyplot as plt
x = [i for i in range(-10,11)]
y= [i**2 for i in range(-10,11)]
plt.plot(x,y)
plt.show()
'''
'''
#3 
bräde=[[i for i in range (9)],['A','B', 'C', 'D', 'E', 'F', 'G', 'H']]
for x in bräde[0]:
    for y in bräde[1]:
        print(y+str(x), end=" ")

#4
s=0
n = int(input("Skriv i n?"))
a1 = int(input("Skriv i a1?"))
an = int(input("Skriv i an?"))
def artimetisk_summa(n,a1,an):
    s=(n*(a1+an))/2
    return s
print(f"{artimetisk_summa(n,a1,an)}")

#1 
tal = int(input("Skriv ett tal och du får veta om det är+-: "))
if tal <0:
    print('Det är negativt')
elif tal>0:
    print('Det är poistivt')
else:
    print('Det är noll')

belopp=int(input("Mata in ett tal och få reda dess absolutbelopp: "))
if belopp <0:
    x=-belopp
    print(f"|{x}|")
elif belopp>0:
    print(f"|{belopp}|")

import math
#10
a=1
b=3
c=1
p=b/a
q=c
x1=((-p)/2) + math.sqrt((p/2)**2 - q)
x2=((-p)/2) - math.sqrt((p/2)**2 - q)

print(f"x1={x1} x2={x2}")

def växla(summa):
    sedlar = [1000, 500, 200, 100, 50,20,10,5,1]
    pengar=['Tusenlappar', 'Femhundralappar', 'Tvåhundralappar', 'Tvåhundralappar', 'Hundralappar','Femtiolappar', 'Tjugolappar', 'Tior', 'Femkronor', 'Enkronor']
    for i in range (len(sedlar)):
        antal=summa//sedlar[i]
        summa %= sedlar[i] 
        print(f"{antal} {pengar[i]}", end=" ")
växla(2222)

s=0
n=0
while s<=99:
    s+=1
    n+=s
print(n)

s=0
n=0
while s<99:
    s+=1
    n+=s
print(n)
'''

s=0
n=1
while n>=0:
    s=(1/(2**n))
print(s)