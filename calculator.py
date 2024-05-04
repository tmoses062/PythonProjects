
def add(n1, n2):
    """This adds two numbers"""
    return n1 + n2

def subtract(n1, n2):
    """This subtracts two numbers"""
    return n1 - n2

def multiply(n1, n2):
    """This multiplies two numbers"""
    return n1 * n2

def divide(n1, n2):
    """This divides two numbers"""
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    from art import logo3
    print(logo3)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    continue_calc = True
    while continue_calc:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if continue_calculating == 'y':
            num1 = answer
        else:
            continue_calc = False
            calculator()

calculator()
        