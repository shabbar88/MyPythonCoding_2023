import sys


def getreport():
    # code for accepting student serial number
    global grade
    while (True):
        sno = int(input("Enter serial number (100-200)"))
        if sno >= 100 and sno <= 200:
            break
        print("\t {} Invalid Student Number : ".format(sno))
    # code for accepting student name
    sname = input("Enter Student Name :")
    # code for accepting marks in c language
    while (True):
        cpm = int(input("Enter marks in c prog lang :"))
        if cpm >= 0 and cpm <= 100:
            break
        print("\t {} Invalid marks in c lang :".format(cpm))

    # code for accepting amarks in cpp lang
    while (True):
        cppm = int(input("Enter marks in c++ prog lang :"))
        if cppm >= 0 and cppm <= 100:
            break
        print("\t {} Invalid marks in c++ lang :".format(cppm))
    # code for accepting marks in python lang
    while (True):
        pym = int(input("Enter marks in python lang :"))
        if pym in range(1, 101):
            break
        print("\t {} Invalid marks in python lang :".format(pym))
    # compute total_marks
    total_marks = cpm + cppm + pym
    percent = round((total_marks / 300) * 100, 2)
    # assign grades<
    if cpm < 40 or cppm < 40 or pym < 40:
        grade = "FAIL"
    else:
        # allocating pass grade
        if percent >= 75:
            grade = "DISTINCTION"
        elif percent >= 60 and percent <= 75:
            grade = "FIRST"
        elif percent > 50 and percent < 60:
            grade = "SECOND"
        elif percent > 40 and percent < 50:
            grade = "THIRD"
    # DISPLAY THE MARKS REPORT
    print("=" * 50)
    print("\t STUDENT MARKS REPORT :")
    print("=" * 50)
    print("\t Student Serial Number :{}".format(sno))
    print("\t Student Name :{}".format(sname))
    print("\t Student Marks in C lang: {}".format(cpm))
    print("\t Student Marks in C++ lang: {}".format(cppm))
    print("\t Student Marks in python lang: {}".format(pym))
    print("=" * 50)
    print("\t TOTAL MARKS : {}".format(total_marks))
    print("\t PERCENTAGE OF MARKS : {}".format(percent))
    print("\t STUDENT GRADE : {}".format(grade))
    print("=" * 50)
    sys.exit()
