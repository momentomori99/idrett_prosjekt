import numpy as np
import matplotlib.pyplot as plt

class Runner:
    def __init__(self):
        self.height_mc = 2 #height of the mass center [m]
        self.mass = 70 #The mass of the runner
        self.g = -9.81 #gravational acc. [m/s^2]
        self.g_array = np.array([0, self.g])
        self.N = 1000 #number of steps
        self.T = 15 #seconds
        self.dt = self.T/self.N #timestep
        self.strike = np.array([0, 100]) #the force exceeded by the legs while running upwards

    def initial_values(self):
        self.t = np.zeros(self.N)
        self.v = np.zeros([self.N,2])
        self.p = np.zeros([self.N,2])
        self.K_e = np.zeros(self.N) #kinetic energy
        self.P_e = np.zeros(self.N) #potential energy
        self.t[0] = 0
        self.v[0] = np.array([0.1,0])
        self.p[0] = np.array([0, self.height_mc])


    def loop(self):
        for i in range(self.N-1):
            if (3.5 < self.t[i] < 4) or (7.5 < self.t[i] < 8):
                a = self.g_array + self.strike
            else:
                a = self.g_array
            self.p[i + 1] =self. p[i] + self.v[i]*self.dt
            self.v[i + 1] = self.v[i] + a * self.dt
            self.t[i + 1] = self.t[i] + self.dt

    def calculate_energy(self):
        self.K_e = 0.5 * self.mass * np.linalg.norm(self.v, axis=1) ** 2
        self.P_e = self.mass * self.g * self.p[:, 1]

    def visualization(self):
        plt.plot(self.p[:,0], self.p[:,1])
        plt.grid(1)
        plt.show()

        plt.plot(self.t, self.K_e, label="kinetic")
        plt.plot(self.t, self.P_e, label="potential")
        plt.grid(1)
        plt.legend()
        plt.show()




if __name__ == '__main__':
    obj = Runner()
    obj.initial_values()
    obj.loop()
    obj.calculate_energy()
    obj.visualization()
