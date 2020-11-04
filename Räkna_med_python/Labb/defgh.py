#d Stimulation av många punkter mellan -1 och 1 för x- och y-kordinater(Random.uniform)

import random as rnd #importerar random opperatorn så vi kan få slumptal
for i in range(10): #Så att det blir stimulation av flera punkter (10)
    x=rnd.uniform(-1,1)#Beskriver det slumpmässiga x-värdet till -1
    y=rnd.uniform(-1,1)#Beskrivet det slumpmässiga y-värdet till 1
    print(f"({x:.2f},{y:.2f})")#Skriver ut punkterna

#e
import random as rnd #importerar random opperatorn så vi kan få slumptal
import math#Gör så att man kan få pi
circle=math.pi*1**2#cirkelns area
square=2*2
h=0
for i in range(100000): #Så att det blir stimulation av flera punkter (10)
    x=rnd.uniform(-1,1)#Beskriver det slumpmässiga x-värdet till -1
    y=rnd.uniform(-1,1)#Beskrivet det slumpmässiga y-värdet till 1
    c=math.sqrt(y**2+x**2)#Hypotenusa
    if c < 1:#De är innanför
        h+=1
#f 
print(f"{(h/100000)*4}")#Det rör sig mot pi, eftersom 

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

