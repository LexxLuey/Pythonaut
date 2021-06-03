import random
import cmath

num1 = random.randint(1,555)

square = num1 * num1

cmath.sqrt(square)

print ("Enter the square root of ",square,": ")
num = int(input())


if num == num1:
	print("CORRECT!!! Na the square root be that.")

else:
	print("INCORRECT!!! The square root is ",num1)
