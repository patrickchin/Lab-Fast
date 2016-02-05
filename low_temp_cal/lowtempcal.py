import numpy as np
import scipy.constants as const

dtype = np.dtype([('time',np.int), ('current',np.float),
    ('voltage',np.float), ('temperature',np.float)])

def calc_radiated_power(temp, surface_area=0.0010187, emissivity=0.04):
    return surface_area * emissivity * const.Stefan_Boltzmann * (temp**4)

def calc_thermal_conductivity(power, iv, temp_diff, surface_area=5.655e-7, length=0.01):
    return np.abs(length*(iv-power)/(surface_area*temp_diff))

def calc_thermal_conductivity2(power, current, voltage, temp_diff, surface_area=5.655e-7, length=0.01):
    return np.abs(length*(current*voltage-power)/(surface_area*temp_diff))

