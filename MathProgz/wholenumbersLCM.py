import random

Num1 = random.randint(4,111)
Num2 = random.randint(15,111)
Num3 = random.randint(30,120)
Num4 = random.randint(50,150)

num1 = Num1
num2 = Num2
num3 = Num3
num4 = Num4

primeFactors1 = []
primeFactors2 = []
primeFactors3 = []

divAns1 = Num1
divAns2 = 0
divAns3 = 0

lower =  2
upper =  100

primeNos = []
print("Prime numbers between", lower, "and", upper, "are: ")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           primeNos.append(num)

print (primeNos)


flag = False

if flag != True:
	for j in primeNos:

		while Num1 % j == 0:
			Num1 = Num1/j

			primeFactors1.append(j)
						
			if Num1 == 1:
				flag = True

flag = False

if flag != True:
	for j in primeNos:

		while Num3 % j == 0:
			Num3 = Num3/j

			primeFactors3.append(j)
			
			if Num3 == 1:
				flag = True

flag = False

if flag != True:
	for j in primeNos:

		while Num2 % j == 0:
			Num2 = Num2/j

			
			primeFactors2.append(j)
			
			
			if Num2 == 1:
				flag = True
LCM =[]

for x in primeFactors1:
	LCM.append(x)
	for y in primeFactors2:
		if primeFactors1[x] != primeFactors2[y]:
			if primeFactors2[y] not in LCM:
				LCM.append(y)



			

print("What is the LCM of ", num1, ", ",num2, ", and ", num3, "? ")

print(primeFactors1)
print(primeFactors2)
print(primeFactors3)


