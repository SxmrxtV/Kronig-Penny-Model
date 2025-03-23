#importing
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider as sl

#Generating the static graph

def KronigPenney(v=1, b=1, a=1):
    alpha_a  = 2.94364
    p = 4.44752 * v * b
    alpha_a_range = np.linspace(-29.4364, 29.4364, 1000)
    y = p*(np.sin(alpha_a_range)/alpha_a_range) + np.cos(alpha_a_range)
    ax.clear()
    ax.plot(alpha_a_range, y)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_xlabel(r'$\alpha a$')
    ax.set_ylabel(r'$\frac{p\sin(\alpha a)}{\alpha a} + \cos(\alpha a)$')
    ax.grid()
    fig.canvas.draw_idle()

fig, ax = plt.subplots(figsize=(6, 6))
plt.subplots_adjust(bottom=0.5)
KronigPenney()


#Sliders
ax_v=plt.axes([0.2, 0.15, 0.65, 0.03])
ax_b=plt.axes([0.2, 0.1, 0.65, 0.03])
ax_a=plt.axes([0.2, 0.05, 0.65, 0.03])

slider_v = sl(ax_v, 'V (Height of Potential Barrier)', 0.1, 10, valinit=1)
slider_b = sl(ax_b, 'B (Width of Potential Barrier)', 0.1, 10, valinit=1)

def update(val):
    KronigPenney(slider_v.val, slider_b.val)

slider_v.on_changed(update)
slider_b.on_changed(update)
plt.show()