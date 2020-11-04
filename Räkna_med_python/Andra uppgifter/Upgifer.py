
#Omvandla kelvin till celsius
Celsius = float(input("Ange en tempratur i Kelvin"))
Kelvin = Celsius-273.15
print(f"{Kelvin}={Celsius}C")

# omvandla celsius till kelvin

Kelvin = float(input("Ange en tempratur i celsius"))
Celsius = Kelvin + 273.15
print(f"{Celsius}={Kelvin}")

#Västtrafik
Gånger= float(input("Hur många gånger åker du med västtrafik?"))
Kostnad = Gånger*301
print(f"{Kostnad}kr kostar dina resor")
if Kostnad > 775: print("Köp ett månadskort")
if Kostnad < 775: print("Köp inte ett månadskort")



