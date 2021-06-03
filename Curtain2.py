__version__ = 0.2
__maintainer__ = "maintainer@website.com"
__status__ = "Prototype"
# To start with, all the measurements will be in cm.
# I will assume that the roll of material is going to be 140cm
# and that the price per metre will be 5 units of currency.
roll_width = 140
price_per_metre = 5
# Prompt the user to input the window measurements in cm.
window_height = input('Enter the height of the window (cm): ')
window_width = input('Enter the width of the window (cm): ')
# Print headers for the rather basic trace table.
print()
print('\twidth\theight\twidths\ttotal\tprice\tshorter?\twider?')
# I need to add a bit for the hems.
# First, I must convert the string into a number.
# Otherwise, I will get an error if I try to perform arithmetic on a
# text string.
curtain_width = (float(window_width) * 0.75) + 20
print('\t', round(curtain_width, 2))
curtain_length = float(window_height) + 15
print('\t\t', round(curtain_length, 2))
# Now. I need to work out how many widths of cloth will be needed
# and figure out the total length of material for each curtain (in cm still).
# If the length of the curtains is less than the roll_width, I can turn the
# whole thing on its side and just use one width of fabric, but if the curtains
# need to be both longer and wider than the roll_width, then I have a further
# problem: If the extra material required is less than half the roll_width, I
# would need to buy an additional width of material at the same length. If it
# is more than half, then I would need to buy two additional widths.
print('\t\t\t\t\t\t', curtain_length < roll_width)
print('\t\t\t\t\t\t\t', curtain_width > roll_width)
if curtain_length < roll_width:
    total_length = (curtain_width * 2) / 100
elif curtain_width > roll_width:
    widths = int(curtain_width/roll_width)
    extra_material = curtain_width%roll_width
    if extra_material < (roll_width / 2):
        widths +=1
    if extra_material > (roll_width / 2):
        widths +=2
        print('\t\t\t', widths)
        total_length = (curtain_length * widths) / 100
        print("You need", round(total_length, 2), "meters of cloth, costing: ", round(price, 2))
else:
    total_length = (curtain_length * 2) / 100
    print('\t\t\t\t', round(total_length, 2))
    # Finally I need to work out how much it will cost
    # Rounded to two decimal places using the built-in round() function
    price = total_length * price_per_metre
    print('\t\t\t\t\t', round(price, 2))
    # And print out the result
    price = total_length * price_per_metre
    total_length = (curtain_length * 2) / 100
    print("You need", round(total_length, 2), "meters of cloth, costing: ", round(price, 2))
