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
density = 1.0 # p

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

# Runge-Kutta coefficients
a2 = 1.0 / 2.0
a3 = 1.0 / 2.0
a4 = 1.0

def simulate_flow():
    for step in range(num_steps):
        # Runge-Kutta time integration
        for rk_step in range(4):
            # to compute velocity gradients and pressure gradients at the current time
            du_dx = (u[1:, :] - u[:-1, :]) / dx
            du_dy = (u[:, 1:] - u[:, :-1]) / dx
            dv_dx = (v[1:, :] - v[:-1, :]) / dx
            dv_dy = (v[:, 1:] - v[:, :-1]) / dx
            dp_dx = (pressure[1:, :] - pressure[:-1, :]) / dx
            dp_dy = (pressure[:, 1:] - pressure[:, :-1]) / dx

            # now to compute the intermediate velocity fields using current gradients
            u_temp = u + time_step * (-u * du_dx - v * du_dy + (1.0 / density) * dp_dx + viscosity * (du_dx ** 2 + du_dy ** 2))
            v_temp = v + time_step * (-u * dv_dx - v * dv_dy + (1.0 / density) * dp_dy + viscosity * (dv_dx ** 2 + dv_dy ** 2))

            # then computing velocity gradients and pressure gradients at INTERMEDIATE time
            du_dx_temp = (u_temp[1:, :] - u_temp[:-1, :]) / dx
            du_dy_temp = (u_temp[:, 1:] - u_temp[:, :-1]) / dx
            dv_dx_temp = (v_temp[1:, :] - v_temp[:-1, :]) / dx
            dv_dy_temp = (v_temp[:, 1:] - v_temp[:, :-1]) / dx

            # finally computing final velocity fields using intermediate gradients
            u = u + a2 * time_step * (-u_temp * du_dx_temp - v_temp * du_dy_temp + (1.0 / density) * dp_dx + viscosity * (du_dx_temp ** 2 + du_dy_temp ** 2))
            v = v + a2 * time_step * (-u_temp * dv_dx_temp - v_temp * dv_dy_temp + (1.0 / density) * dp_dy + viscosity * (dv_dx_temp ** 2 + dv_dy_temp ** 2))

