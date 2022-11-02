def input_values():
    values = input("Enter your calculation: ")
    if values.lower() == "q":
        print("Exiting calculator...")
        quit()
    array = values.split()
    if array[2] == "/" or array[2] == "//" or array[2] == "%":
        if array[1] == "0":
            print("Divisions by zero is not possible")
            return input_values()
    return array

def output(answer):
    print(answer)

def calc(array):
    try:
        num1 = float(array[0])
        num2 = float(array[1])
    except:
        print("The first two arguments must be numbers.")
        return -1
    operation = array[2]

    match operation:
        case "+":
            answer = num1 + num2
        case "-":
            answer = num1 - num2
        case "*":
            answer = num1 * num2
        case "/":
            answer = num1 / num2
        case "//":
            answer = num1 // num2
        case "%":
            answer = num1 % num2
        case "**":
            answer = num1 ** num2
        case _:
            answer = "Use a valid operation."
    output(answer)

def main():
    values = input_values()
    calc(values)
    return main()

if __name__ == "__main__":
    main()