import openpyxl

wb=openpyxl.load_workbook('c://python36/example.xlsx')

type(wb)

wb.get_sheet_names()

sheet = wb.active

print(sheet['A1'].value)