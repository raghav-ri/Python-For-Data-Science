import pandas as pd

df1 = pd.DataFrame({
    'Eid': [1, 2, 3],
    'Salary': [5000, 20000, 60000]
})

df2 = pd.DataFrame({
    'Duration': [4, 5, 6],
    'Joining_date': [31, 12, 30]
})

result =df1.join(df2)
print(result)


#result=df.groupby('Department')['Salary'].mean()



