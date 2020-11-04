'''
import matplotlib.pyplot as plt
y1 = 0.4
x1=0.9
x2=-0.5
y2=-0.3
plt.plot(x1,y1,'*r')
plt.plot(x2, y2,'*g')
plt.show()
'''
'''
#g
import matplotlib.pyplot as plt
import random as rnd #importerar random opperatorn så vi kan få slumptal
import math#Gör så att man kan få pi
circle=math.pi*1**2#cirkelns area
square=2*2
h=0
for i in range(100000): #Så att det blir stimulation av flera punkter (10)
    x=rnd.uniform(-1,1)#Beskriver det slumpmässiga x-värdet till -1
    y=rnd.uniform(-1,1)#Beskrivet det slumpmässiga y-värdet till 1
    c=math.sqrt(y**2+x**2)#Hypotenusa
    if c > 1: #utanför          
        plt.plot(x,y,'*r')
    else:
        plt.plot(x,y,'*g')

plt.show()
'''
'''
#h
import matplotlib.pyplot as plt
import random as rnd #importerar random opperatorn så vi kan få slumptal
import math#Gör så att man kan få pi
circle=math.pi*1**2#cirkelns area
square=2*2
h=0
for i in range(100): #Så att det blir stimulation av flera punkter (10)
    x=rnd.uniform(-1,1)#Beskriver det slumpmässiga x-värdet till -1
    y=rnd.uniform(-1,1)#Beskrivet det slumpmässiga y-värdet till 1
    c=math.sqrt(y**2+x**2)#Hypotenusa
    if c > 10: #Desto störreradie2         
        plt.plot(x,y,'*r')
    else:
        plt.plot(x,y,'*g')
plt.show()
'''
'''
#b För varje multipel av 5 ska programmet skriva "burr"
for i in range (1,101):
    if i%5 ==0:
        print("Burr")
    else:
        print(i)
'''
'''
#C Låt andvändaren mata in ett tal vars multiplar blir burr
b=int(input("Skriv in ett tal"))
for i in range (1,101):
    if i%b == 0:
        print("Burr")
    else:
        print(i)
'''
'''
#D Låt användaren även mata in ett tal vars multiplar blir "birr"
bi=int(input("Skriv in ett tal= "))
b=int(input("Ett till tal= "))
for i in range (1,101):
    if i%b == 0:
        print("Burr")
    elif i%bi ==0:
        print("Birr")
    else:
        print(i)
'''
#E Designa ett program som låter användaren välja start, slut, multipel för "burr" och multipel för birr. 
# Programmet ska räkna upp antalet "burr", "birr", och "burr" "birr"
print("Ange ett intervall")
start=int(input("Startnummer= "))
slut=int(input("Slutnummer= "))
bi=int(input("Ange siffra i intervallet= "))
b=int(input("Och en till siffra= "))
for i in range (start,slut):
    if i%b == 0 and i%bi ==0:
        print("Burr, Birr")
    elif i%b == 0:
        print("Burr")
    elif i%bi ==0:
        print("Birr")
    else:
        print(i)
