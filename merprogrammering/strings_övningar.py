
#1
namn=input("Skriv ditt namn: ")
print(f"Ditt namn innehåller {len(namn)} st bokstäver")

#2
mening=("En bild säger mer än tusen ord, en matemstisk formel säger mer än tusen bilder")
mening=mening.split()
print(f"Meningen innehåller {len(mening)} ord")

#3a
ord=input("Skriv ett ord så får du veta om det är ett palindrom: ")
ord=ord.upper()
ord_bak = ord[::-1]
if ord==ord_bak:
    print("Ordet är ett palindrom!")
else:
    print("Inget palindrom")

#3b
mening=input("Skriv en mening så får du veta om det är ett palindrom: ")
palindrom=mening.split(" ")
palindrom=mening.upper()
palindrom = mening[::-1]
if mening==palindrom:
    print("Meningen är ett palindrom!")
else:
    print("Inget palindrom")

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
#5
