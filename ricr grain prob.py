

def countGrains():
    grains = 1
    sumOfGrains = 1

    for board in range(2, 65):
        grains = grains * 2
        sumOfGrains += grains
        print("Board No: ",board)
        print("Current grain amount: ",grains)
        print("Total Grain so far: ",sumOfGrains)
        print( "Total amount of rice grains the king needs to pay is " ,sumOfGrains )

def fruity():
    fruits = ['mango', 'orange', 'banana', 'pineapple', 'guava', 'cashew', 'pawpaw', 'avocado', 'pear', 'lemon']
    print(fruits)
    fruits.append('coconut')
    print(fruits)
    print(fruits[0:4])
    print(fruits[2:8])

def cookieBox():
    numOfCookies = int (input("enter the total number of cookies: "))
    boxCookies = int (input("enter the number of cookies in a box: "))
    containerCookies = int (input("enter the number of cookie boxes in a container: "))

    numBox = numOfCookies//boxCookies

    numContainer = numBox//containerCookies

    leftOverCookie  = numOfCookies % boxCookies

    leftOverBox = numBox % containerCookies

    print("Total number of  Cookies: ", numOfCookies)
    print("Cookies per box: ", boxCookies)
    print("Boxes per container: ", containerCookies)
    print("Amount of Boxes needed: ", numBox)
    print("Amount of Containers needed: ", numContainer)
    print("Left over Cookies: ", leftOverCookie)
    print("Left over Boxes: ", leftOverBox)
    print((boxCookies * containerCookies))
    print(numOfCookies/(boxCookies * containerCookies))

name = 'War Kenneth'
print(name[1:-1] )

