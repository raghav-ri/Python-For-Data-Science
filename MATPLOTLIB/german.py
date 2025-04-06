import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\RAMAN\Desktop\Python CSV\german.csv', encoding='ISO-8859-1')

print("Unique value credit history", df['Credit history'].unique())
df['CREDIT BY 10'] = df['Credit amount'] / 10
print(df['Credit amount'].value_counts())
print(df['Purpose'].value_counts())

# Corrected color list
df['Purpose'].value_counts().plot(kind='bar', color=['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'grey', 'cyan', 'magenta', 'violet', 'indigo', 'maroon', 'olive', 'navy', 'teal', 'aqua', 'lime', 'fuchsia', 'silver', 'white'])
plt.xlabel('Purpose')
plt.ylabel('Count')
plt.title('Purpose of Credit')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()

# plt.hist(df['Credit amount'], bins=30, edgecolor='green')
# plt.xlabel('Credit Amount')
# plt.ylabel('Frequency')
# plt.title('Credit Amount Distribution')
# plt.show()