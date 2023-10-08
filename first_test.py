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
K_e = np.zeros(N) #kinetic energy
P_e = np.zeros(N) #potential energy




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
    K_e[i] = 0.5*mass*np.linalg.norm(v[i])**2
    P_e[i] = mass*g*p[i,1]



#print(p[:,0])
plt.plot(p[:,0], p[:,1])
plt.grid(1)
plt.show()

plt.plot(t, K_e, label="kinetic")
plt.plot(t, P_e, label="potential")
plt.grid(1)
plt.legend()
plt.show()
