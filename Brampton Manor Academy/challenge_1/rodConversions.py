def rodConversions():
    string = ""
    
    value = float(input("Enter distance in rods: "))
    
    def rods_to_meters(value):
        return value * 5.0292
    def meters_to_feet(value):
        return rods_to_meters(value) / 0.3048
    def meters_to_miles(value):
        return rods_to_meters(value) / 1609.34
    def rods_to_furlongs(value):
        return value / 40
    def time_to_walk(value):
        return (meters_to_miles(value) / 3.1) * 60

    print(f"Meters: {rods_to_meters(value)}")
    print(f"Feet: {meters_to_feet(value)}")
    print(f"Miles: {meters_to_miles(value)}")
    print(f"Furlongs: {rods_to_furlongs(value)}")
    print(f"Minutes to walk: {time_to_walk(value)}")

rodConversions()
