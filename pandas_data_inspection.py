#how to head and tail of data
#Head is upper part Tail is lower part
import pandas as pd
data=pd.read_json("sample_Data.json")
print("Display the First 10 rows")
print(data.head(10))
print("display the last 10 rows")
print(data.tail(10))
#how to get find the info of data
import pandas as pd
data1=pd.read_json("sample_Data.json")
print("Information od data")
print(data1.info())
#Describstion of data(the all average value in data)
import pandas as pd
data2={
    "Name":['Afzal','Amjad','Suhaib','Aasim','Abdul',"sahil","imran","chandan"],
    "Age":[20,19,19,26,23,28,22,21],
    "Salary":[100000,80000,60000,120000,110000,18000,80000,90000],
    "Performance":[90,90,75,100,90,30,85,95]
}
dataframe=pd.DataFrame(data2)
print("Sample Data Frame")
print(dataframe)
print("Describtion")
print(dataframe.describe())
#Find the Shape of data
print(dataframe)
print("shape of data:",dataframe.shape)
#Find the name of columns
print(dataframe)
print("Columns Name:",dataframe.columns)