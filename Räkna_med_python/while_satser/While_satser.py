#1
print("1+2+3+4+5...+99+100")
s=0
n=0
while s<100:
    s+=1 
    n += s
print(n)

#2
s=1
n=0
while s<100:
    n += s
    s+=2 
print(f"1+2+5+7..+99+100 = {n}")
#3
s=0  #variabl ska funkar som räknarvariabel
n = 0
while n<10:
    s += 2**(-n)
    n = n+1
print(f"talet är={s}")

#5
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
