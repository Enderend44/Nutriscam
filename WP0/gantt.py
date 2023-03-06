import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np

FILE = './avanceeDesTaches.csv'
DATA = pd.read_csv(FILE, parse_dates=['Start', 'End'])
OUTPUT = './gantt.png'


###########################
##  1. DATA PREPARATION  ##
###########################

# reverse order of rows to have the last task at the bottom
DATA = DATA.iloc[::-1].reset_index(drop=True)

# project start date
proj_start = DATA.Start.min()
# number of days from project start to task start
DATA['start_num'] = (DATA.Start-proj_start).dt.days
# number of days from project start to end of tasks
DATA['end_num'] = (DATA.End-proj_start).dt.days
# days between start and end of each task
DATA['days_start_to_end'] = DATA.end_num - DATA.start_num

def color(row):
    c_dict = {
        'WP0':'#34D0E6', # blue
        'WP1':'#E64646', # red
        'WP2':'#E69646', # orange
        'WP3':'#34D05C'} # green
    return c_dict[row['Group']]

DATA['color'] = DATA.apply(color, axis=1)

# days between start and current progression of each task
DATA['current_num'] = (DATA.days_start_to_end * DATA.Completion)


##########################
##  2. LEGEND AND PLOT  ##
##########################

fig, ax = plt.subplots(1, figsize=(16,6))

# bars
ax.barh(DATA.Task, DATA.current_num, left=DATA.start_num, color=DATA.color) 
ax.barh(DATA.Task, DATA.days_start_to_end, left=DATA.start_num, color=DATA.color, alpha=0.5)

# texts
for idx, row in DATA.iterrows():
    if row.Completion < 1 and row.Completion > 0:
        ax.text(row.start_num+row.current_num+0.1, idx, 
                f"{int(row.Completion*100)}%", 
                va='center', alpha=0.8)
    
# grid
legend_elements = [Patch(facecolor=DATA.color.unique()[i], label=DATA.Group.unique()[i])  for i in range(len(DATA.Group.unique()))]
plt.legend(handles=legend_elements[::-1], loc='upper right')

# xticks and labels 
n_days = 7 # number of days between each tick
xticks = np.arange(0, DATA.end_num.max()+1, n_days)
xticks_labels = pd.date_range(proj_start, end=DATA.End.max()).strftime("%m/%d")
xticks_minor = np.arange(0, DATA.end_num.max()+1, 1)
ax.set_xticks(xticks)
ax.set_xticks(xticks_minor, minor=True)
ax.set_xticklabels(xticks_labels[::n_days])


####################
## 3. SAVE FIGURE ##
####################

plt.savefig(OUTPUT, dpi=300, bbox_inches='tight')
