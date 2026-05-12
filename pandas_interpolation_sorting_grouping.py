#Interpolation
import pandas as pd
data={
    "Time":[1,2,None,4,5,6,None,8,9,10,None,12],
    "Value":[10,20,30,None,50,60,70,None,90,100,None,120]
}
df=pd.DataFrame(data)
print("Before Interpolation Data")
print(df)
print("After Time Interpolation Data")
Inter1=df["Time"]=df["Time"].interpolate(method="linear")
print(df)
print("After Both Interpolation Dta")
Inter2=df["Value"]=df["Value"].interpolate(method="linear")
print(df)
#Sorting Data
import pandas as pd
data1={
    "Name":["Amjad","Qadir","Suhaib","Bablu","Chintu","Danish"],
    "Age":[20,30,20,30,38,38],
    "Salary":[50000,78000,80000,450000,95000,100000],
}
df=pd.DataFrame(data1)
print("Without any Command Data")
print(df)
print("After Singe Sort Data by Age")
single_sort=df.sort_values("Age")
print(single_sort)
print("After sorting Data by Age in Ascending order")
sorting=df.sort_values("Age",ascending=False)
print(sorting)
#Aggregattion
print("After Aggregation Data")
print("Average Salary Data")
avg_salary=df["Salary"].mean()
print(avg_salary)
print("Minimum Salary Data")
min_salary=df["Salary"].min()
print(min_salary)
print("Max Age Data")
max_age=df["Age"].max()
print(max_age)
#Grouping
print("After Grouping Data")
first=df.groupby("Age")["Salary"].sum()
print(first)
print("After Multiple Grouping Data")
second=df.groupby(["Age","Name"])["Salary"].sum()
print(second)
