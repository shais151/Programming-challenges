def getCardNumber():
    number = 0
    while number == 0:
        try:
            number = int(input("Enter your card number: "))

            if len(str(number)) > 16:
                print("Card number is too long")
                number = 0
            elif len(str(number)) < 16:
                print("Card number is too short")
                number = 0
        except:
            print("Card number must be just numbers")
    return number

def identifyPAN(number):
    num_str = str(number)
    return int(num_str[7:15])

def checksum(number):
    num_str = str(number)
    return int(num_str[-1])

def identifyIssuer(number):
    num_str = str(number)
    if num_str[0:2] == "34" or num_str[0:2] == "37":
        return "American Express"
    elif num_str[0:1] == "3":
        return "JCB"
    elif num_str[0:1] == "4":
        return "Visa"
    elif num_str[0:2] >= "51" and num_str[0:2] <= "55":
        return "MasterCard"
    else:
        return

def checkValidity(number, pan, checksumDigit):
    return

def output(number, issuer, isReal):
    print(f"Card number: {number}")
    print(f"Issuer: {issuer}")

if __name__ == "__main__":
    number = getCardNumber()
    pan = identifyPAN(number)
    checksumDigit = checksum(number)
    issuer = identifyIssuer(number)
    isReal = checkValidity(number, pan, checksumDigit)
    # output(number, issuer, isReal)