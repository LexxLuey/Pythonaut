__version__ = "0.1"
__maintainer__ = "maintainer@website.com"
__status__ = "Prototype"
punctuation = "#()*+,-/:;<=>? \\@^_`{|}~[]"
print()
print("***")
print()
input_string = input("Enter a text string: ")
output_string = ' '
space_flagged = False
for char in input_string:
    if char == '.':
        print(output_string)
        output_string = ' '
    elif char not in punctuation:
        output_string += char
        space_flagged = False
    else:
        if not space_flagged:
            output_string += ' '
            space_flagged = True
print(output_string)
print()
print("***")
print()
