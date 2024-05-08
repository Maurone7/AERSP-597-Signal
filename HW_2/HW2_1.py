import numpy as np 
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

g=lambda t: 51*np.cos(2*np.pi*5*t) + 5*np.cos(2*np.pi*17*t) + 21*np.cos(2*np.pi*51*t)
t=np.linspace(0,4,1000)
plt.plot(t,g(t))
plt.savefig('HW_2/HW2_1.png')
plt.clf()

Np = 2048
fs = 500
Tf = Np/fs
dt = 1/fs
t = np.arange(0,Tf,dt)
Gs = fft(g(t),Np)
f = fftfreq(Np,dt)
plt.plot(f,abs(Gs))
plt.title('FFT of g(t)')
plt.savefig('HW_2/HW2_1frequency.png')
plt.clf()
