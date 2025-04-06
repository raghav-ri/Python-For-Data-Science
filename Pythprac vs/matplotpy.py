import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10]
y=[40,42,41,40,39,35,37,38,40,40]
plt.xlabel('Day')
plt.ylabel('Weather')
plt.title("Weather Report")
plt.plot(x,y,color='red',linestyle='-.',linewidth=4,marker='^',markersize=10)
plt.legend(['Temp line'],loc=4)
plt.grid(True)
plt.show()