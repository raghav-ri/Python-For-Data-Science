import pandas as pd
import matplotlib.pyplot as plt


data = pd.DataFrame({
    'Cricketers': ["Rohit Sharma", "Virat Kohli", "MS Dhoni","KL Rahul","Rishabh Pant"],
    'Runs': [60, 70, 80,36,42]
})


plt.pie(data['Runs'], labels=data['Cricketers'], autopct='%1.2f%%')


plt.title('Runs scored by Cricketers')


plt.show()

