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