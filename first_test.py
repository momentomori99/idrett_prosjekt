import numpy as np
import matplotlib.pyplot as plt

height_mc = 2 #height of the mass center [m]
mass = 70 #The mass of the runner
g = -9.81 #gravational acc. [m/s^2]
g_array = np.array([0, g])
N = 1000 #number of steps
T = 15 #seconds
dt = T/N #timestep
strike = np.array([0, 100]) #the force exceeded by the legs while running upwards

t = np.zeros(N)
v = np.zeros([N,2])
p = np.zeros([N,2])



#defining initial values:
t[0] = 0
v[0] = np.array([0.1,0])
p[0] = np.array([0, height_mc])


for i in range(N-1):
    if (3.5 < t[i] < 4) or (7.5 < t[i] < 8):
        a = g_array + strike
    else:
        a = g_array
    p[i + 1] = p[i] + v[i]*dt
    v[i + 1] = v[i] + a * dt
    t[i + 1] = t[i] + dt



#print(p[:,0])
plt.plot(p[:,0], p[:,1])
plt.grid(1)
plt.show()
