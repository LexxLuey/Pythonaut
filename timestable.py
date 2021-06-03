num = int
ranz = int
status = 0
while status == 0:
    num = int(input("what multiplication table you want?"))
    ranz = int(input("What the range?"))
    for i in range(1,ranz):
        print(num,'x',i,'=',num*i)
    status = int(input("wanna continue? enter 1 to quit or 0 to continue."))
    if status == 1:
        break
print ("bye")
        
    
        
