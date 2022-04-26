from operator import index
import string, xlrd
import pandas, random
from fpdf import FPDF
import openpyxl

class PDF(FPDF):
    def header(self):
        #logo
        self.image('static/lion.jpg', 10, 8, 25)
        #font
        self.set_font('helvetica', 'B', 20)
        #title
        self.cell(0, 10, 'Question Paper', ln=1, align='C')
        #line-break
        self.ln(20)

pdf = PDF('P', 'mm', 'Letter')



def generate_ques(pathToQues):
    #loading the workbook in wb
    #!!!!add your path for the excel sheet here!!!!
    #SHREYA'S PATH: C:\Users\shrey\question paper\Question-Paper-Generator\questions
    wb = openpyxl.load_workbook(r'C:\\Users\\farde\\OneDrive\\Desktop\\QPG\\Question-Paper-Generator\\questions\\'+f'{pathToQues}.xlsx')
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

    #generating the pdf
    #adding a page
    pdf.add_page()

    #specifying fonts
    pdf.set_font('helvetica', '', 16)
    
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

        pdf.cell(40, 30, f'{i-1}'+'. '+data, ln=True)

    pdf.output('pdf_1.pdf')