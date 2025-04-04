
def calculator():

    num1 = float(input("Enter first number: "))

    op = input("Enter operator (+, -, *, /): ")

    num2 = float(input("Enter second number: "))

   

    if op == "+":

        return f'Result {num1 + num2}'

    elif op == "-":

        return f'Result {num1 - num2}'

    elif op == "*":

        return f'Result {num1 * num2}'

    elif op == "/":

        return "Error! Division by zero." if num2 == 0 else num1 / num2

    else:

        return "Invalid operator!"g


print(calculator())