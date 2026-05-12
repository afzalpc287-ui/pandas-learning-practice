import pandas as pd
#how to read files in pandas
fo_csv=pd.read_csv("sales_data_sample.csv",encoding="latin1")
print(fo_csv)
fo_json=pd.read_json("sample_data.json")
print(fo_json)
fo_xcl=pd.read_excel("SampleSuperstore.xlsx")
print(fo_xcl)