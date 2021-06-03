# Check the used spreadsheet space using the attribute "dimensions"
sheet.dimensions
'A1:O100'

sheet.auto_filter.ref = "A1:O100"
workbook.save(filename="sample_with_filters.xlsx")

#Adding Formulas

# Star rating is column "H"
sheet["P2"] = "=AVERAGE(H2:H100)"
workbook.save(filename="sample_formulas.xlsx")

# The helpful votes are counted on column "I"
sheet["P3"] = '=COUNTIF(I2:I100, ">0")'
workbook.save(filename="sample_formulas.xlsx")

#Adding Styles
# Import necessary style classes
from openpyxl.styles import Font, Color, Alignment, Border, Side, colors

# Create a few styles
bold_font = Font(bold=True)
big_red_text = Font(color=colors.RED, size=20)
center_aligned_text = Alignment(horizontal="center")
double_border_side = Side(border_style="double")
square_border = Border(top=double_border_side,
                       right=double_border_side,
                       bottom=double_border_side,
                       left=double_border_side)

# Style some cells!
sheet["A2"].font = bold_font
sheet["A3"].font = big_red_text
sheet["A4"].alignment = center_aligned_text
sheet["A5"].border = square_border
workbook.save(filename="sample_styles.xlsx")

#When you want to apply multiple styles to one or several cells, you can use a NamedStyle class instead, which is like a style template that you can use over and over again. Have a look at the example below:

from openpyxl.styles import NamedStyle

# Let's create a style template for the header row
header = NamedStyle(name="header")
header.font = Font(bold=True)
header.border = Border(bottom=Side(border_style="thin"))
header.alignment = Alignment(horizontal="center", vertical="center")

# Now let's apply this to all first row (header) cells
header_row = sheet[1]
for cell in header_row:
    cell.style = header

workbook.save(filename="sample_styles.xlsx")

#Conditional Formatting
#conditional formatting allows you to specify a list of styles to apply to a cell (or cell range) according to specific conditions.

from openpyxl.styles import PatternFill, colors
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import Rule

red_background = PatternFill(bgColor=colors.RED)
diff_style = DifferentialStyle(fill=red_background)
rule = Rule(type="expression", dxf=diff_style)
rule.formula = ["$H1<3"]
sheet.conditional_formatting.add("A1:O100", rule)
workbook.save("sample_conditional_formatting.xlsx")

#The ColorScale gives you the ability to create color gradients:

from openpyxl.formatting.rule import ColorScaleRule
color_scale_rule = ColorScaleRule(start_type="min",
                                  start_color=colors.RED,
                                  end_type="max",
                                  end_color=colors.GREEN)

# Again, let's add this gradient to the star ratings, column "H"
sheet.conditional_formatting.add("H2:H100", color_scale_rule)
workbook.save(filename="sample_conditional_formatting_color_scale.xlsx")

#You can also add a third color and make two gradients instead:

from openpyxl.formatting.rule import ColorScaleRule
color_scale_rule = ColorScaleRule(start_type="num",
                                  start_value=1,
                                  start_color=colors.RED,
                                  mid_type="num",
                                  mid_value=3,
                                  mid_color=colors.YELLOW,
                                  end_type="num",
                                  end_value=5,
                                  end_color=colors.GREEN)

# Again, let's add this gradient to the star ratings, column "H"
sheet.conditional_formatting.add("H2:H100", color_scale_rule)
workbook.save(filename="sample_conditional_formatting_color_scale_3.xlsx")

#The IconSet allows you to add an icon to the cell according to its value:

from openpyxl.formatting.rule import IconSetRule

icon_set_rule = IconSetRule("5Arrows", "num", [1, 2, 3, 4, 5])
sheet.conditional_formatting.add("H2:H100", icon_set_rule)
workbook.save("sample_conditional_formatting_icon_set.xlsx")

#DataBar allows you to create progress bars:

from openpyxl.formatting.rule import DataBarRule

data_bar_rule = DataBarRule(start_type="num",
                            start_value=1,
                            end_type="num",
                            end_value="5",
                            color=colors.GREEN)
sheet.conditional_formatting.add("H2:H100", data_bar_rule)
workbook.save("sample_conditional_formatting_data_bar.xlsx")