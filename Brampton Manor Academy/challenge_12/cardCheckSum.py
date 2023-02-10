def getCardNumber() -> int:
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

def identifyPAN(number: str) -> int:
    return int(number[6:15])

def identifyChecksum(number: str) -> int:
    return int(number[-1])

def identifyIssuer(number: str) -> str:
    if number[0:2] == "34" or number[0:2] == "37":
        return "American Express"
    elif number[0:1] == "3":
        return "JCB"
    elif number[0:1] == "4":
        return "Visa"
    elif number[0:2] >= "51" and number[0:2] <= "55":
        return "MasterCard"
    else:
        return "Unknown"

def calculateChecksum(numArr) -> int:
    sum = 0
    for num in numArr:
        sum += num
    checkSum = (10 - (sum % 10)) % 10
    return checkSum

def checkValidity(number: int, checksumDigit: int) -> str:
    payload:str = str(number)[0:15]
    sumArr:list = []
    i:int = 0
    for num in payload:
        if i % 2 == 0:
            num = str(int(num) * 2)
            if len(num) > 1:
                num = int(num[0]) + int(num[1])
        sumArr.append(int(num))
        i += 1
    if calculateChecksum(sumArr) == checksumDigit:
        return "valid"
    else:
        return "not valid"

def output(number: int, issuer: str, isReal: str):
    print(f"Card number: {number}")
    print(f"Issuer: {issuer}")
    print(f"The card is {isReal}")

if __name__ == "__main__":
    number:int = getCardNumber()
    pan:int = identifyPAN(str(number))
    checksumDigit:int = identifyChecksum(str(number))
    issuer:str = identifyIssuer(str(number))
    isReal:str = checkValidity(number, checksumDigit)
    output(number, issuer, isReal)