from astropy import units as u
from astropy import constants as const

length = 26 * u.meter

G = 6.67430e-11 * ((u.N*u.m**2)/u.kg**2)

#astronomical data for various planets
earth_vol_mean_radius_m = 6371000
earth_mass_kg = 5.9722e24
earth_period_yr = 1



def force_gravity(m1, m2, r):
    #Universal law of gravitation

    return((G*m1*m2)/(r**2))

print(force_gravity(200,200,4))

print(G)

print(const.G)