#Goal 1

#Need to import, math, numpy, and matplotlib
import math
import numpy as np
import matplotlib.pyplot as plt

#Same starting as the Matlab code
sampling_rate = 500

#Had to use float
time = np.arange(0,5,float(1/sampling_rate))
　
#Same as Matlab　
freq_1 = 60
freq_2 = 35
freq_3 = 10

#Used a combination of np and math to make this translate
signal = ((np.sin(2*math.pi*freq_1*time)+np.sin(2*math.pi*freq_2*time)+np.sin(2*math.pi*freq_3*time))/3)

#Needed to make this into an int for dF　
N = int(signal.size)
　
#Kept the Fourier Transformation part simple　
signal_fft = np.fft.fft(signal, N)
　
Nyquist = sampling_rate/2

dF = float(sampling_rate/N)

#Switched around the order to satisfy python requirements
f = np.arange(0,Nyquist -dF, (Nyquist/N))

#Translated this simply as well
inds = np.nonzero(f<75)
frequencies = f[inds]
signal_fft = signal_fft[inds]

#Plots graph 1 which is unfiltered signal
plt.subplot(211)
plt.plot(time, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Unfiltered Signal')
plt.show()

#Plots graph 2 which is Spectrum
plt.subplot(212)
plt.bar(frequencies,signal_fft)
plt.title('Spectrum of Unfiltered Signal')
plt.xlabel('frequency (Hz)')
plt.ylabel('power')
plt.show()
