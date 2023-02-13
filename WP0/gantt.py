import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np

file = './avanceeDesTaches.csv'
data = pd.read_csv(file, parse_dates=['Start', 'End'])
output = './gantt.png'


###########################
##  1. DATA PREPARATION  ##
###########################

# project start date
proj_start = data.Start.min()
# number of days from project start to task start
data['start_num'] = (data.Start-proj_start).dt.days
# number of days from project start to end of tasks
data['end_num'] = (data.End-proj_start).dt.days
# days between start and end of each task
data['days_start_to_end'] = data.end_num - data.start_num

def color(row):
    c_dict = {
        'WP1':'#E64646',
        'WP2':'#E69646',
        'WP3':'#34D05C'}
    return c_dict[row['Group']]

data['color'] = data.apply(color, axis=1)

# days between start and current progression of each task
data['current_num'] = (data.days_start_to_end * data.Completion)


##########################
##  2. LEGEND AND PLOT  ##
##########################

fig, ax = plt.subplots(1, figsize=(16,6))

# bars
ax.barh(data.Task, data.current_num, left=data.start_num, color=data.color)
ax.barh(data.Task, data.days_start_to_end, left=data.start_num, color=data.color, alpha=0.5)

# texts
for idx, row in data.iterrows():
    ax.text(row.end_num+0.1, idx, 
            f"{int(row.Completion*100)}%", 
            va='center', alpha=0.8)
# grid
legend_elements = [Patch(facecolor=data.color.unique()[i], label=data.Group.unique()[i])  for i in range(len(data.Group.unique()))]
plt.legend(handles=legend_elements)

xticks = np.arange(0, data.end_num.max()+1, 3)
xticks_labels = pd.date_range(proj_start, end=data.End.max()).strftime("%m/%d")
xticks_minor = np.arange(0, data.end_num.max()+1, 1)
ax.set_xticks(xticks)
ax.set_xticks(xticks_minor, minor=True)
ax.set_xticklabels(xticks_labels[::3])


####################
## 3. SAVE FIGURE ##
####################

plt.savefig(output, dpi=300, bbox_inches='tight')
