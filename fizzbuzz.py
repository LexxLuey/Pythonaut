def fizz_buzz(x):
    
    a = x % 3
    b = x % 5

    if (a == 0):
        if (b == 0):
            return ("FizzBuzz")
        return ("Fizz")
    elif (b == 0):
        return ("Buzz")
    else:
        return x
    
while True:
    a = input('Do you want to continue? ')
    if a.lower() != 'y':
        break
    num = int (input("Enter a number: "))
    print ("The number is a ",fizz_buzz(num))
