def richter_to_energy(richter: float) -> float:
    return 10 ** ((1.5 * richter) + 4.8)
def energy_to_tnt(richter: float) -> float:
    return richter_to_energy(richter) / 4184000000

def table():
    richterValues = [1, 5, 9.1, 9.2, 9.5]

    headerValues = ["Richter", "Joules", "TNT"]
    print(f'{headerValues[0]} {headerValues[1]:>15} {headerValues[2]:>23} ')
    for value in richterValues:        
        energy = richter_to_energy(value)
        tnt = energy_to_tnt(value)

        energyLength = len(str(value))        
        tntLength = len(str(value))        

        print(f"{value} {energy:>{30 - energyLength}} {tnt:>{25 - tntLength}} ")


def input_richter() -> float:
    return float(input("Please enter a Richter scale value: "))

def richterConversions(richter:float):
    print(f"Equivalence in joules: {richter_to_energy(richter)}")
    print(f"Equivalence in tons of TNT: {energy_to_tnt(richter)}")

if __name__ == "__main__":
    table()
    richter:float = input_richter()
    richterConversions(richter)