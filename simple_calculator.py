#I'm gonna make a simple calculator using if statment only
operator = input("enter the operator you are going to use (+ - / *): ")
#This loop infinitly tell the user entres the right input for the operator
while operator not in ["+", "-", "*", "/"]:
    operator = input("intre the operator that u gona use (+ - / *): ")
num1 = float(input("entre the first number: "))
num2 = float(input("entre the second number: "))

if operator == '+':
    print(f"{num1} {operator} {num2} = {num1 + num2}")
elif operator == '-':
    print(f"{num1} {operator} {num2} = {num1 - num2}")
elif operator == '*':
    print(f"{num1} {operator} {num2} = {num1 * num2}")
elif operator == '/':
    print(f"{num1} {operator} {num2} = {num1 / num2}")