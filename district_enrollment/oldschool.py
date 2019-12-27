import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')

# PARSE DATA INTO STRUCTURES
stuff = list(data.values)
districts = []
attendance = []
enrollment = []
for item in stuff:
    districts.append(item[0][-2:]) #only take last 2 characters (e.g. 01 from DISTRICT 01)
    attendance.append(item[2] * (item[1]/100)) #enrollment * percent/100
    enrollment.append(item[2])

# STYLE PLOT
font = {'family' : 'Georgia',
        'weight' : 'regular',
        'size'   : 15}

plt.rc('font', **font)
plt.rcParams['axes.edgecolor']='#333F4B'
plt.rcParams['axes.linewidth']=0.8
plt.rcParams['xtick.color']='#333F4B'
plt.rcParams['ytick.color']='#333F4B'

#INITIALIZE
plt.figure(figsize=(15,7.5))
ax = plt.gca()

# SET DEFAULTS
width=0.8
tickfq=5000

ax.set_facecolor((0.05, 0.55, 0.10, 0.1)) #change background to green RGBA
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.yticks(np.arange(0, max(enrollment), tickfq)) #change tick frequency

# LABELS
plt.xlabel('DISTRICTS')
plt.ylabel('NUMBER OF STUDENTS')
plt.title('STUDENT ENROLLMENT/ATTENDANCE BY DISTRICT')

# PLOTS
plt.bar(districts[0:-2], enrollment[0:-2], color = 'white',edgecolor='#333F4B', width=width, label='Enrollment')
plt.bar(districts[0:-2], attendance[0:-2], color = 'green', edgecolor='black', alpha = 0.5, width=0.5 * width, label='Attendance')
plt.legend()

#SAVE OUTPUT
#plt.show()
plt.savefig('forest_graph.png')