import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft


class EasyExample:
    def sample_function(self):
        self.sr = 10 #sampling rate
        self.ts = 1.0/self.sr #timestep
        self.t = np.arange(0,1,self.ts)
        self.x = np.sin(20 * self.t)

    def fourier_transform(self):
        self.X = fft(self.x)
        #N = len(self.X)
        #n = np.arange(N)
        #T = N/self.sr
        #freq = n/T

    def plotting(self):
        plt.plot(self.t, self.x)
        plt.plot(self.t, ifft(self.X))
        plt.show()

if __name__ == '__main__':
    obj = EasyExample()
    obj.sample_function()
    obj.fourier_transform()
    obj.plotting()
