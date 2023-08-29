from MultTable import table
from MultExcept import ZeroError, NegNumError

try:
    n = int(input("Enter any number for generating multiplication table :"))
    table(n)
except ZeroError:
    print("plzz do not provide zero :")
except NegNumError:
    print("plzz do not provide negative number :")
except:
    print("oops!! something went wrong.. ")
