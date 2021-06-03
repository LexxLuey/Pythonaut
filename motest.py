from statistics import mode 

arr = [10, 27, 9, 10, 100, 38, 30, 32, 45, 29, 27, 29, 32, 38, 32, 38, 14, 38, 29, 30, 63, 29, 63, 91, 54, 10, 63]

deletions = 0

#Find element 'x' in array that occurs the most 
x = mode(arr)

#Delete all elements in array that are not 'x'
for value in arr:
    if value != x:
        deletions += 1
    else:
        pass
print(arr)
print(deletions)

#Count number of deletions made
