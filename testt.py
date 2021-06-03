s = 'ashley'
t = 'ash'
k = 2
n =''
startPopIndex = None
startInsIndex = None
startPop = 0
startIns = 0
space = 0
x = []
z = []
for letter in s:
    x.append(letter)
for letter in t:
    z.append(letter)

for index in range(len(x)):
    if s == t:
        k = 0
        break
    if x[index] != z[index]:
        
        
        startPopIndex = x[index]
        startInsIndex = z[index]
        startPop = index
        startIns = index
        space = len(z) - (startIns + 1)
        
        break

for index in range(startPop, len(x)):
    if s == t:
        k = 0
        break
    
    x.pop()
    k -= 1
    print(x)
    print(k)
    print(space)
    
    if k == 0 and s != t:
        break

    if not x and space != k:
        while space != k:
            k -= 1

for index in range(startIns, len(z)):
    if s == t:
        k = 0
        break
        
    if k == 0 and s != t:
        break
        
    x.append(z[index])
    k -= 1

print(x)
print(z)
if x == z or s == t and k == 0:
    print('YES')
else:
    print('NO')
            
        
