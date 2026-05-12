import pandas as pd
fi={
    "Name":['Afzal','Amjad','Suhaib'],
    "Age":[20,18,18],
    "City":['Delhi','Baghpat','Ghaziabad']
}
data=pd.DataFrame(fi)
print(data)
data.to_csv("output.csv",index=False)
data.to_excel("output.xlsx",index=False)
data.to_json("output.jsan",index=False)

