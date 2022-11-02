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

def identifyPAN(number):
    num_str = str(number)
    return int(num_str[7:])

def checksum(number):
    num_str = str(number)
    return int(num_str[-1])

def identifyIssuer(number):
    return

if __name__ == "__main__":
    number = getCardNumber()
    pan = identifyPAN(number)
    checksumDigit = checksum(number)
    issuer = identifyIssuer(number)