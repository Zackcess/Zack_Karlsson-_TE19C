#st
'''
import matplotlib.pyplot as plt
import numpy as np

m=[0,10,20,30,40,50,60,70,80,90,100]#antal meter
t=[0,1.83,2.87,3.78,4.65,5.5,6.32,7.14,7.96,8.79,9.69]#mätvärden tid

plt.plot(t,m,"*-")
plt.xlabel("tid (s)")
plt.ylabel("sträcka (m)")
plt.title("S/t")
plt.show()
'''
#vt
import matplotlib.pyplot as plt
import numpy as np

m=[0,10,20,30,40,50,60,70,80,90,100]#antal meter
t=[0,1.83,2.87,3.78,4.65,5.5,6.32,7.14,7.96,8.79,9.69]#mätvärden tid
v=[0]#tomlista

for i in range(1, len(m)):
    v_i = ((m[i]-m[i-1])/(t[i]-t[i-1]))
    v.append(v_i) #lägger v_i till listan


plt.plot(t, v, '*-')
plt.title("Usain bolt 100m - v-t graf")
plt.xlabel("Tiden i sekunder")
plt.ylabel("Hastigheten i m/s")
plt.grid()
plt.show()