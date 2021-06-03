import random

Num1 = random.randint(2,1111)
#Num2 = random.randint(2,1111)
Num2 = Num1 + random.randint(1,20)

if Num2 == Num1:
	Num2 = random.randint(2,1111)

factors1 = []
factors2 = []
commonFactors = []


for num in range(1, Num1 + 1):
	if Num1 % num == 0:
		factors1.append(num)

for num in range(1, Num2 + 1):
	if Num2 % num == 0:
		factors2.append(num)

factors1.sort()
factors2.sort()

print(factors1)
print(factors2)

for i in factors1:
	for j in factors2:
		if i == j:
			commonFactors.append(i)

commonFactors.sort()
HCF = max(commonFactors)

print(commonFactors)
print(HCF)

print("What is the HCF of ", Num1," and " ,Num2, " ?\n")

answer = int(input("Enter your answer: "))

if HCF == answer: 
    print ("Your answer is correct. ",HCF," is the HCF.") 
else: 
    print ("Your answer is incorrect",HCF," is the HCF.") 
