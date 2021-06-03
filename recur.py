def factorial(n):
    print("factorial called with n = ", str(n))
    if n == 1 or n == 0:
        print("Ending condition met.")
        return 1
    else:
        return n * factorial(n-1)

n = int(input("'Enter the number that you want it's factorial: "))

print(factorial(n))
