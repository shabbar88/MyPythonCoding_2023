from Division import divop
from Tauquir import  BangDivError
try:
    a=int(input("Enter number a : "))
    b=int(input("Enter number b :"))
    c=divop(a,b)
except BangDivError:
    print("Do not give zero for denominator :")

