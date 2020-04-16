import pandas as pd
import datetime
import matplotlib.pyplot as plt 
import numpy as np

all_month = []

df = pd.read_csv("uber_nyc_enriched.csv")
df.fillna(value="NA", inplace=True)
for i in enumerate(df["pickup_dt"]):
    all_month.append(datetime.datetime.strptime(i[1], "%Y-%m-%d %H:%M:%S").date().month)
df["pickup_dt"] = all_month
new_df = pd.pivot_table(df, index=["pickup_dt", "borough"], values=['pickups'], aggfunc=np.sum)

#================================ Plot =======================================================================#
index = np.arange(6)
bar_width = 0.35
opacity = 0.4
error_config = {
    'ecolor': '0.3'
}

query_table = new_df.query('borough == ["Bronx"]')
bronx = query_table.unstack().reset_index().pickups.Bronx
plt.bar(index, bronx, bar_width, alpha=opacity, yerr=None, color='red', error_kw=error_config, label='Bronx', edgecolor='black', linewidth=1)

query_table = new_df.query('borough == ["EWR"]')
ewr = query_table.unstack().reset_index().pickups.EWR
plt.bar(index, ewr, bar_width, alpha=opacity, yerr=None, color='green', error_kw=error_config, label='EWR', edgecolor='black', linewidth=1, bottom=bronx)

query_table = new_df.query('borough == ["Brooklyn"]')
brooklyn = query_table.unstack().reset_index().pickups.Brooklyn
plt.bar(index, brooklyn, bar_width, alpha=opacity, yerr=None, color='yellow', error_kw=error_config, label='Brooklyn', edgecolor='black', linewidth=1, bottom=ewr+bronx)

query_table = new_df.query('borough == ["Manhattan"]')
manhattan = query_table.unstack().reset_index().pickups.Manhattan
plt.bar(index, manhattan, bar_width, alpha=opacity, yerr=None, color='blue', error_kw=error_config, label='Manhattan', edgecolor='black', linewidth=1, bottom=brooklyn+ewr+bronx)

query_table = new_df.query('borough == ["Queens"]')
queens = query_table.unstack().reset_index().pickups.Queens
plt.bar(index, queens, bar_width, alpha=opacity, yerr=None, color='purple', error_kw=error_config, label='Queens', edgecolor='black', linewidth=1, bottom=manhattan+brooklyn+ewr+bronx)

query_table = new_df.query('borough == ["Staten Island"]')
staten_island = query_table.unstack().reset_index().pickups["Staten Island"]
plt.bar(index, staten_island, bar_width, alpha=opacity, yerr=None, color='grey', error_kw=error_config, label='Staten Island', edgecolor='black', linewidth=1, bottom=queens+manhattan+brooklyn+ewr+bronx)

plt.xlabel('Months')
plt.ylabel('Pickups')
plt.title('Monthly Pickup')
plt.xticks(index, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])
plt.legend()
plt.tight_layout()
plt.show()