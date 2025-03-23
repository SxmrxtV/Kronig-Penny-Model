#importing
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider as sl

#Generating the static graph

def KronigPenney(v=10**(-14), b=10**(-14), a=0.543*10**(-9)):
    alpha = 5.421074 * 10**(9)
    p = 4.44752 * v * b * 10**(28)
    alpha_a_range = np.linspace(-10*a*alpha, 10*a*alpha, 1000)
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

#v_0 = 10**(-14)
#b_0 = 10**(-14)

slider_v = sl(ax_v, 'V (Height of Potential Barrier)', 10**(-16), 10**(-13), valinit=10**(-14))
slider_b = sl(ax_b, 'B (Width of Potential Barrier)', 10**(-16), 10**(-13), valinit=10**(-14))
slider_a = sl(ax_a, 'a (Lattice Constant)', 0.543*10**(-10), 0.543*10**(-8), valinit=0.543* 10**(-9))

def update(val):
    KronigPenney(slider_v.val, slider_b.val, slider_a.val)

slider_v.on_changed(update)
slider_b.on_changed(update)
slider_a.on_changed(update)
plt.show()