import numpy as np

def maxwellian(vx, vy, vz, sigma, drift = 0):
    coefficient = 1 / (2*np.pi*sigma**2)**(3/2)
    exponent = -((vx-drift)**2 + vy**2 + vz**2)
    return coefficient * np.exp(exponent / (2*sigma**2))

def core_beam(vx, vy, vz, alpha= 0.05, drift=2, sigma_c=1, sigma_b=0.4):
    core = maxwellian(vx, vy, vz, sigma_c)
    beam = maxwellian(vx, vy, vz, sigma_b, drift)

    return (1 - alpha) * core + alpha * beam




