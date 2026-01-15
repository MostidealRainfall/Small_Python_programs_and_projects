# Python calculator
operator = input("Enter an operator: (+ - * /): ")
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

if operator == "+":
    result = num_1 + num_2
    print(round(result))

elif operator == "-":
    result = num_1 - num_2
    print(round(result))

elif operator == "*":
    result = num_1 * num_2
    print(round(result))

elif operator == "/":
    result = num_1 / num_2
    print(round(result))
    
else:
    print(f"The operator {operator} is not valid")