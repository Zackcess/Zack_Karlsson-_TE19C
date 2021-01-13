'''
#1
birds= 8000 #Fåglar start
year=0 #Från år 0
while birds > 800: #Så länge det är fler fåglar än 800
    year+= 1 #Då adderars ett år
    birds/=2 #och fåglarna divideras på två
    print(f"År {year}: antal fåglar: {birds:.0f}") #Slutprodukten beskiver hur fåglarna halveras i fyra år till ett minimum på 500 efter 4 år.

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
'''
#6 Den ska visa om det är rätt eller fel och hur långt ifrån det är.
def tabell(x):
    for i in range(10):

