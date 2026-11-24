import numpy as np

from vdf import core_beam
from grids import velocity_grid

vx, vy, vz, dv = velocity_grid(N=128, L=6)

f = core_beam(vx, vy, vz)

density = np.sum(f) * dv**3

print(density)
print(abs(density-1))
print("poop")