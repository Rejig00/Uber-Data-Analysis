import pandas as pd
import datetime
import matplotlib.pyplot as plt 
import numpy as np

all_month = []

df = pd.read_csv("uber_nyc_enriched.csv")
for row in df.iterrows():
    row[1]["pickup_dt"] = datetime.datetime.strptime(row[1]["pickup_dt"], "%Y-%m-%d %H:%M:%S").date().month
    all_month.append(row[1]["pickup_dt"])
df["pickup_dt"] = all_month
new_df = pd.pivot_table(df, index=["pickup_dt", "borough"], values=['pickups'], aggfunc=np.sum)

#================================ Plot =======================================================================#
# num_bins = 3
index = np.arange(6)
bar_width = 0.35
opacity = 0.4
error_config = {
    'ecolor': '0.3'
}

query_table = new_df.query('borough == ["Bronx"]')
bronx = query_table.unstack().reset_index().pickups.Bronx
# bronx_hist = plt.hist(bronx, num_bins, density=False, color='red', alpha=0.5, label='Bronx', edgecolor='black', linewidth=1, stacked=True)
plt.bar(index, bronx, bar_width, alpha=opacity, yerr=None, color='red', error_kw=error_config, label='Bronx', edgecolor='black', linewidth=1)

query_table = new_df.query('borough == ["EWR"]')
ewr = query_table.unstack().reset_index().pickups.EWR
# plt.hist(ewr, num_bins, density=False, color='green', alpha=0.5, label='EWR', edgecolor='black', linewidth=1, stacked=True, bottom=brooklyn)
plt.bar(index, ewr, bar_width, alpha=opacity, yerr=None, color='green', error_kw=error_config, label='EWR', edgecolor='black', linewidth=1, bottom=bronx)

query_table = new_df.query('borough == ["Brooklyn"]')
brooklyn = query_table.unstack().reset_index().pickups.Brooklyn
# plt.hist(brooklyn, num_bins, density=False, color='yellow', alpha=0.5, label='Brooklyn', edgecolor='black', linewidth=1, stacked=True, bottom=bronx_hist)
plt.bar(index, brooklyn, bar_width, alpha=opacity, yerr=None, color='yellow', error_kw=error_config, label='Brooklyn', edgecolor='black', linewidth=1, bottom=ewr+bronx)

query_table = new_df.query('borough == ["Manhattan"]')
manhattan = query_table.unstack().reset_index().pickups.Manhattan
# # plt.hist(manhattan, num_bins, density=False, color='blue', alpha=0.5, label='Manhattan', edgecolor='black', linewidth=1, stacked=True, bottom=ewr)
plt.bar(index, manhattan, bar_width, alpha=opacity, yerr=None, color='blue', error_kw=error_config, label='Manhattan', edgecolor='black', linewidth=1, bottom=brooklyn+ewr+bronx)

query_table = new_df.query('borough == ["Queens"]')
queens = query_table.unstack().reset_index().pickups.Queens
# plt.hist(queens, num_bins, density=False, color='blue', alpha=0.5, label='Queens', edgecolor='black', linewidth=1, stacked=True, bottom=manhattan)
plt.bar(index, queens, bar_width, alpha=opacity, yerr=None, color='purple', error_kw=error_config, label='Queens', edgecolor='black', linewidth=1, bottom=manhattan+brooklyn+ewr+bronx)

query_table = new_df.query('borough == ["Staten Island"]')
staten_island = query_table.unstack().reset_index().pickups["Staten Island"]
# plt.hist(staten_island, num_bins, density=False, color='blue', alpha=0.5, label='Staten Islands', edgecolor='black', linewidth=1, stacked=True, bottom=queens)
plt.bar(index, staten_island, bar_width, alpha=opacity, yerr=None, color='grey', error_kw=error_config, label='Staten Island', edgecolor='black', linewidth=1, bottom=queens+manhattan+brooklyn+ewr+bronx)

plt.xlabel('Months')
plt.ylabel('Pickups')
plt.title('Monthly Pickup')
plt.xticks(index, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])
plt.legend()
plt.tight_layout()
plt.show()