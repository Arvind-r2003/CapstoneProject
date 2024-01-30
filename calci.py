def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        print("Result:", num1 + num2)
    elif operator == '-':
        print("Result:", num1 - num2)
    elif operator == '*':
        print("Result:", num1 * num2)
    elif operator == '/':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero.")
    else:
        print("Invalid operator. Please try again.")

if __name__ == "__main__":
    calculator()
