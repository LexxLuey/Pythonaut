num = int
status = 0
while status == 0:
    num = int(input("what multiplication table do you want?"))
    
    for i in range(1,12):
        print(num,'x',i,'=',num*i)
    status = int(input("wanna continue? enter 1 to quit or 0 to continue."))
    if status == 1:
        break
print ("bye")
        
    
        
