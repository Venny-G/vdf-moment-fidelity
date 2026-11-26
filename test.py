from vdf import core_beam
from grids import velocity_grid
from moments import density, bulk_velocity, third_moment, fourth_moment
from moments import heat_flux, pressure_tensor

vx, vy, vz, dv = velocity_grid(N=128, L=6)

f = core_beam(vx, vy, vz)
P = pressure_tensor(f, vx, vy, vz, dv)
Q = third_moment(f, vx, vy, vz, dv)
n = density(f, dv)
u = bulk_velocity(f, vx, vy, vz, dv)

print("Density:", n)
print("Density error:", abs(n - 1))
print("Bulk velocity:", u)
print("Pressure tensor:", P)

##3rd moment
Q = third_moment(f, vx, vy, vz, dv)

print("Third moment tensor:")
print(Q)

print("Qxxx:", Q[0, 0, 0])
print("Qxyy:", Q[0, 1, 1])
print("Qxzz:", Q[0, 2, 2])

##heat flux from fourth moment
print("Heat flux:", heat_flux(Q))

R = fourth_moment(f, vx, vy, vz, dv)

print("Rxxxx:", R[0, 0, 0, 0])
print("Rxxyy:", R[0, 0, 1, 1])
print("Ryyyy:", R[1, 1, 1, 1])
print("Ryyzz:", R[1, 1, 2, 2])
