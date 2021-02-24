'''
while True:
    try:
        ålder=float(input("Hur gammal är du?"))
        assert ålder >= 0 and ålder < 125, "Din ålder ska vara mellan 0 och 124"
        break#Hoppar ut från whilesatsen
    except AssertionError as msg:
        print(msg)
    except:
        print("Ålder ska vara ett tal och inte sträng")
if ålder >=18:
    print("Du är vuxen")
else:
    print("DU är barn")


#Låt användaren mata in ett tal
#Skriv ut största talet
#Skriv ut minsta talet
tal_str=input("Skriv ett antal tal med mellanrum emellan")
lista_str = tal_str.split()#Split ger oss en lista, splittar där vi har mellanslag
print(lista_str)
try:
    tal_lista= [float(x) for x in lista_str]
    störst=max(tal_lista)
    minst=min(tal_lista)
    print(f"Största talet är: {störst} minsta talet är: {minsta} ")
except:
    print("felaktiga tal")


print(tal_lista)
#1
import numpy as np

def distance(p1, p2):
    answer=np.sqrt(p1+p2)
    return answer
print(distance(0.5,0.5))

#2 
def ar_fyrsiffrigt(tal):
    if abs(tal)//1000< 10 and abs(tal)//1000 >=1:
        return True
    else:
        return False

testtal=[100,231,10000, 10001,-1000, 102313]

for t in testtal:
    if ar_fyrsiffrigt(t):
        print(f"{t} är fyrsiffrigt")
    else:
        print(f"{t} är inte fyrsiffrigt")

#3
engångsbiljett=30
månadskort=1825
while True:
    try:
        antal_ggr=int(input("Hur ofta åker du spårvagn? "))
        assert antal_ggr >= 0 and antal_ggr < 70, "Du åker mellan 0 och 70 gånger varje månad"
        break
    except AssertionError as msg:
        print(msg)
    except:
        print("Antal gånger ska vara ett tal och inte sträng")  
if antal_ggr > (1825/30):
    print("Du borde köpa månadskort")
else:
    print("Fortsätt åk med engångsbiljett")

'''