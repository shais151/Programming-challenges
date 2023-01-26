def check_values(values):
    if values.lower() == "q":
        print("Exiting calculator...")
        quit()
    
    array = values.split()

    try:
        array[0] = float(array[0])
        array[1] = float(array[1])
    except:
        print("The first two arguments must be numbers.")
        return -1

    if (array[2] == "/" or array[2] == "//" or array[2] == "%") and array[1] == 0:
        print("Divisions by zero is not possible")
        return -1

    return array

def calc(array):
    num1 = float(array[0])
    num2 = float(array[1])
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
    return answer

def main():
    values = input("Enter your calculation: ")
    calcArr = check_values(values)
    if calcArr == -1:
        return main()
    answer = calc(calcArr)
    print(answer)
    return main()

if __name__ == "__main__":
    main()