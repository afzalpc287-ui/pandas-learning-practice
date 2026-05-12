#Merging and Joining
import pandas as pd
df1=pd.DataFrame({
    'CustomerID':[1,2,3],
    'Name':['Afzal','Abdul','Amjad']
})
df2=pd.DataFrame({
    'CustomerID':[1,2,4],
    'Salary':[10,20,30]
})
print('inner join')
print(pd.merge(df1,df2,on='CustomerID',how='inner'))
print('outer join')
print(pd.merge(df1,df2,on='CustomerID',how='outer'))
print('right join')
print(pd.merge(df1,df2,on='CustomerID',how='right'))
print('left join')
print(pd.merge(df1,df2,on='CustomerID',how='left'))
#ConCotinate
import pandas as pd
df_Region1=pd.DataFrame({
    'CustomerID':[1,2],
    'Name':['Afzal','Abdul']
})
df_Region2=pd.DataFrame({
    'CustomerID':[1,2],
    'Name':['Amjad','Suhiab']
})
print('Vertical Concotinate')
df_Con=pd.concat([df_Region1,df_Region2],axis=1,ignore_index=True)
print(df_Con)
print('Horizontal Concotinate')
df_Con2=pd.concat([df_Region1,df_Region2],axis=0,ignore_index=True)
print(df_Con2)