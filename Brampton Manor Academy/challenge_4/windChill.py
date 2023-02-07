def temp_input() -> float:
    return float(input("Enter air temperature: "))
def wind_input() -> float:
    return float(input("Enter wind speed: "))

def calculate_chill(air_temp: float, air_speed: float) -> float:
    wind_chill = 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16
    return wind_chill

def output(wind_chill: float):
    print(f"Wind chill: {wind_chill}")

if __name__ == "__main__":
    air_temp:float = temp_input()
    air_speed:float = wind_input()
    wind_chill:float = calculate_chill(air_temp, air_speed)
    output(wind_chill)
