
number1 = input("Enter first number:")
operation = input("Enter operation (+, -, *, /): ")
number2 = input("Enter second number:")

add = float(number1) + float(number2)
subtract = float(number1) - float(number2)
multiply = float(number1) * float(number2)
divide = float(number1) / float(number2)

if operation == "+":
    print ("The sum of the two numbers is:", add)
elif operation == "+": 
    print("The difference of the two numbers is:", subtract)
elif operation == "+":
    print ("The product of the two numbers is:", multiply)
elif operation == "+":
    print ("The quotient of the two numbers is:", divide)
else: 
    print("Error Please Try again")