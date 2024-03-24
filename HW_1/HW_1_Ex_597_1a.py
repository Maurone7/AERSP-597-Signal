import numpy as np; import matplotlib.pyplot as plt

u = lambda t: 1 if t >= 0 else 0

f = lambda t: 1 if t >= -1 and t<= 1 else 0
f_matrix = [f(t)*u(t) for t in np.linspace(-4, 4, 1000)]

h = lambda t: 1/3 *t if t >=0 and t <= 3 else 0
h_matrix = [h(t)*u(t) for t in np.linspace(-4, 4, 1000)]

x = np.linspace(-8, 8, 1999)
plt.plot(np.linspace(-4, 4, 1000), f_matrix, label='f(t)')
plt.plot(np.linspace(-4, 4, 1000), h_matrix, label='h(t)')
plt.legend(), plt.show()

convolution = np.convolve(f_matrix, h_matrix)
plt.plot(x, convolution), plt.show()