from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.cell(1,1).value = "Hello World!!!"

wb.save('It\'s test.xlsx')
