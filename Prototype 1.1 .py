import numpy as np
import matplotlib.pyplot as plt

alpha_a  = 2.94364
p = 4.44752
alpha_a_range = np.linspace(-29.4364, 29.4364, 1000)
y = p*(np.sin(alpha_a_range)/alpha_a_range) + np.cos(alpha_a_range)
plt.figure(figsize=(6,6))
plt.xlabel(r'$\alpha a$')
plt.ylabel(r'$\frac{p\sin(\alpha a)}{\alpha a} + \cos(\alpha a)$')
plt.plot(alpha_a_range, y)
plt.grid()
plt.tight_layout()
plt.show()