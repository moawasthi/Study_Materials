# Create a calculator
#     The calculator must take inputs from the user
#     Provide operators 
#     Provide next number
#     If symbol is = then show the result
result = 0
operator = ''

while(operator != "="):
    operator = input("Enter the operator")
    if operator == '+':
        num1 = int( input("Enter the first number") )
        num2 = int( input("Enter the second number"))
        result += (num1 + num2)
        continue 
    elif operator == '-':
        num1 = int( input("Enter the first number") )
        num2 = int( input("Enter the second number"))
        result += num1 - num2
        continue
    elif operator == "*":
        num1 = int( input("Enter the first number") )
        num2 = int( input("Enter the second number"))
        result += num1 * num2
        continue
    elif operator == "/":
        num1 = int( input("Enter the first number") )
        num2 = int( input("Enter the second number"))
        result += num1 / num2
        continue

print(result)
