import matplotlib.pyplot as plt
import numpy as np


students = ['A', 'B', 'C']

math_marks = [70, 80, 90]
science_marks = [60, 70, 80]


bar_width = 0.2
x=np.arange(len(students))
plt.bar(x-bar_width/2, math_marks, color='b', width=bar_width, edgecolor='grey', label='Math')
plt.bar(x+bar_width/2, science_marks, color='r', width=bar_width, edgecolor='grey', label='Science')


plt.xlabel('Students', fontweight='bold')
plt.ylabel('Marks', fontweight='bold')
plt.title('Marks of Students in Math and Science')
plt.xticks([r + bar_width/2 for r in range(len(students))], students)


plt.legend()


plt.show()



