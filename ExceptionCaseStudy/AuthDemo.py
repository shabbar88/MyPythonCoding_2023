from Authentication import verify
from Login import LoginError
while(True):
    try:
        verify()
    except LoginError:
        print("username or password is wrong.plzz try again ...")