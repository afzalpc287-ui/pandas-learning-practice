import pandas as pd
data={
    "Name":['Afzal','Amjad','Suhaib','Aasim','Abdul',"sahil","imran","chandan"],
    "Age":[20,19,19,26,23,28,22,21],
    "Salary":[100000,80000,60000,120000,110000,18000,80000,90000],
    "Performance":[90,90,75,100,90,30,85,95]
}
df=pd.DataFrame(data)
print("Sample DAta")
print(df)
#we have given the data and print the selecting columns and filtered rows
#Select single Column
print("Single column")
print(df['Name'])
#Selecting Multiple Columns
print("Selecting Multiple Columns")
print(df[["Name","Salary"]])
#Filtering Single Rows
print("Filtered Single Row")
highest_salary=df[df['Salary']<100000]
print("filter employe salary lower than 100k")
print(highest_salary)
#Filtering Multiple Rows
print("filtered multiple rows")
filter=df[(df['Salary']<100000)&(df['Age']<20)]
print("filtered employe salary is <100k and age<20")
print(filter)
#Filtering Multiple Row Through OR Operator
print("using OR Operator ROWs")
filter_or=df[(df['Salary']<90000)|(df['Age']<20)]
print(filter_or)