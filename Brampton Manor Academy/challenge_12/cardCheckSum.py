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

num_str = str(number)
pan = int(num_str[7:])

checksum = int(num_str[-1])
