def rods_to_meters(rods: float) -> float: 
    return rods * 5.0292 
def meters_to_feet(rods: float) -> float: 
    return rods_to_meters(rods) / 0.3048 
def meters_to_miles(rods: float) -> float: 
    return rods_to_meters(rods) / 1609.34 
def rods_to_furlongs(rods: float) -> float: 
    return rods / 40 
def time_to_walk(rods: float) -> float: 
    return (meters_to_miles(rods) / 3.1) * 60 

def enter_rods() -> float:
    return float(input("Enter distance in rods: ")) 

def rodConversions(rods: float): 
    print(f"Meters: {rods_to_meters(rods)}") 
    print(f"Feet: {meters_to_feet(rods)}") 
    print(f"Miles: {meters_to_miles(rods)}") 
    print(f"Furlongs: {rods_to_furlongs(rods)}") 
    print(f"Minutes to walk: {time_to_walk(rods)}") 

if __name__ == "__main__":
    rods:float = enter_rods()
    rodConversions(rods)
