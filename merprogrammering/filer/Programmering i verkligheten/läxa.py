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
'''
#3
pokemons=[]
pokedex={}
with open("pokemonlista.txt", "r") as f1:
    for rad in f1:
        rad=rad.replace("\n", "")
        pokemons.append(rad)
for i in range (10):
    index=pokemons[rad]
print(index)

'''

