import xlrd

filePath = xlrd.open_workbook('./ejemplo.xls')

openFile = xlrd.open_workbook('./ejemplo.xls')

sheet = openFile.sheet_by_name('Hoja1')

print('Número de filas: ', sheet.nrows)
print('Número de columnas: ', sheet.ncols)

print('\n')

for i in range(sheet.nrows):
    print(sheet.cell_value(i,0),"                   " ,sheet.cell_value(i,1))
