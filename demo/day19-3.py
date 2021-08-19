import numpy as np
import matplotlib.pyplot as plt
x = np.random.rand(10,10)
wave = np.cos(x)
plt.plot(wave)
plt.show()
transformed = np.fft.fft2(wave)
plt.plot(transformed)
plt.show()

plt.plot(np.fft.ifft2(transformed))
plt.show()