from openpyxl import *
workbook=Workbook()
sheet=workbook.active
sheet['a1']='elad'
sheet['b1']='ratner'
workbook.save(filename='hello_world.xlsx')
print(sheet['a1:c2'])