cardNum = input("Please enter you credit card number: ")
#cardNum = '4003600000000014'
num = int(cardNum)
x = int(cardNum)

def lungAlg(x):
    sum = 0
    doublesum = 0
    total = 0
    dsum = 0
    dsumtotal = 0
    while x > 0:
        sum = sum + (x % 10)
        x //= 10
        dsum = (x % 10) * 2
        doublesum = doublesum + ((x % 10) * 2)
        if dsum > 9:
            dsumtotal += dsum % 10
            dsum //= 10
            dsumtotal += dsum
        else:
            dsumtotal += dsum
        x //= 10
    total = sum + dsumtotal
    
    if total % 10 == 0:
        num = int(cardNum)
        for i in range(len(cardNum) - 1):
            num //= 10

        if len(cardNum) == 15 and num == 3:
            print("American Express")
        elif len(cardNum) == 16 and num == 5:
            print("MasterCard")
        elif num == 4:
            if len(cardNum) == 13 or len(cardNum) == 16:
                print("Visa")
            else:
                print("Error")
        else:
            print("Please enter a valid credit card number")
    else:
        print("Not a valid credit card number")

lungAlg(x)