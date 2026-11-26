import numpy as np

def density(f, dv):
    return np.sum(f) * dv**3

def bulk_velocity(f, vx, vy, vz, dv):
    n = density(f, dv)

    ux = np.sum(vx * f) * dv**3 / n
    uy = np.sum(vy * f) * dv**3 / n
    uz = np.sum(vz * f) * dv**3 / n

    return np.array([ux, uy, uz])

def pressure_tensor(f, vx, vy, vz, dv):
    u = bulk_velocity(f, vx, vy, vz, dv)

    cx = vx - u[0]
    cy = vy - u[1]
    cz = vz - u[2]

    c = [cx, cy, cz]

    P = np.zeros((3, 3))

    for i in range(3):
        for j in range(3):
            P[i, j] = np.sum(c[i] * c[j] * f) * dv**3

    return P

def third_moment(f, vx, vy, vz, dv):
    u = bulk_velocity(f, vx, vy, vz, dv)

    cx = vx - u[0]
    cy = vy - u[1]
    cz = vz - u[2]

    c = [cx, cy, cz]

    Q = np.zeros((3, 3, 3))

    for i in range(3):
        for j in range(3):
            for k in range(3):
                Q[i, j, k] = np.sum(
                    c[i] * c[j] * c[k] * f
                ) * dv**3

    return Q

def heat_flux(Q):
    q = np.zeros(3)

    for i in range(3):
        for j in range(3):
            q[i] += 0.5 * Q[i, j, j]

    return q

def fourth_moment(f, vx, vy, vz, dv):
    u = bulk_velocity(f, vx, vy, vz, dv)
    c = [vx - u[0], vy - u[1], vz - u[2]]
    R = np.zeros((3, 3, 3, 3))

    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    R[i, j, k, l] = np.sum(
                        c[i] * c[j] * c[k] * c[l] * f
                    ) * dv**3

    return R 