import random

data = [None] * 17


for i in range(len(data) ):
    j = random.randint(1,30)
    data[i] = j

data2 = data.copy()

data3 = data.copy()

print("Unsorted Data:")
print(data)


print("\nInsert sorting Data:")
for scanIndex in range(1, len(data)):
    temp = data[scanIndex]

    minIndex = scanIndex

    while minIndex > 0 and temp < data[minIndex - 1]:
        data[minIndex] = data[minIndex - 1]
        minIndex -= 1

    data[minIndex] = temp

    print(data)

print("\nUnsorted Data:")
print(data2)


print("\nSelect sorting Data:")
for scanIndex in range(0, len(data2)):
    minIndex = scanIndex

    for compIndex in range(scanIndex + 1, len(data2)):
        if data2[compIndex] < data2[minIndex]:
            minIndex = compIndex

    if minIndex != scanIndex:
        data2[scanIndex], data2[minIndex] = \
                         data2[minIndex], data2[scanIndex]
        print(data2)

def mergeSort(list):
    # Determine whether the list is broken into
    # individual pieces.
    if len(list) < 2:
        return list

    # Find the middle of the list.
    middle = len(list)//2

    # Break the list into two pieces.
    left = mergeSort(list[:middle])
    right = mergeSort(list[middle:])

    # Merge the two sorted pieces into a larger piece.
    print("Left side: ", left)
    print("Right side: ", right)
    merged = merge(left, right)
    print("Merged ", merged)
    return merged

def merge(left, right):
    # When the left side or the right side is empty,
    # it means that this is an individual item and is
    # already sorted.
    if not len(left):
        return left
    if not len(right):
        return right

    # Define variables used to merge the two pieces.
    result = []
    leftIndex = 0
    rightIndex = 0
    totalLen = len(left) + len(right)

    # Keep working until all of the items are merged.
    while (len(result) < totalLen):
        # Perform the required comparisons and merge
        # the pieces according to value.
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex+= 1
        else:
            result.append(right[rightIndex])
            rightIndex+= 1

    # When the left side or the right side is longer,
    # add the remaining elements to the result.
        if leftIndex == len(left) or \
           rightIndex == len(right):
            result.extend(left[leftIndex:]
                          or right[rightIndex:])
            break

    return result

print("\nUnsorted Data:")
print(data3)

print("\nMerge sorting Data:")

mergeSort(data3)

