# Simulation of a Simple Harmonic Oscillator using Physics and the Runge-Kutta Method of Numerical Integration

import numpy as np
import matplotlib.pyplot as plt

# F = kx 

# parameters
m = 1.0 # mass
k = 1.0 # spring constant
x0 = 0.5 # osc initial pos
v0 = 0.0 # osc initial vel

# time step and time span
dt = 0.01
t_start = 0.00
t_end = 20.00

# initial conditions (of the system)
y0 = np.array([x0, v0])

# defining a function that establishes/describes the system dynamics
def f(t, y):
    # y[0] is the position x of the oscillator
    # y[1] is the velocity v of the oscillator
    return np.array([y[1], -k/m*y[0]])

# Runge-Kutta method to solve system of Ordinary Differential Equations
def rk4th_step(f, t, y, dt):
    k1 = f(t, y)