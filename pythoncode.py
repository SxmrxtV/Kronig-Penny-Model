import numpy as np
import matplotlib.pyplot as plt
from js import document
import io, base64

def KronigPenney(v, b, a):
    try:
        alpha = 5.421074 * 10**9
        p = 4.44752 * v * b * 10**28
        alpha_a_range = np.linspace(-10 * a * alpha, 10 * a * alpha, 1000)
        y = p * (np.sin(alpha_a_range) / alpha_a_range) + np.cos(alpha_a_range)

        fig, ax = plt.subplots(figsize=(6, 6))
        ax.plot(alpha_a_range, y)
        ax.axhline(0, color='black', linewidth=1.5)
        ax.axvline(0, color='black', linewidth=1.5)
        ax.set_xlabel(r'$\alpha a$')
        ax.set_ylabel(r'$\frac{p\sin(\alpha a)}{\alpha a} + \cos(\alpha a)$')
        ax.fill_between(alpha_a_range, -1, 1, where=(np.abs(y) <= 1), color='lightblue', alpha=0.5)
        ax.grid()

        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)

        img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        document.getElementById("plot").src = 'data:image/png;base64,' + img_base64

        plt.close(fig)
    except Exception as e:
        print("Error in KronigPenney:", e)

KronigPenney(1e-14, 1e-14, 5.43e-10)

def update_plot(v, b, a):
    KronigPenney(v, b, a)
