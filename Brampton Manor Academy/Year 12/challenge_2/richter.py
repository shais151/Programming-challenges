def richter_to_energy(richter):
    return 10 ** ((1.5 * richter) + 4.8)
def energy_to_tnt(richter):
    return richter_to_energy(richter) / 4184000000

def input_richter():
    return float(input("Please enter a Richter scale value: "))

def richterConversions(richter):
    print(f"Equivalence in joules: {richter_to_energy(richter)}")
    print(f"Equivalence in tons of TNT: {energy_to_tnt(richter)}")

richter = input_richter()
richterConversions(richter)
