#word = str(input("Enter the word to search for in UPPERCASE: "))

puzzleword = ['S','C','O','R','E']

s = ''
for i in range(len(puzzleword)):
    t = puzzleword[i]
    s = s + t
##
p = []
q = []
r = []


puzzlewordForward = []
puzzlewordPositionsForward = []

rows = int(input("Rows: "))
columns = int(input("Columns: "))

for row in range(rows):
    
    for column in range(columns):
        #print(column)
        q.append(column)
        #print(q)
        if column == 17:
            p.append(q)
            #print(q)
            #print(p)
            if row != 17:
                q.clear()



def checkforward(Row, Column):
	if Column < (rows - len(word)):
		for columns in range(Column, Column + len(word)):
			puzzlewordForward.append(puzzle[Row][columns])
			puzzlewordPositionsForward.append([Row, columns])
		s = 0
		for i in range(len(puzzlewordForward)):
			t = puzzlewordForward[i]
			s = s + t
		if s == word:
			print(word,"found!")
			print(puzzlewordPositionsForward)
		else:
			puzzlewordPositionsForward.clear()

word = int(input("No to find: "))

for row in range(0, rows):
    for column in range(0, columns):
        if p[row][column] == word[0]:
            checkforward(rows, columns)

#for i in range(0, rows):
#m.append(p)

print("Final Table:\n")
    
for row in range(rows):
    for column in range(columns):
        #if row == p[0][0] and column == p[0][1]:

        print(p[row][column], end='      ')

        if column == 17:
            print('\n')
          

