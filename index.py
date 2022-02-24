from os import sep
from tkinter.messagebox import QUESTION
import xlrd 
import random 
import pandas

work_book = pandas.read_excel(r"C:\Users\user\Desktop\Question-Paper-Generator\Questions_database1.xlsx")

df = pandas.DataFrame(work_book)
for i in range(1,10):
    var=df.sample(n=1)
    print('\n')
    print(i,".",sep='',end=' ')
    print('\n'.join(var.to_string(index=False).split('\n')[1:]))
