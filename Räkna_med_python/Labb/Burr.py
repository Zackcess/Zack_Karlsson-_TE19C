#a Låt programmet skriva ut tal från 1-100
for i in range (1,101):#Den här funktionen(range) ger dig alla tal mellan 1 och 100, där den av standard ökar med 1.
    print(f"{i}", end=" ")#Skriver ut variabeln "i"  och "end" gör så att det hamnar på en rad, med mellanrum.

#b För varje multipel av 5 ska programmet skriva "burr"
for i in range (1,101):
    if i%5 ==0: #Modulus ger resten av det tal man dividerar med, så om den är 0 är det en multipel.
        print("Burr")
    else:
        print(i)

#C Låt andvändaren mata in ett tal vars multiplar blir burr
b=int(input("Skriv in ett tal")) 
for i in range (1,101):
    if i%b == 0:
        print("Burr")
    else:
        print(i)

#E Designa ett program som låter användaren välja start, slut, multipel för "burr" och multipel för birr. 
# Programmet ska räkna upp antalet "burr", "birr", och "burr" "birr"
print("Ange ett intervall")
start=int(input("Startnummer= "))
slut=int(input("Slutnummer= "))
bi=int(input("Ange siffra i intervallet= "))
b=int(input("Och en till siffra= "))
burrcount=0
birrcount=0
for i in range (start,slut):
    if i%b == 0 and i%bi ==0:
        print("Burr, Birr")
        burrcount +=1
        birrcount +=1
    elif i%b == 0:
        print("Burr")
        burrcount +=1
    elif i%bi ==0:
        print("Birr")
        birrcount +=1
    else:
        print(i)
print(f"Antalet burr: {burrcount} och antalet birr: {birrcount}")
#f Man skulle kunna addera några till namn, så att det blir burr, birr och barr med flera. Det hade medfört att det blev ännu svårare att klara av spelet. 
print("Ange ett intervall")
start=int(input("Startnummer= "))
slut=int(input("Slutnummer= "))
print("Ange tre nummer i intervallet")
bi=int(input("Nummer= "))
b=int(input("Nummer= "))
ba=int(input("Nummer= "))
burrcount=0
birrcount=0
barrcount=0
for i in range (start,slut):
    if i%b == 0 and i%bi ==0 and i%ba ==0:
        print("Burr, Birr, Barr")
        burrcount +=1
        birrcount +=1
        barrcount +=1
    elif i%b == 0:
        print("Burr")
        burrcount +=1
    elif i%bi ==0:
        print("Birr")
        birrcount +=1
    elif i%ba==0:
        print("Barr")
        barrcount=+1
    else:
        print(i)
print(f"Antalet burr: {burrcount}, antalet birr: {birrcount} och antalet barr: {burrcount}")