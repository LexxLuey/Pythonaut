
while True:
    a = input('Do you want to continue? ')
    if a.lower() != 'y':
        break

    a = float(input('Enter a number : '))
    b = float(input('Enter another number : '))
    print(a, ' % ', b, ' = ', a % b)
    print(b, ' % ', a, ' = ', b % a)

