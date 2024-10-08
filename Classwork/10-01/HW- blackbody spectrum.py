import numpy as np
import matplotlib.pyplot as plt

# some important constants
h = 6.62607015*(10**-34)
c = 299792458
k = 1.380649*(10**-23)

# define an array of 100 numbers from 0 to 2
lm = np.linspace(0, 3, 1000)
l = np.linspace(0, 0.000003, 1000)


def blackbody(T):
    return ((((8*np.pi*h*c)/(l**5))*(1/((np.e**((h*c)/(k*T*l)))-1))))


# calculate the value of y for three different functions
y1 = blackbody(4000)
y2 = blackbody(4500)
y3 = blackbody(5000)

# plot the blackbody curves
plt.plot(lm, y1, label="4000K")
plt.plot(lm, y2, label="4500K")
plt.plot(lm, y3, label="5000K")

# add axis labels
plt.xlabel("Wavelength (micrometers)")
plt.ylabel("B (J/m^4)")

# add a legend
plt.legend()
plt.show()
