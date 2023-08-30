from ATMMenu import menu
from ATMOperations import deposit, withdraw, balenq
from ATMExcept import DepositError, WithdrawError, InsufficientFundError

while True:
    menu()
    try:
        ch = int(input("Enter ur choice : "))
        match ch:
            case 1:
                try:
                    deposit()
                except ValueError:
                    print("Do not enter alnums,strs and symbols :")
                except DepositError:
                    print("plzz do not deposit -ve/zero amt in account")

            case 2:
                try:
                    withdraw()
                except ValueError:
                    print("Do not enter alnums,strs and symbols :")
                except WithdrawError:
                    print("Do not withdraw -ve/zero amt from Account ")

                except InsufficientFundError:
                    print("Ur account do not have funds ")

            case 3:
                balenq()

            case 4:
                print("Thanks for using program :")
                break
            case _:
                print("Ur selection of operation is wrong..try again.....")
    except ValueError:
        print("Do not enter alnums,strs and symbols  ")
