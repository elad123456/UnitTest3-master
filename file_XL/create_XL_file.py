from openpyxl import *
# create XL file with values
workbook = load_workbook(filename="test.xlsx")
sheet = workbook.active

sheet["A3"] = "liav"
sheet["B3"] = "bar-on!"

workbook.save(filename="test.xlsx")
