import random

data = [None] * 17

for i in range(len(data) ):
    j = random.randint(1,30)
    data[i] = j

print("Unsorted Data:")
print(data)
print("\nsorting Data:")

for scanIndex in range(0, len(data)):
    minIndex = scanIndex

    for compIndex in range(scanIndex + 1, len(data)):
        if data[compIndex] < data[minIndex]:
            minIndex = compIndex

    if minIndex != scanIndex:
        data[scanIndex], data[minIndex] = \
                         data[minIndex], data[scanIndex]
        print(data)
