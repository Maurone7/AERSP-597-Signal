import numpy as np 
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import sympy as sym

'''
f (t) = 51 cos(2π5t) + 5 cos(2π17t) + 21 cos(2π51t)
a) Pick the sampling frequency as 5 times the Nyquist frequency. Choose an appropriate length of the
signal and obtain the FFT of f (t).
b) Differentiate the function f (t) to obtain f ′(t) and take its Fourier Transform
c) Now, obtain the derivative of this function (f (t)) by performing the appropriate operations in the
frequenct domain. Compare this with the FFT in part (b)
d) Reconstruct the f ′(t) by taking the inverse fourier transform and compare with f ′(t). Plot the errors
'''

f = lambda t: 51*np.cos(2*np.pi*5*t) + 5*np.cos(2*np.pi*17*t) + 21*np.cos(2*np.pi*51*t)
fs = 5*51
Np = 2048
T = Np/fs
dt = 1/fs
t = np.arange(0,T,dt)

Fs = fft(f(t),Np)
f = fftfreq(Np,dt)
plt.plot(f,abs(Fs))
plt.title('FFT of f(t)')
plt.savefig('HW_2/HW2_3a.png')
plt.clf()


t = sym.symbols('t')
f = 51*sym.cos(2*sym.pi*5*t) + 5*sym.cos(2*sym.pi*17*t) + 21*sym.cos(2*sym.pi*51*t)
f_prime = sym.diff(f,t)
f_prime = sym.utilities.lambdify(t,f_prime)
t = np.arange(0,T,dt)
F_prime = fft(f_prime(t),Np)
f = fftfreq(Np,dt)
plt.plot(f,abs(F_prime))
plt.title('FFT of f_prime')
plt.savefig('HW_2/HW2_3c.png')
#clear plot
plt.clf()

# do inverse transform on F_prime
f_prime_inverse_F = np.fft.ifft(F_prime)
plt.plot(t,f_prime_inverse_F, label='f_prime_inverse_F')
plt.plot(t,f_prime(t), label='f_prime')
plt.title('Inverse FFT of f_prime vs f_prime')
plt.legend()
plt.savefig('HW_2/HW2_3d.png')
plt.clf()
