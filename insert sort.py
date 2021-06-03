
import random

data = [None] * 17

for i in range(len(data) ):
    j = random.randint(1,30)
    data[i] = j

print("Unsorted Data:")
print(data)
print("\nsorting Data:")


for scanIndex in range(1, len(data)):
    temp = data[scanIndex]

    minIndex = scanIndex

    while minIndex > 0 and temp < data[minIndex - 1]:
        data[minIndex] = data[minIndex - 1]
        minIndex -= 1

    data[minIndex] = temp

    print(data)
