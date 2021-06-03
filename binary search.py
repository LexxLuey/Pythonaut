def search(searchList, key):
    mid = int(len(searchList) / 2)
    print("\nSearching midpoint at ", str(searchList[mid]))

    if mid == 0:
        print("Key Not Found!")
        return key

    elif key == searchList[mid]:
        print("Key Found!")
        return searchList[mid]

    elif key > searchList[mid]:
        print("searchList now contains: \n ",
            searchList[mid:len(searchList)])
        search(searchList[mid:len(searchList)], key)

    else:
        print("searchList now contains: \n ",
            searchList[0:mid])
        search(searchList[0:mid], key)

aList = list(range(1, 50))

yes = 1
no = 0

n = int(input("\nEnter the number that you want to find: "))

search(aList, n)

continueUsing = int(input("\nDo you want to continue? \nPress 1 for YES and 0 for No: "))

while(continueUsing != 0):
    n = int(input("\nEnter the number that you want to find: "))
    search(aList, n)
    continueUsing = int(input("\nDo you want to continue? \nPress 1 for YES and 0 for No: "))
