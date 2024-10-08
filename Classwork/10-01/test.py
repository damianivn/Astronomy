import numpy as np

h = 6.62607015*(10**-34)
c = 299792458
k = 1.380649*(10**-23)

T1 = 1000
l = 2.9*(10**-6)


# print(((8*np.pi*h*c)/(l**5))*(1/((np.e**((h*c)/(k*T1*l)))-1)))

lm = np.linspace(0, 15, 0.0001)
print(lm)
