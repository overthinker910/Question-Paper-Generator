from operator import index
import xlrd 
import pandas

work_book = pandas.read_excel(r"C:\Users\user\Desktop\Question-Paper-Generator\Questions_database1.xlsx")
var_index1=[]
df = pandas.DataFrame(work_book)
seq=df[["Question"]]
for i in range(1,10):
    var=df.sample(n=1)
    var_index=var.index.tolist()
    var_index1.append(var_index[0]+2)
    print(var_index[0]+2)
    print('\n')
    print(i,".",sep='',end=' ')
    print(var.to_string(index=False).split('\n')[1].split("?")[0])
    
for i in range(len(var_index)):
    var_index1.append(var_index[i])

var_index1.remove(var_index1[-1])
print(var_index1)

print(df.iloc[var_index1[0],1])
#code prints 10 questions in a random order