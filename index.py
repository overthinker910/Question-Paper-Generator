from operator import index
import xlrd 
import pandas

work_book = pandas.read_excel(r"C:\Users\user\Desktop\Question-Paper-Generator\Questions_database1.xlsx")
var_index1=[]
score=0
df = pandas.DataFrame(work_book)
j=0
for i in range(1,5):
    var=df.sample(n=1)
    var_index=var.index.tolist()
    var_index1.append(var_index[0]+2)
    print('\n')
    print(i,".",sep='',end=' ')
    print(var.to_string(index=False).split('\n')[1].split("?")[0]+"?")
    str=input("Enter the answer: ")
    if str==df.iloc[var_index1[j]-2,1].lower():
        score+=2
    j=j+1

for i in range(len(var_index)):
    var_index1.append(var_index[i])

var_index1.remove(var_index1[-1])
    
print("\n\nThe score of your test is: ")
print(score)

print("\nFind below the answers of this test: ")
for i in range(0,4):
    print(i+1,".",sep='',end=' ')
    print(df.iloc[var_index1[i]-2,1])

print()

#test comment