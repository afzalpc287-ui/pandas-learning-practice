#Adding the columns in data
import pandas as pd
data={
    "Name":['Afzal','Amjad','Suhaib','Aasim','Abdul',"sahil","imran","chandan"],
    "Age":[20,19,19,26,23,28,22,21],
    "Salary":[100000,80000,60000,120000,110000,18000,80000,90000],
    "Performance":[90,90,75,100,90,30,85,95]
}
df=pd.DataFrame(data)
print(df)
#Adding on random location column
df["Bonus"]=df["Salary"]*.1
print("Modifeid data")
print(df)
#Adding on Specific location Columns
df.insert(0,"Employe Id",[202501,202502,202503,202504,202505,202506,202507,202508])
print("Modifeid data")
print(df)
#Updating  Data in one specfic column or row
df.loc[5,"Salary"]=25000
print("modifeid data")
print(df)
#Update the multiple rows in one column'
df["Salary"]=df["Salary"]*1.05
print("Modifeid Salary")
print(df)
#How to delete the columns
df.drop(columns=["Performance"],inplace=True)
print("Deleted Performance")
print(df)





