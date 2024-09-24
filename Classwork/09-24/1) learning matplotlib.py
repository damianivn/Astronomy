import numpy as np
import matplotlib.pyplot as plt

#define an array of 100 numbers from 0 to 2
x = np.linspace(0, 2, 100)

#calculate the value of y for three different functions
y1 = x
y2 = x**2
y3 = x**3

#plot the first line
plt.plot(x, y1, label="linear")

#plot the second line
plt.plot(x, y2, label="quadratic")

#plot the third line
plt.plot(x, y3, label="cubic")

#add axis labels
plt.xlabel("x label")
plt.ylabel("y label")

#add a legend
plt.legend()
plt.show()