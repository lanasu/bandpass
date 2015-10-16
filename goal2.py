#This is based on the example code that scipy gives, and uses N and f from goal 1. 
#So this wouldn't run on its own here because N and f are from goal1, but I just wanted to include this.
#So you'd get an idea of what I saw when I was researching bandstop filter on scipy. 

from scipy import signal
import matplotlib.pyplot as plt

b, a = scipy.signal.butter(N, f, btype='bandstop', analog=False, output='ba')
w, h = signal.freqs(b, a)
plt.plot(w, h)
plt.title('Bandstop filter')
plt.xlabel('Time')
plt.ylabel('Amplitude')

#cutoff
plt.axvline(60, color='blue') 
plt.show()
