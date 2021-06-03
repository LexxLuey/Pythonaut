age = int(input("Hello. Please Enter your age: "))
while (age > 0):
    if age <= 2:
        print("Thou art a babe.")
        age = int(input("Hello. Please Enter your age: "))
    elif age < 6:
        print("Thou art a child.")
        age = int(input("Hello. Please Enter your age: "))
    elif age < 10:
        print("Thou art a preteen.")
        age = int(input("Hello. Please Enter your age: "))
    elif age < 20:
        print("Thou art a teenager.")
        age = int(input("Hello. Please Enter your age: "))
    elif age < 30:
        print("Thou art a young adult.")
        age = int(input("Hello. Please Enter your age: "))
    elif age < 50:
        print("Thou art an adult.")
        age = int(input("Hello. Please Enter your age: "))
    elif age < 70:
        print("Thou art a middle aged person.")
        age = int(input("Hello. Please Enter your age: "))
    elif age < 200:
        print("Thou art a senior citizen.")
        age = int(input("Hello. Please Enter your age: "))
    else:
        print("Incorrect age.")
        age = int(input("Hello. Please Enter your age: "))

    
    
