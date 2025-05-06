import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Name": ["Ravi", "Nayan", "Deepak", "Vishal", "Rahul"],
    "Age": [18, 19, 20, 21, 22],
    "Marks": [90, 92, 89, 78, 85]
})
print(data.to_string(index=False))

avg = data["Marks"].mean()

print("Student having more than average marks:")
for i in range(len(data)):
    if data['Marks'][i] > avg:
        print(data['Name'][i])


data['Percentage'] = data['Marks'] / 100 * 100

print(data)
data['Normalized_Marks'] = (data['Marks'] - data['Marks'].min()) / (data['Marks'].max() - data['Marks'].min())

print(data['Normalized_Marks'])



print()
x=data['Name']
y=data['Marks']
plt.bar(x,y,color='green',width=0.4)
plt.xlabel("Name")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()

data['Normalized Marks']=(data['Marks']-data['Marks'].min())/(data['Marks'].max()-data['Marks'].min())
