#Indices function  New General Maths
import random
import cmath

count = 0
num = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

while count <= 10:


    num1 = random.randint(0,25)

    Num = num[num1] 
    #num2 = random.randint(1,100)

    pow1 = random.randint(1,100)
    pow2 = random.randint(1,100)

    operator = random.randint(1,2)



    if operator == 1: 
        qText = ("{}^{}  x  {}^{} = {}^?").format(Num, pow1, Num, pow2, Num)

        print (qText)

        user = int(input())
        
        ans = pow1 + pow2

        if user == ans:
            print("CORRECT!!! That is the answer. It is ",Num,"^",ans)
        else:
            print("INCORRECT!!! That is not the answer. It is ",Num,"^",ans)

    else: 
        qText = ("{}^{} ÷ {}^{} = {}^?").format(Num, pow1, Num, pow2, Num)

        print (qText)

        user = int(input())
        
        ans = pow1 - pow2

        if user == ans:
            print("CORRECT!!! That is the answer.It is ",Num,"^",ans)
        else:
            print("INCORRECT!!! That is not the answer. It is ",Num,"^",ans)

        count == count + 1

