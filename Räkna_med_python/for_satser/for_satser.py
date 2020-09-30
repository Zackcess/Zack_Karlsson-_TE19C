#Skriv ut alla tal 1-100

#for i in range(1,101):
    #print(i, end=" ")


for j in range(100,49,-1):
    print(j, end=" ")

print("\n")

for i in range(50,101):
     print(150-i,end=" ")

print("\n")

s=0
for i in range(11):
    s += i
print(f"1+2+3...+8+9+10 = {s}")

#1 programeringshäfte #a
for i in range(1,11):
    print(i)
#b
for i in range(-10,11):
    print(i,end=" ")
#c
for i in range(1,11):
    print(11-i,end=" ")
#2 Denna var svår
for n in range(1,101): #n radar upp alla tal mellan 1-100

    for a in range(2,n): #för a gäller det att den är emellan 2 0ch 1-100 
        if (n%a == 0):  #om n dividerat med a blir 0 är det inte ett primtal annars är det ett
            break
    else:
        print(n,end=" ")
#3
s=0
for i in range (101):
    s+= i
print(f"1+2+3+4+5....+99+100= {s}")
#4
s=0
for i in range (100):
    s+= i
print(f"1+2+3+4+5....+99+100= {s}")
#5 a
for i in range(11):
    i*=5
    print(i)

#kockhun code along
#Fuska på nationella prov ma3c
#Skapar en tom lista
import matplotlib.pyplot as plt
a_vals = []
for x in range (1,100):
    a = round(5*(2+4/x),2)
    a_vals.append(a) #Sparar a värdena i en lista

print(a_vals)
#resultatet blir tio
plt.show(a_vals)

#b
t = int(input("Skriv en multiplikationstabell: "))
b= int(input("start för tabell: "))
e= int( input("slut för tabell: "))
for i in range(b,e):
    i*=t
    print(i)

#c
for i in range(1,11):
    for j in range(1,11):
        print (f"{i*j}", end= "\t")
    print("\n")

#6
