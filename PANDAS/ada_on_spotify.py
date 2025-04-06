import pandas as pd
import numpy as np
df=pd.read_csv(r'C:\Users\RAMAN\Desktop\Python CSV\Spotify_Youtube.csv')
print("Info about data frame:",df.info())
print("First 15 records: ",df.head(15))
print("Last 15 records: ",df.tail())

print("Statical description of data frame: ",df.describe())
print("Missing value count: ",df.isnull().sum())

# Null values of numeric column is being replaced by mean of their respective data
num_cols = ['Danceability', 'Energy', 'Key', 'Loudness', 'Speechiness',
                'Acousticness', 'Instrumentalness', 'Liveness', 'Valence',
                'Tempo', 'Duration_ms', 'Stream', 'Views', 'Likes', 'Comments']
for col in num_cols:
    df[col].fillna(df[col].mean(), inplace=True)

#  Null values of text column is being replaced by unknown 
text_cols = ['Title', 'Channel', 'Description', 'Url_youtube']
for col in text_cols:
    df[col].fillna("Unknown", inplace=True)
# datatype changed from float to int 
int_cols = ['Stream', 'Views', 'Likes', 'Comments']
for col in int_cols:
    df[col] = df[col].astype(int)

df.drop_duplicates(inplace=True)

print("Dataset cleaned successfully!")
