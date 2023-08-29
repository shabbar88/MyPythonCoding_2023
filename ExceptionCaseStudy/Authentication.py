from StudentMarksReport import getreport
from Login import LoginError
def verify():
    un=input("Enter your username :")
    pw = input("Entre your password :")
    if un=="python" and pw=="hyd":
        getreport()
    else:
        raise LoginError
