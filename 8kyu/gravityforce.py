def solution(arr_val, arr_unit):
    unit_conversion = {
        'kg': 1,
        'g': 0.001,
        'mg': 1e-6,
        'μg': 1e-9,
        'lb': 0.453592,
        'm': 1,
        'cm': 0.01,
        'mm': 0.001,
        'μm': 1e-6,
        'ft': 0.3048
    }

    # Extract values and units from arrays
    mass_obj1, mass_obj2, distance = arr_val
    unit_mass_obj1, unit_mass_obj2, unit_distance = arr_unit

    # Convert masses and distance to SI units
    mass_obj1_si = mass_obj1 * unit_conversion[unit_mass_obj1]
    mass_obj2_si = mass_obj2 * unit_conversion[unit_mass_obj2]
    distance_si = distance * unit_conversion[unit_distance]

    # Gravitational constant
    G = 6.67e-11

    # Calculate gravitational force
    force = (G * mass_obj1_si * mass_obj2_si) / distance_si**2

    return force

arr_val = [10, 20, 5]
arr_unit = ['kg', 'kg', 'm']
result_force = solution(arr_val, arr_unit)
print(result_force)
#Did not liked this task
