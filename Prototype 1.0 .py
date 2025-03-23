#Importing Modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider as sl

#We're gonna try and plot a relatively easy graph representing the equation x = a*sin(wt+phi)

def wave(a=1, w=2*np.pi, phi=0):
    t = np.linspace(0,2*np.pi, 1000)
    x = a*np.sin(w*t + phi)
    ax.clear()
    ax.plot(t, x)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_xlabel('Time (t)')
    ax.set_ylabel('Displacement (x)')
    ax.grid()
    fig.canvas.draw_idle()

fig, ax = plt.subplots(figsize=(8, 4))
plt.subplots_adjust(bottom=0.5)
wave()


#Adding the sliders

ax_a = plt.axes([0.2, 0.15, 0.65, 0.03])
ax_w = plt.axes([0.2, 0.1, 0.65, 0.03])
ax_phi = plt.axes([0.2, 0.05, 0.65, 0.03])

slider_a = sl(ax_a, 'Amplitude', 0.1, 10, valinit=1)
slider_w = sl(ax_w, 'Frequency', 0.1, 20*np.pi, valinit=2*np.pi)
slider_phi = sl(ax_phi, 'Phase Difference', -2*np.pi, 2*np.pi, valinit=0)

def update(val):
    wave(slider_a.val, slider_w.val, slider_phi.val)

slider_a.on_changed(update)
slider_w.on_changed(update)
slider_phi.on_changed(update)
plt.show()
