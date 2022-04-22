from operator import index
import string, xlrd
import pandas, random
from fpdf import FPDF
import openpyxl
<<<<<<< HEAD

pdf = FDF('P', 'mm', 'Letter')

=======
>>>>>>> c2364ddf49fb709863bb42a3295c926fc2682efc
def generate_ques(pathToQues):
    #loading the workbook in wb
    #!!!!add your path for the excel sheet here!!!!
    #SHREYA'S PATH: C:\Users\shrey\question paper\Question-Paper-Generator\questions
    wb = openpyxl.load_workbook(r'C:\\Users\\shrey\\question paper\\Question-Paper-Generator\\questions\\'+f'{pathToQues}.xlsx')
    #"questions/aoa_excel.xlsx"
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
    i=1
    while no_of_questions<7:
        column_value = 'A'
        row_value = random.randint(2, 26)
        answer_value = column_value + str(row_value)
        answer_value = str(answer_value)

        #appending each question loction in this array for future use
        questions_index.append(answer_value)
        
        #print(answer_value)
        data = sh1["{}".format(answer_value)].value
        print(str(i) + '. '+data)
        i=i+1
        no_of_questions=no_of_questions+1

        #generating the pdf
        #adding a page
        pdf.add_page()

        #specifying fonts
        pdf.set_fonts('helvetica', '', 16)

        #adding text
        #create cell
        pdf.cell(40, 10, 'hello')