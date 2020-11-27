#1a
kast=[1,2,3,4,5,6]
kastningar =[x for x in kast]
print(f"{kastningar}")
#1b
print(f"{kastningar[::-1]}")

#2 
x=0
tal= [x for x in range(-10,11)]
kvadrater=[x**2 for x in tal]
print(kvadrater)

#3 
tabell=[]
for i in range(9):
    rad=[x for x in range(9)]#En rad av gånger tabellen
    tabell.append(rad)
    for j in range(1,9):
        print(f"{tabell[i][j]:3}", end=" ")
    print()
print()
print(f"tabell[3]: {tabell[3]}")
print(f"tabell[3][3]: {tabell[3][3]}")
