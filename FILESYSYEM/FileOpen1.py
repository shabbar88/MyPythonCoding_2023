try:
    fp = open("std_data", "r")
except FileNotFoundError:
    print("file does not exist ....")
else:
    print("--------------------------------")
    print("Type of fp=", type(fp))
    print("File opened successfully...")
    print("----------------------------------")
    print("File Name :", fp.name)
    print("is file readable", fp.readable())
    print("is file writable", fp.writable())
    print("is file closed", fp.closed)
    print("-------------------------------------")
finally:
    print("I am from finally block..............")
    fp.close()
    print("is file closed..", fp.closed)
