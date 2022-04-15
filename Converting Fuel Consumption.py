def liters_100km_to_miles_gallon(liters):
    onemile = 1609.344
    onegallon = 3.785411784
    rgallon = liters/onegallon
    rmiles = 100000/onemile
    result = rmiles/rgallon
    return result

def miles_gallon_to_liters_100km(miles):
    onegallon = 3.785411784
    onemile = 1609.344
    rkm = miles*onemile
    rliters = onegallon
    result = (rliters/rkm)*100000
    return result

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
