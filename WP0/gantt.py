import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np

print('Starting gantt.py')

FILE = './csv/avanceeDesTaches_'
OUTPUT = './gantt/gantt_'

GANTT_DATES = ["2023-02-14", "2023-03-06", "2023-03-27", "2023-04-10"] # dates where the gantt chart is updated

HOLIDAYS_START = "2023-02-15"
HOLIDAYS_END = "2023-03-05"


for i in range(len(GANTT_DATES)):
    print('Processing file '+FILE+str(i)+'.csv')

    ###########################
    ##  1. DATA PREPARATION  ##
    ###########################

    data = pd.read_csv(FILE+str(i)+'.csv', parse_dates=['Start', 'End'])

    # reverse order of rows to have the last task at the bottom of the plot
    data = data.iloc[::-1].reset_index(drop=True)

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
            'WP0':'#34D0E6', # blue
            'WP1':'#E64646', # red
            'WP2':'#E69646', # orange
            'WP3':'#34D05C'} # green
        return c_dict[row['Group']]

    data['color'] = data.apply(color, axis=1)

    # days between start and current progression of each task
    data['current_num'] = (data.days_start_to_end * data.Completion)


    ##########################
    ##  2. LEGEND AND PLOT  ##
    ##########################

    fig, ax = plt.subplots(1, figsize=(16,6))

    # vertical line for today
    ax.axvline(x=(pd.to_datetime(GANTT_DATES[i])-proj_start).days, color='k', linestyle='--', alpha=0.5)

    # grey background for holidays
    ax.axvspan((pd.to_datetime(HOLIDAYS_START)-proj_start).days, (pd.to_datetime(HOLIDAYS_END)-proj_start).days, color='grey', alpha=0.2)

    # bars
    ax.barh(data.Task, data.current_num, left=data.start_num, color=data.color) 
    ax.barh(data.Task, data.days_start_to_end, left=data.start_num, color=data.color, alpha=0.5)

    # texts
    for idx, row in data.iterrows():
        if row.Completion < 1 and row.Completion > 0:
            ax.text(row.start_num+row.current_num+0.1, idx, 
                    f"{int(row.Completion*100)}%", 
                    va='center', alpha=0.8)

    # grid
    legend_elements = [Patch(facecolor=data.color.unique()[i], label=data.Group.unique()[i])  for i in range(len(data.Group.unique()))]
    plt.legend(handles=legend_elements[::-1], loc='upper right')

    # xticks and labels 
    xticks = np.unique(data[['start_num', 'end_num']].values)
    xticks_labels = [proj_start + pd.Timedelta(days=int(x)) for x in xticks]
    xticks_labels = [x.strftime('%d/%m') for x in xticks_labels]
    xticks_minor = np.arange(0, data.end_num.max()+1, 1)

    ax.set_xticks(xticks)
    ax.set_xticks(xticks_minor, minor=True)
    ax.set_xticklabels(xticks_labels)


    ####################
    ## 3. SAVE FIGURE ##
    ####################

    plt.savefig(OUTPUT+str(i)+'.png', dpi=300, bbox_inches='tight')
    print('Figure saved as '+OUTPUT+str(i)+'.png')

print('Done')
