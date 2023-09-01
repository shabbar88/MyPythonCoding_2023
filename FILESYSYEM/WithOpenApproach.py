try:
    with open("std_data") as tauquir:
        print("-------------------------------------------------")
        print("Type of tauquir=", type(tauquir))
        print("File opened successfully")
        print("--------------------------------------------------")
        print("File Name:", tauquir.name)
        print("File mode:", tauquir.mode)
        print("is file readable:", tauquir.readable())
        print("is file writable:", tauquir.writable())
        print("is file closed:", tauquir.closed)
        print("-------------------------------------------------")
except FileNotFoundError:
    print("file does not exist")
finally:
    print("I AM FROM FINALLY BLOCK")
    print("is file closed:", tauquir.closed)
