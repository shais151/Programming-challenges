def rods_to_meters(rods): 
    return rods * 5.0292 
def meters_to_feet(rods): 
    return rods_to_meters(rods) / 0.3048 
def meters_to_miles(rods): 
    return rods_to_meters(rods) / 1609.34 
def rods_to_furlongs(rods): 
    return rods / 40 
def time_to_walk(rods): 
    return (meters_to_miles(rods) / 3.1) * 60 

def enter_rods():
    return float(input("Enter distance in rods: ")) 

def rodConversions(rods): 
    print(f"Meters: {rods_to_meters(rods)}") 
    print(f"Feet: {meters_to_feet(rods)}") 
    print(f"Miles: {meters_to_miles(rods)}") 
    print(f"Furlongs: {rods_to_furlongs(rods)}") 
    print(f"Minutes to walk: {time_to_walk(rods)}") 

rods = enter_rods()
rodConversions(rods)
