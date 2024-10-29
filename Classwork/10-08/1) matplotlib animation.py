import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


xdata = np.linspace(0, 2*np.pi, 100)
ydata = np.sin(xdata)

# set up a figure
fig, ax = plt.subplots()
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-2, 2)

# plot the data and return the line object
ln, = plt.plot(xdata, ydata, "r-")


def update(frame):
    ydata = np.sin(xdata+frame)
    ln.set_data(xdata, ydata)
    return ln,


# create an animation by passing the figure, the function that will get updated,
# and the argument to the function (frames)
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128), interval=10,
                    blit=True)
plt.show()
# ani.save("wave.mp4")
