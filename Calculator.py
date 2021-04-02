print("This program will calculate the answer to any two number math equation you give it.")
print("Enter an equation: ")
equation = input()
if "+" in equation:
    test = equation.split("+")
elif "-" in equation:
    test = equation.split("-")
elif "/" in equation:
    test = equation.split("/")
elif "*" in equation:
    test = equation.split("*")
num1 = int(test[0])
num2 = int(test[1])
operation = ""
if "+" in equation:
    operation = (num1 + num2)
if "*" in equation:
    operation = (num1 * num2)
if "/" in equation:
    operation = (num1 / num2)
if "-" in equation:
    operation = (num1 - num2)
print(operation)
