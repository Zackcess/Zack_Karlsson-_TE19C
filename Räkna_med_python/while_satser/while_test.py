'''
print("1+1/2+1/4+1/8+1/2**n")
s=1 #variable ska funkar som räknarvariabel
i=0
while s<=2:
    #n=2**s
print(n)
'''
'''
n = 0 #Räknarvariabel
while n < 10:
    print(n, end=" ")
    n += 1
'''
'''
summa=0
n=1
while n < 10:
    summa = summa + n
    n=n+2
print (f"1+2+3+4+5+6+7+8+9+10 = {summa}")
'''


#How to do random
'''
import random as rnd

rnd.radint (1,10)
'''
'''


import random as rnd
s=rnd.randint (0,100)
h = 0
while h != s:
    h = int(input("Gissa på ett heltal mellan 0-100= "))
    print("Fel, tyvärr")
    if h < s:
        print("För lågt")
    elif h > s:
        print("För högt")
    else:
        print("Rätt svar")
 
'''

'''
#mjölkuppgift -while
#1l mjölk 1 500 000 bakterier i rumstemp. Ökar med 50%/timme i rumstemp. 
# Mjölk surnar när vi har mer än 10 000 000st. 
# Hur många timmar tar det tills mjölken surnar?
import matplotlib.pyplot as plt
import nympy as np

bakterier = 1.5e6
surt = 1e7
faktor = 1.5
timmar = 0

y_bakterier = [bakterier ] #lista som ska hålla bakkteriernas förändring

while bakterier < surt:
    bakterier=faktor*bakterier
    y_bakterier.append(bakterier)
    timmar += 1

x_timmar = np.arange(timmar + 1)#Från 0 till det tal som står minus 1



print(f"Det tar {timmar}h i rumstemp för att mjölken ska surna")
print(f"x={x_timmar} y={y_bakterier}")
print(y_bakterier)

plt.plot(x_timmar, y_bakterier, "*-")
plt.xlabel("timmar (h)")
plt.ylabel("antal bakterier")
plt.title("Bakterietillväxt i mjölk i rumstemp")
plt.show()
'''
#4 skriv ett program som skriver ut värdena på f(x) = x**2 - 3x för -2<=x<= -2 med intervall 0.1. 
# Med while

x = -2
y = 0
while x >= -2 and x<=2:
    y+=(x**2 - 3*x)
    x=x+0.1
    print(f"y={round(y,1)}") 
