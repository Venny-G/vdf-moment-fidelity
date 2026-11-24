import numpy as np

##set up a grid of points in velocity space
def velocity_grid(N=128, L=6):
    dv = 2*L/N
    v = np.linspace(-L + dv/2, L - dv/2, N)
    vx, vy, vz = np.meshgrid(v, v, v, indexing='ij') 

    return vx, vy, vz, dv
##it autofilled this btw...
## Volume is d^3 v = (delta_v)^3.