#1
'''
poäng=0
kurser= {
    "matte4": 100,
    "fysik":150,
    "engelska6":100,
    "webb":100,
    "svenska":100,
    "datorvetenskap": 100,
    "idrott":100,
}

for key,value in kurser.items():
    poäng += value
print(f"Jag läser antal {poäng}")
#2
import random as rnd
resultat={}
randomtal=[]
for i in range(1,7):
    resultat[f"{i}"] = 0
for i in range(100000):
    kast=rnd.randint(1,6)
    randomtal.append(kast)
for j in range(1,7):
    resultat[f"{j}"]=randomtal.count(j)
print(resultat)

#for-sats för att generera key-value par
siffror={}
import random as rnd

for i in range(10):
    slumptal=rnd.randint(1,10)
    siffor[f"{i}"]=slumptal

print(siffror)

#3 
#Index är både nummer och egenskap, medans pokemon är namnet på pokemonen
pokemons=[]
pokedex={}
index=[]
with open("pokemonlista.txt", "r") as f1:
    for rad in f1:
        rad=rad.replace("\n", "")
        pokemons.append(rad)
#pokemondelen mst använda list comprehension
new_items = [item for item in pokemons if not item.isdigit()]

print (new_items)
#index delen
for n in range(150):
    for i in pokemons:
        index.append(pokemons)


print (new_items)
'''
#4
morsetecken={}
#öppnar filen morse.txt
with open("morse.txt", "r") as f1:
    #går igenom alla rader av filen och delar upp det i key och value. key=bokstav. Value=morsekoden
    for rad in f1:
        bokstav=rad[:1]
        kod=rad[3:]
        morsetecken[bokstav]=kod
#funktion som översätter
def översätt(text):
    kodad=[]
    #går igenom varje bokstav i ordet och kollar om det finns i dict
    for bokstav in user_text:
        
        if bokstav in morsetecken:
            print(bokstav)
            #hittar value till key och lägger det i lista
            kodad.append(morsetecken[bokstav])
            #det är något konstigt så att jag får /n
            fullt_ord=[bokstav[:-1] for bokstav in kodad]
    print(fullt_ord)
user_text= input("Vilket ord vill du får transelterat???").upper() #
översätt(user_text)
