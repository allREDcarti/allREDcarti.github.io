print("Calculator (+ - * /)")

operator = input("Enter a Operator (+ - * /): ")
num_one = float(input("Enter a number: "))
num_two = float(input("Enter a number: "))

if operator == "+":
    print(round("result = " , num_one + num_two, 3))
elif operator == "-":
    print(round("result = " ,num_one - num_two, 3))
elif operator == "*":
    print(round("result = " ,num_one * num_two, 3))
elif operator == "/":
    print(round("result = " ,num_one / num_two, 3))
else: 
    print(f"The {operator} is not valid operator!")
