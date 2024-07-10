def addition(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("""
What would to like to do?
    1. Add two numbers
    2. Subtract two numbers
    3. Multiply two numbers
    4. Divide two numbers
""")

choice = input("> ")
calc = True

while calc:
    if choice in ("1", "2", "3", "4"):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if choice == "1":
                print(f"{a} + {b} = {addition(a, b)}")
            elif choice == "2":
                print(f"{a} - {b} = {subtract(a, b)}")
            elif choice == "3":
                print(f"{a} * {b} = {multiply(a, b)}")
            elif choice == "4":
                try:
                    print(f"{a} / {b} = {divide(a, b)} {float.as_integer_ratio(divide(a, b))}")
                except ZeroDivisionError:
                    print("undefined")
        except ValueError:
            print("Invalid input.")
            continue
    else:
        print("Not an option!")
