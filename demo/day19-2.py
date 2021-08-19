import wave

import numpy as np
import matplotlib.pyplot as plt
# 包含50个点的余弦波信号 wave = np.cos(x)
x = np.linspace(0, 2 * np.pi,30)
wave = np.cos(x)

# 傅里叶变换
transformed = np.fft.fft(wave)

# 使用matplotlib绘制变换后的信号 plt.show()
plt.plot(np.fft.ifft(transformed))
shifted = np.fft.fftshift(transformed)
plt.plot(np.fft.ifft(shifted))
plt.plot(shifted)
plt.show()
