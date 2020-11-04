#a Låt programmet skriva ut tal från 1-100
for i in range (1,101):
    print(f"{i}", end=" ")

#b För varje multipel av 5 ska programmet skriva "burr"
for i in range (1,101):
    if i%5 ==0:
        print("Burr")
    else:
        print(i)

#C Låt andvändaren mata in ett tal vars multiplar blir burr
b=int(input("Skriv in ett tal"))
for i in range (1,101):
    if i%b == 0:
        print("Burr")
    else:
        print(i)

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