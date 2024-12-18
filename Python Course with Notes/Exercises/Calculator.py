# learning arithmetic operators 

# + = addition
# - = subtraction
# * = multiplication
# / = division
# % = modulus (remainder value batata hai ye ex: 3/5=2)
# ** = exponential (basically ye power lagata hai ex: 2^2=4)
# // = floor division ( ye point se bahar ka value bata deta hai ex: 15//6 = 2)

print("Enter any 2 numbers below: ")

a = int(input())
b = int(input())

print("What operation would you like to perform? add, sub, mul, div, mod, exp")

inputResult = input()

if inputResult == "add":
    print("The value of addition is: ", a + b)
elif inputResult == "sub":
    print("The value of subtraction is: ",a - b)
elif inputResult == "mul":
    print("The value of multiplication is: ",a * b)
elif inputResult == "div":
    print("The value of division is: ",a / b)
elif inputResult == "mod":
    print("The value of modulus is: ",a % b)
elif inputResult == "exp":
    print("The value of exponential function is: ",a ** b)
else:
        print("We don't have more operations for now. We are working on it. Thank you!")





#Calculator 2.0 using match case statments:

u_num1 = int(input('''__Basic Calculator__
Enter your first number: '''))

u_op = int(input('''What Operation you wanna do?
1- Addition
2- Subtraction
3- Multiplication
4- Division
5- Modulus

input your operation number here: '''))

u_num2 = int(input('Enter your second number: '))

match u_num1 and u_num2:
  case _ if u_op == 1:
    print(f"\nYour answer of your operation {u_op} is",u_num1 + u_num2)
  case _ if u_op == 2:
    print(f"\nYour answer of your operation {u_op} is",u_num1 - u_num2)
  case _ if u_op == 3:
    print(f"\nYour answer of your operation {u_op} is",u_num1 * u_num2)
  case _ if u_op == 4:
    print(f"\nYour answer of your operation {u_op} is",u_num1 / u_num2)
  case _ if u_op == 5:
    print(f"\nYour answer of your operation {u_op} is",u_num1 % u_num2)

  case _:
    print("Invalid request of  operation")

