#simple calculator
def add (x,y):
    return x+y
def subtract (x,y):
    return x-y
def multiply (x,y):
    return x*y
def divide (x,y):
    return x/y
def square (x,y):
    return (x*x)

print ("wetin you wan do?")
print ("1.Add")
print ("2.subtract")
print ("3.multiply")
print ("4.divide")
print ("5.square")

choice = input ("enter choice (1/2/3/4/5): ")
num1 = int (input ("wetin be first number: "))
num2 = int (input ("wetin be second number: "))
if choice == '1':
        print (num1, "+", num2, "=", add (num1, num2))
elif choice == '2': 
        print (num1, "-", num2, "=", subtract (num1, num2))
elif choice == '3':
        print (num1, "*", num2, "=", multiply (num1, num2))
elif choice == '4':
        print (num1, "/", num2, "=", divide (num1, num2))
elif choice == '5':
        print (num1, "square is", square (num1, num1))

else:
            print ("invalid input")
