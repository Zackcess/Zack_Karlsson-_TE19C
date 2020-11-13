'''
förnamn="Kokchun"
efternamn="Giang"

namn=förnamn + " " + efternamn
ålder="17"
adress="Kronhusgatan 9"
telefon=112

personuppg="Namn: " + namn + "\n" + "Ålder: " + ålder + "\n" + "Telefon: "+str(telefon)

print(personuppg)
'''
#indexera
'''
alfabet="abcdefghijklmnopqrstuvwxyzåäö"
print:(f"Antal bokstäver: {len(alfabet)}")
print(f"bokstav på index 0: {alfabet[0]}")
print(f"bokstav på index 28: {alfabet[28]}")
'''
favoritämnen = "matematik programmering teknik webbutveckling fysik"
favoritmat= "lasagne,korv,grönsaker,kebab,ris"
print(favoritämnen)
#separerar en sträng
favoritämnen = favoritämnen.split()
favoritmat = favoritmat.split(",")
print(favoritämnen)
print(favoritmat)

for mat in favoritmat:
    print(f"Jag älskar att äta {mat}")