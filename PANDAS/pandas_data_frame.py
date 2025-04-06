import pandas as pd
data ={
    "Name":['John','Alice','Bob','Emma'],
    "Age":[25,23,24,22],
    "Gender":['Male','Female','Male','Female'],
    "Marks":[85,90,75,95]

}
df=pd.DataFrame(data);
print(df)
print()
#print(df.loc[[0]],df.loc[[1]])    # for first row and column
# print(df.iloc[2,3]) # printing particular
#print(df.loc[0:2,'Name':'Age']) # using loc  printing required columns and rows
# for col in df:
#     print(col)
print(df.info()) # information of columns
print(df.describe()) # statistical information of record
print()
print(df.sort_values(by="Age"))
# join merge and concat