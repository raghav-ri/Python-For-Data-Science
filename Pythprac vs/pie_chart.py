import pandas as pd
import matplotlib.pyplot as plt
data=pd.DataFrame({
    "Country":["India","England","Australia","South Africa","New Zealand","Pakistan","Afghanistan","Bangladesh","Sri Lanka","West Indies","Afganistan"],
    "World_Cup_Matches_Won":[63,48,69,38,59,49,8,12,35,43,8]
})
labe=data['Country']
size=data['World_Cup_Matches_Won']
plt.pie(size,labels=labe,autopct='%1.1f%%',colors=['r','g','b','y','c','m','k','w','r','g','b'])
plt.axis('equal')
plt.title("World Cup Matches Won")
plt.show()