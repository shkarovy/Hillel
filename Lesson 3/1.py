num1 = float(input("Enter the first number: "))
operation = input("Enter an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed!")
    else:
        result = num1 / num2
        print("Result:", result)
else:
    print("Unknown operation. Please enter one of the following: +, -, *, /")
