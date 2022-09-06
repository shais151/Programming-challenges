def rodConversions():
    # create string that will be returned
    string = ""

    # print header
    print("### ECO CS 18 ##\n### Project 1 ##\n\n")
    
    # get float value
    value = float(input("Enter distance in rods: "))

    # calculate conversion values
    meters = value * 5.0292
    feet = meters / 0.3048
    miles = meters / 1609.34
    furlongs = value / 40
    time = (miles / 3.1) * 60

    # add conversion values to string
    string += "\nConversions\n"
    string += f"Meters: {meters}\n"
    string += f"Feet: {feet}\n"
    string += f"Miles: {miles}\n"
    string += f"Furlongs: {furlongs}\n"
    string += f"Minutes to walk 10.0 rods: {time}"

    # return the string
    return string

# print the string returned from the function
print(rodConversions())
    
