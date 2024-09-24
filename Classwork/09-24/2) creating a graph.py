import numpy as np
import matplotlib.pyplot as plt

#create an array of unit circle values

x = np.linspace(0, 2*np.pi, 1000)

#calculate the y-values for various trig functions

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

#plot axis lines and guiding lines
plt.axhline(y=0, color="black", label="midline", linestyle = 'dashed')
plt.axhline(y=1, color="black", label="max value", linestyle = 'dashed')
plt.axhline(y=-1, color="black", label="min value", linestyle = 'dashed')
plt.axvline(x = 0, color = "lightgray", linestyle = 'dashed')
plt.axvline(x = np.pi/2, color = 'lightgray', linestyle = 'dashed')
plt.axvline(x = 2*np.pi/2, color = "lightgray", linestyle = 'dashed')
plt.axvline(x = 3*np.pi/2, color = "lightgray", linestyle = 'dashed')
plt.axvline(x = 4*np.pi/2, color = "lightgray", linestyle = 'dashed')

#plot the lines
plt.plot(x, y1, label="sine")
plt.plot(x, y2, label="cosine")
#plt.plot(x, y3, label="tangent")

#add axis labels
plt.xlabel("x label")
plt.ylabel("y label")

#add a legend
plt.legend()
plt.show()