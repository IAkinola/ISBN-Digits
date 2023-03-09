def validateNumber(number):
    # Checking input to know if it is valid or not
    if len(number) == 10 or len(number) == 13:
        if len(number) == 13:
            print("Valid")
        else:
            print("Invalid") if not isbn10(number) else convertTo13(number)
    else:
        print("Invalid")


def isbn10(number):
    # Verifying a 10 digit ISBN
    addUp = 0
    for num in range(len(number)):
        if number[num] != "X":
            multiplier = 10
            addUp += int(number[num]) * multiplier
            multiplier -= 1
        else:
            addUp += 10
    validity = True if addUp % 11 == 0 else False
    return validity


def isbn13(number):
    # Verifying a 13 digit ISBN
    addUp = 0
    for num in range(len(number)):
        multiplier = 1 if num % 2 == 0 else 3
        addUp += (int(number[num]) * multiplier)

    validity = True if addUp % 10 == 0 else False
    return validity


def convertTo13(number):
    # Converting a 10-digit ISBN to 13-digit ISBN
    isbn = "978" + number
    convert = isbn[:-1]
    addUp = 0
    for num in range(len(convert)):
        multiplier = 1 if int(num) % 2 == 0 else 3
        addUp += int(num) * multiplier
    addUp = (10 - addUp % 10) % 10
    convert += str(addUp)
    print(convert)


while True:
    digits = input("Enter the ISBN Digits(exit to stop): ")
    if digits == "exit":
        break
    validateNumber(digits)
