import pandas as pd
df1=pd.DataFrame(
    {
        "Department":['MARKETING','IT','HR','FINANCE','IT','MARKETING','HR'],
        "Salary":[50000,96000,63000,25000,32000,80000,61000]
    }
)
#res=df1.sort_values(by="Department")
result=df1.groupby('Department')['Salary'].mean()
print(result)
