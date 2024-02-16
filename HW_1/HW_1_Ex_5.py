import numpy as np
import matplotlib.pyplot as plt

u = lambda t: 1 if t >= 0 else 0

f = lambda t: np.exp(-t)
f_matrix = [f(t)*u(t) for t in np.linspace(-4, 4, 1000)]
h = lambda t: np.exp(-2*t)
h_matrix = [h(t)*u(t) for t in np.linspace(-4, 4, 1000)]

x = np.linspace(-8, 8, 1999)
convolution = np.convolve(f_matrix, h_matrix)

plt.plot(np.linspace(-4, 4, 1000), f_matrix, label='f(t)')
plt.plot(np.linspace(-4, 4, 1000), h_matrix, label='h(t)')
plt.legend(), plt.savefig('HW_1/Pre-convolution'), plt.show()
plt.plot(x, convolution), plt.savefig('HW_1/Convolution'), plt.show()
