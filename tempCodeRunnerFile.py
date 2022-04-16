from operator import index
import string, xlrd
import pandas, random

import openpyxl

#loading the workbook in wb
wb = openpyxl.load_workbook("questions/aoa_excel.xlsx")

#cheching the sheets present in that workbook
sheets = wb.sheetnames
#print(sheets)

#storing the Sheet1 in sheet1 to print column values
sh1 = wb['Sheet1']

#a simple way to print any value inside the cell
#without any problem
data = sh1['A2'].value
print(type(data))

#looping it
questions_index = []
no_of_questions=2
while no_of_questions<7:
    column_value = 'A'
    row_value = random.randint(2, 26)
    answer_value = column_value + str(row_value)
    answer_value = str(answer_value)

    #appending each question loction in this array for future use
    questions_index.append(answer_value)
    
    #print(answer_value)
    data = sh1["{}".format(answer_value)].value
    print(data)
    i=i+1
