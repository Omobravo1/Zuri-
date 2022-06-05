#Program to make a simple calculator

def add(x,y):
    "This function adds 2 numbers"
    return x + y

def subtract(x,y):
    "This function subtracts 2 numbers"
    return x - y

def multiply(x,y):
    "This function multiplies 2 numbers"
    return x * y

def divide(x,y):
    "This function divides 2 numbers"
    return x / y

def modulo(x,y):
    "This function gives the remainder of 2 numbers"
    return x % y

def power(x,y):
    "This function raises a number to another number"
    return pow(x,y)

#Take the input from the user
print ("Select operation.") 
print ("1.Add")
print ("2.Subtract")
print ("3.Multiply")
print ("4.Divide")
print ("5.Modulo")
print ("6.Power")

choice = input ("Enter choice 1/2/3/4/5/6:")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if choice == '1':
     print (num1, "+", num2,"=", add(num1, num2))

elif choice == '2':
     print (num1, "-", num2,"=", subtract(num1, num2))

elif choice == '3':
     print (num1, "*", num2,"=", multiply(num1, num2))

elif choice == '4':
     print (num1, "/", num2,"=", divide(num1, num2))

elif choice == '5':
     print (num1, "%", num2,"=", modulo(num1, num2))

elif choice == '6':
     print (num1, "^", num2,"=", power(num1, num2))

else:
    print("invalid input")
