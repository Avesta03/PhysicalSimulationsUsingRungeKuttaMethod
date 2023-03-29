# Pendulum Simulation using Physics & the Runge-Kutta Method of Numerical Integration

import numpy as np
import matplotlib.pyplot as plt

# parameters
L = 1.0
m = 1.0
g = 9.81

theta0 = 3.1415926535879793238462624338327950 / 4 # initial angle // can use np.pi as a substitute for the excessively long pi
omega0 = 0.0 # initial angular vel

def f(theta, omega):
    # func that returns deriv of th and om
    dtheta_dt = omega
    domega_dt = -(g / L) * np.sin(theta)
    return dtheta_dt, domega_dt

dt = 0.01
t_start = 0.00
t_end = 10.00
t = np.arange(t_start, t_end, dt) # time range

# creating arrays (t) for th and om
theta = np.zeros(len(t))
omega = np.zeros(len(t))

# initial conditions
theta[0] = theta0
omega[0] = omega0

# Runge-Kutta method to integrate motion eqns
for i in range(1, len(t)):
    k1_theta, k1_omega = f(theta[i-1], omega[i-1])
    k2_theta, k2_omega = f(theta[i-1] + 0.5*dt*k1_theta, omega[i-1] + 0.5*dt*k1_omega)
    k3_theta, k3_omega = f(theta[i-1] + 0.5*dt*k2_theta, omega[i-1] + 0.5*dt*k2_omega)
    k4_theta, k4_omega = f(theta[i-1] + dt*k3_theta, omega[i-1] + dt*k3_omega)
    theta[i] = theta[i-1] + (dt/6) * (k1_theta + 2*k2_theta + 2*k3_theta + k4_theta)
    omega[i] = omega[i-1] + (dt/6) * (k1_omega + 2*k2_omega + 2*k3_omega + k4_omega)
# wahoo



