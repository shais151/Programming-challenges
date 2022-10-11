def temp_input():
    return float(input("Enter air temperature: "))
def wind_input():
    return float(input("Enter wind speed: "))

def calculate_chill(air_temp, air_speed):
    wind_chill = 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16
    return wind_chill

def output(wind_chill):
    print(f"Wind chill: {wind_chill}")

air_temp = temp_input()
air_speed = wind_input()
wind_chill = calculate_chill(air_temp, air_speed)
output(wind_chill)
