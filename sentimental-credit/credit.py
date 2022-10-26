def luhnsCheck(number):
    sum1 = 0
    sum2 = 0
    firstdigits = []
    lastdigits = []
    length = len(str(number))
    for i in range(0, length - 1, 2):
        firstdigits.append(2*(int(str(number)[length - i - 2])))
    for i in range(len(firstdigits)):
        if firstdigits[i] >= 10:
            firstdigits[i] = (firstdigits[i] % 10) + (firstdigits[i] // 10)
            sum1 += firstdigits[i]
        else:
            sum1 += firstdigits[i]
            continue
    for i in range(0, length, 2):
        lastdigits.append(int(str(number)[length - i - 1]))
    for i in range(len(lastdigits)):
        if lastdigits[i] >= 10:
            lastdigits[i] = (lastdigits[i] % 10) + (lastdigits[i] // 10)
            sum2 += lastdigits[i]
        else:
            sum2 += lastdigits[i]
            continue

    sumtotal = sum1 + sum2

    if sumtotal % 10 == 0:
        return True
    else:
        return False

def visaCheck(number):
    if (luhnsCheck(number)) and str(number)[0] == '4':
        return True
    else:
        return False

def amexCheck(number):
    if (luhnsCheck(number)) and str(number)[:2] in ['34', '37']:
        return True
    else:
        return False

def masterCheck(number):
    if (luhnsCheck(number)) and str(number)[:2] in ['51', '52', '53', '54', '55']:
        return True
    else:
        return False

def main():
    #User Prompt
    while (True):
        try:
            number = int(input("Card Number: "))
            break;
        except ValueError:
            print("INVALID1")

    if(str(number)[1]) in [4, 7]:
        print(Yes)

    #Card Bool Init
    visa = False
    amex = False
    master = False

    #Digit Error Check & Running Number Through Check Functions
    if len(str(number)) != 13 and len(str(number)) != 15 and len(str(number)) != 16:
        print("INVALID")
        exit(1)

    visa = visaCheck(number)
    amex = amexCheck(number)
    master = masterCheck(number)

    #Final Check & Card Type Print
    if (visa):
        print("VISA")
        exit(0)
    elif (amex):
        print("AMEX")
        exit(0)
    elif (master):
        print("MASTERCARD")
        exit(0)
    else:
        print("INVALID")
        exit(1)


if __name__ == "__main__":
    main()
