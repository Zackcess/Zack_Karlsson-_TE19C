#1
namn=input("Skriv ditt namn: ")
print(f"Ditt namn innehåller {len(namn)} st bokstäver")

#2
ord=("En bild säger mer än tusen ord, en matemstisk formel säger mer än tusen bilder")
print(f"Meningen innehåller {len(ord)} ord")

#3a
ord=input("Skriv ett ord så får du veta om det är ett palindrom: ")
ord_bak = ord[::-1]
if ord==ord_bak:
    print("Ordet är ett palindrom!")
else:
    print("Inget palindrom")
#3b
ord=input("Skriv ett ord så får du veta om det är ett palindrom: ")
ord_bak = ord[::-1]
if ord==ord_bak:
    print("Ordet är ett palindrom!")
else:
    print("Inget palindrom")