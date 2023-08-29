from Tauquir import BangDivError
def divop(a,b):
    if b==0:
        raise BangDivError
    else:
        return (a/b)