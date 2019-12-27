import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')

# PARSE DATA INTO STRUCTURES
categories = data.columns.values
districts = [item[-2:] for item in data[categories[0]]] #e.g. 02 (from District 02)
enrollment = data[categories[2]] #e.g. 1239219
attendance = (data[categories[1]] / 100) * enrollment #e.g. 123921.9 (from 10/100 * 1239219) 

# STYLE PLOT
font = {'family' : 'Georgia',
        'weight' : 'regular',
        'size'   : 15}

plt.rc('font', **font)
plt.rcParams['axes.edgecolor']='#333F4B'
plt.rcParams['axes.linewidth']=0.8
plt.rcParams['xtick.color']='#333F4B'
plt.rcParams['ytick.color']='#333F4B'

#INITIALIZE (MATLAB STYLE)
plt.figure(figsize=(15,7.5))

# SET DEFAULTS
width=0.8
tickfq=5000

plt.gca().set_facecolor((0.05, 0.55, 0.10, 0.1)) #change axes background to green (RGBA)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.yticks(np.arange(0, max(enrollment), tickfq)) #change tick frequency

# LABELS
plt.xlabel('DISTRICTS')
plt.ylabel('NUMBER OF STUDENTS')
plt.title('STUDENT ENROLLMENT/ATTENDANCE BY DISTRICT IN NYC\n2010 - 2011')

# PLOTS (not including last 3 special columns)
plt.bar(districts[0:-2], enrollment[0:-2], color ='white', edgecolor='#333F4B', width=width, label='Enrollment')
plt.bar(districts[0:-2], attendance[0:-2], color ='green', edgecolor='black', alpha=0.5, width=width/2, label='Attendance')
plt.legend()

#SAVE OUTPUT
#plt.show()
plt.savefig('forest_graph.png')
