#calling a mathematical function to perform a task
import cmath
a = int(input("Enter the first number"))
#the above statement allows a user to enter the first number
b = int(input("Enter the second number"))
#the above statement allows a user to enter the second number
c = int (input("Enter the third number"))
#the above statement allows a user to enter the third number
d = (b**a)-(b*a*c)
x1 = (-b-cmath.sqrt (d))/(a*a)
x2 = (-b+cmath.sqrt (d))/(a*a)
#the above three lines of codes do the main calculation
print ("the answers are {0} and {1}", format (x1,x2))
#the above line of code will display the output
