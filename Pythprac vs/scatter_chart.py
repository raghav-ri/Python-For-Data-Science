import matplotlib.pyplot as plt
Matches_played=[15,16,78,96,45,12,36,45,78,96]
Won=[10,12,45,56,23,10,25,30,45,50]
plt.scatter(Matches_played,Won,color='r',marker='o')
plt.xlabel("Matches Played")
plt.ylabel("Matches Won")
plt.title("Matches Played vs Matches Won")
plt.show()
# Compare this snippet from line_chart.py:  
# import matplotlib.pyplot as plt
# x=[1,2,3,4,5,6,7,8,9,10]
# y=[40,42,41,40,39,35,37,38,40,40]
# plt.xlabel('Day')
# plt.ylabel('Weather')
# plt.title("Weather Report")
# plt.plot(x,y,color='red',linestyle='-.',linewidth=4,marker='^',markersize=10)
# plt.legend(['Temp line'],loc=4)
# plt.grid(True)
# plt.show()
# Compare this snippet from histogram.py:

