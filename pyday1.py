print("***********************************")
print("Welcome to BS InfoTech 302 A. Grading System")
print("GRADE    GRADING SCALE       REMARKS")
print("1.00      94.8 - 100         Passed")
print("1.25      89.2 - 94.7        Passed")
print("1.50      83.6 - 89.1        Passed")
print("1.75      78.0 - 83.5        Passed")
print("2.00      72.4 - 77.9        Passed")
print("2.25      66.8 - 72.3        Passed")
print("2.50      61.2 - 66.7        Passed")
print("2.75      55.6 - 61.1        Passed")
print("3.00      50.0 - 55.5        Passing Grade")
print("5.00      0.0 - 49.9         Failling Grade")



name = input("Enter your name: ")
print(f"Hi, {name}")
age = int(input("Enter your Age: "))
print(f"Age: {age}")
section = input("Enter your Section: ")
print(f"Section: {section}")

grade1= float(input("Introduction to Computing: "))
grade2 = float(input("Computer Programming 1: "))
grade3 = float(input("Information Management: "))
grade4 = float(input("Data Structures and Algorithms: "))
grade5 = float(input("Object Oriented Programming: "))


grades = (grade1 + grade2 + grade3 + grade4 + grade5)/5
print("GWA: ", grades)

if grades > 1.00: 
    print("PASSED!")
elif grades > 1.25:
    print("PASSED!")
elif grades > 1.50:
    print("PASSED!")
elif grades > 1.75:
    print("PASSED!")
elif grades > 2.00:
    print("PASSED!")
elif grades > 2.25:
    print("PASSED!")
elif grades > 2.50:
    print("PASSED!")
elif grades > 2.75:
    print("PASSED!")
elif grades > 3.00:
    print("PASSING GRADE!")
elif grades > 5.00:
    print("FAILLING GRADE!")


