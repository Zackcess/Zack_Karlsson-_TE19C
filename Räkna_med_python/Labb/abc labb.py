#Simulering av piltavla
#a beräkna avståndet från origo till (x,y) = (0.5;0.5),,,pytagorasats a**2+b**2=c**2
import numpy as np#Den här importen medför att vi kan använda matemtiska funktioner
x=0.5
y=0.5
s = np.sqrt((0.5**2)+(0.5**2))#Här tar vi hjälp av "numpy" när vi tar roten ur
print(f"sträcka i l.e. från origo till (0.5;0.5) = {s:.2f}")#"2f medför att vi får två decimaler"

#b Beräkna avståndet från origo till (x,y) = (1;1),,,Pytagorasats a**2+b**2=c**2
x=1
y=1
s = np.sqrt((1**2)+(1**2))
print(f"sträcka i l.e. från origo till (1;1) = {s:.2f}")

#c Beräkna avståndet från origo till (x,y)=(0.5;-0.5),,,Pytagorasats a**2+b**2=c**2
x=0.5
y=-0.5
s= np.sqrt((0.5**2)+(-0.5**2))
print(f"sträcka i l.e. från origo till (0.5;-0.5) = {s:.2f}")




