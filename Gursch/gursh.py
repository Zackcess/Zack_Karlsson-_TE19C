import random as rnd

cardfaces =[]
färger =["Hjärter", "Ruter", "Klöver", "Spader"]
royals =["J", "Q", "K", "A"]
deck = []

#2-10
for i in range (2,11):
    cardfaces.append(str(i))

for j in range (4):
    cardfaces.append(royals[j])


for k in range (4):
    for l in range(13):
        card= cardfaces[l],"av", färger[k]
        deck.append(card)


#shuffle
rnd.shuffle(deck)
for m in range(52):
    print(deck[m]) 

spelare_1=[]
for z in range(5):   
    spelare_1.append(deck.pop())


print(spelare_1, end=" ")