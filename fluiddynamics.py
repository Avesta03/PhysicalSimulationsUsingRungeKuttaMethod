import numpy as np
import matplotlib.pyplot as plt

# defining domain
grid_size = 50  # Number of cells in each dimension
domain_size = 1.0  # Length of the domain
dx = domain_size / grid_size  # Cell size

# creating grid
x = np.linspace(0, domain_size, grid_size)
y = np.linspace(0, domain_size, grid_size)
X, Y = np.meshgrid(x, y)
