from ATMExcept import DepositError, WithdrawError, InsufficientFundError

bal = 500.00


def deposit():
    damt = float(input("Enter ur deposit amount "))
    if damt <= 0:
        raise DepositError
    elif damt > 0:
        global bal
        bal = bal + damt
        print("Ur account xxxx1212 credited with INR: {}".format(damt))
        print("Now ur account xxxx1213 bal after credited INR {} IS {}".format(damt, bal))


def withdraw():
    global bal
    wamt = float(input("Enter ur deposit amount "))
    if wamt <= 0:
        raise WithdrawError
    elif wamt + 500 > bal:
        raise InsufficientFundError
    else:

        bal = bal - wamt
        print("Ur account xxxx1212 debited with INR: {}".format(wamt))
        print("Now ur account xxxx1213 bal after debited INR {} IS {}".format(wamt, bal))


def balenq():
    print("ur account xxxxx1213 bal is: INR {}".format(bal))
