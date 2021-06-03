import cmath

factors = []

end = 0

while end != 1:

    def factorz():
        num = int(input("\nEnter the number that you want its factors: "))

        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)

        print ("\nThe factors of ",num," are: ")
        print ("\n",factors)

    factorz()

    

    print("\nThe equation is in the format Ax^2 + Bx + C: ")

    A = int(input("\nEnter the coefficient of x^2: "))

    B = int(input("\nEnter the coefficient of x: "))

    C = int(input("\nEnter the constant: "))

    product = A * C

    for i in range(1, product + 1):
            if product % i == 0:
                factors.append(i)

    print (factors)
    
    for i in factors:
        for j in reversed(factors):
            Z = i + j
            Y = j + i
            X = i - j
            W = j - i
        
            if Z == B or Y == B or X == B or W == B:
               
                if i * j == product:

                    print("\nThe True factors of the equation are ",i," and ", j)
                    
                break
            
    
    end = int(input( "\nDo you wanna Quit? 1 - YES, 0 - NO: \n"))

    factors.clear()
