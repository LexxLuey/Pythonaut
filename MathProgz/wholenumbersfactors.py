import random

randomNum = random.randint(2,1111)

factors = []
answer = []

for num in range(1, randomNum + 1):
	if randomNum % num == 0:
		factors.append(num)

print("What are the factors of ", randomNum,"? \n\nEnter your answer. Enter 0 when you are done: ")

userans = 1

while userans != 0:
	userans = int(input("Enter Number: "))
	if userans == 0:
		break
	answer.append(userans)

print ("The factors of ",randomNum," are : " + str(factors)) 
print ("Your answer was : " + str(answer)) 
  
# sorting both the lists 
factors.sort() 
answer.sort() 
  
# using == to check if  
# lists are equal 
if factors == answer: 
    print ("Your answer is correct") 
else : 
    print ("Your answer is incorrect") 
