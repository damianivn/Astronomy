import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# some important constants
h = 6.62607015*(10**-34)
c = 299792458
k = 1.380649*(10**-23)

# define an array of 100 numbers from 0 to 2
lm = np.linspace(0, 3, 1000)
l = np.linspace(0, 0.000003, 1000)


def blackbody(T):
    return ((((8*np.pi*h*c)/(l**5))*(1/((np.e**((h*c)/(k*T*l)))-1))))


xdata = 4000
ydata = blackbody(xdata)

# plot the data and return the line object
fig, ax = plt.subplots()
ln, = plt.plot(lm, ydata, "r-", label=xdata)

# set up a figure


def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(0, 1500000)
    return ln


legend = plt.legend(loc=1)  # Define legend objects


def update(frame):
    ln.set_data(lm, blackbody(xdata+frame))
    # Update label each at frame
    legend.get_texts()[0].set_text(str(round(xdata+frame))+'K')
    return ln,


# create an animation by passing the figure, the function that will get updated,
# and the argument to the function (frames)
ani = FuncAnimation(fig, update, frames=np.linspace(
    0, 2000, 5), init_func=init, interval=1000)

# add axis labels
plt.xlabel("Wavelength (micrometers)")
plt.ylabel("B (J/m^4)")

# show the plot
plt.show()

# ani.save("wave.mp4")
