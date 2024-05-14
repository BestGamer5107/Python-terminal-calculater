result = None

print("What's the first number?")
num1 = float(input())

print("What's the operation? (+, -, *, /, ^)")
op = input()

print("What's the second number?")
num2 = float(input())

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "^":
    result = num1 ** num2
elif op == "/":
    if num2 != 0:
        result = num1 / num2
    elif num2 == 0:
        print("Error: Division by zero.")
else:
    print("Error: Unknown operation.")

if result != None:
    print("Result:", result)
