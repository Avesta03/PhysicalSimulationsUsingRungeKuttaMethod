import numpy as np
import matplotlib.pyplot as plt

# defining domain
grid_size = 50  # number of cells in each dimension
domain_size = 1.0  # length of the domain
dx = domain_size / grid_size  # cell size

# creating grid
x = np.linspace(0, domain_size, grid_size)
y = np.linspace(0, domain_size, grid_size)
X, Y = np.meshgrid(x, y)

# initialising fluid properties
u = np.zeros((grid_size, grid_size))  # x-component of velocity
v = np.zeros((grid_size, grid_size))  # y-component of velocity
pressure = np.zeros((grid_size, grid_size))  # pressure (p)

# simulation parameters
viscosity = 0.1  # viscosity of the fluid
time_step = 0.01  # time step size
num_steps = 100  # number of time steps

# discretising the equations (using the finite difference method hopefully)
def simulate_flow():
    for step in range(num_steps):
        # computing velocity gradients
        du_dx = (u[1:, :] - u[:-1, :]) / dx # finite difference method - we're calculating the gradients by subtracting the velocity values along the x-direction then dividing by cell size...
        du_dy = (u[:, 1:] - u[:, :-1]) / dx # ... in order to approximate the derivative!
        dv_dx = (v[1:, :] - v[:-1, :]) / dx
        dv_dy = (v[:, 1:] - v[:, :-1]) / dx

        # now to compute pressure gradients
        dp_dx = (pressure[1:, :] - pressure[:-1, :]) / dx
        dp_dy = (pressure[:, 1:] - pressure[:, :-1]) / dx