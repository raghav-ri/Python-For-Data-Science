# for dropping column df.drop(columns=['Department'])
# for rseetting index  df.reset_index(drop=True)
            # for getting the first row df.head(1)
            # for getting the last row df.tail(1)
            # for getting the first n rows df.head(n)
            # for getting the last n rows df.tail(n)
#for converting datatype df['Department']=df['Department'].astype(float)
# handling false information outlier df=df[df['Age']<100]
# df[df['Fare']<df['Fare'].quantile(0)]

import pandas as pd
url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
print(df.info())
df['Age'].fillna(df['Age'].median())
df['Ticket'].fillna(df['Ticket'].mode()[0],inplace=True)

# drop duplicates
df.drop_duplicates(inplace=True)

# converting data type
df['Fare']=df['Fare'].astype(float)

# Handling outlier
df=df[df['Age']<100]
df=df[df['Fare']<df['Fare'].quantile(0.99)]


# reset index
df.reset_index(drop=True)
print("Cleaned Dataset\n")
print(df)
