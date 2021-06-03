rowsOfChair = [[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],]


delegate = 1
count = 0

for row in range(0, len(rowsOfChair)):
	if row == 0:
		for seat in range(0, 5):
			if seat == 1 or seat == 3:
				rowsOfChair[row][seat] = delegate
				count += 1

	if row == 19:
		for seat in range(0, 5):
			if rowsOfChair[row - 1][seat] == 0:
				rowsOfChair[row][seat] = delegate
				count += 1

	for seat in range(0, 5):
		if seat == 0:
			if rowsOfChair[row - 1][seat] == 0 and rowsOfChair[row + 1][seat] == 0 and rowsOfChair[row][seat + 1] == 0:
				rowsOfChair[row][seat] = delegate
				count += 1

		if seat == 4:
			if rowsOfChair[row - 1][seat] == 0 and rowsOfChair[row + 1][seat] == 0 and rowsOfChair[row][seat - 1] == 0:
				rowsOfChair[row][seat] = delegate
				count += 1

		if rowsOfChair[row][seat] == 0:
			if rowsOfChair[row - 1][seat] == 0 and rowsOfChair[row + 1][seat] == 0 and rowsOfChair[row][seat - 1] == 0 and rowsOfChair[row][seat + 1] == 0:
				rowsOfChair[row][seat] = delegate
				count += 1


print("Sitting Arrangement: \n")

def displayTable():
	for row in range(0,len(rowsOfChair)):
		for seat in range(0,5):
			print(rowsOfChair[row][seat], end=' ')

			if seat == 4:
				print('\t')
displayTable()

print("Number of seated delegates: ", count)
print("Number of seats: ", len(rowsOfChair) * 5)
print("Number of empty seats: ", (len(rowsOfChair) * 5) - count)
