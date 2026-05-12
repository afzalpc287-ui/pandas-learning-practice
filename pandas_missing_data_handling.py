#Handling Missing Data
import pandas as pd
data={
    "Name":['Afzal','Amjad','Suhaib','Aasim','Abdul',None,"Imran","chandan"],
    "Age":[20,19,19,26,23,None,22,21],
    "Salary":[100000,80000,60000,120000,110000,None,80000,90000],
    "Performance":[90,90,75,100,90,None,85,95]
}
df=pd.DataFrame(data)
print("Missing value Data")
print(df)
#We have this missing value data 
#Now Find out the missing value
print("Where Value is Missing in this Data")
print(df.isnull())
#How to find how many value is missing
print("How Many Values is Missing in this Data")
print(df.isnull().sum())
"""Handling the Missing Data
We have two option for handle the missing data
1st is delete the missing data
2nd fill out the missing data"""
#Delete the Missing Data
print("Deletd Missing Data")
deleted=(df.dropna())
print(deleted)
#Fillout the Missing data
print("Filling missing data")
Filling=df.fillna(0)
print(Filling)
#Filling data by self
print("---After Filling Data---")
filling={"Name":"Sahil",
         "Age":28,
         "Salary":18000,
         "Performance":50
         }
filling_value=df.fillna(value=filling)
print(filling_value)

