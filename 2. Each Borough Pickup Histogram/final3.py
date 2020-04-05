# import csv
import pandas as pd
import datetime
import matplotlib.pyplot as plt 
import numpy as np
import time

all_date = []
t1 = time.time()
# modified_date = datetime.datetime.now()
#=============================================================================================================#
df = pd.read_csv("uber_nyc_enriched.csv")

# for row in df.iterrows():

#     row[1]["pickup_dt"] = datetime.datetime.strptime(row[1]["pickup_dt"], "%Y-%m-%d %H:%M:%S").date()
#     all_date.append(row[1]["pickup_dt"])
#     # print(row[1]["pickup_dt"])
#     # print(row[1])
for i in enumerate(df["pickup_dt"]):
    modified_date = datetime.datetime.strptime(i[1], "%Y-%m-%d %H:%M:%S").date()
    all_date.append(modified_date)

# all_date = [datetime.datetime.strptime(i[1], "%Y-%m-%d %H:%M:%S").date() for i in enumerate df["pickup_dt"]]
df["pickup_dt"] = all_date
new_df = pd.pivot_table(df, index=["pickup_dt", "borough"], values=['pickups'], aggfunc=np.sum)
#================================ Plot =======================================================================#
num_bins = 30

# query_table = new_df.query('borough == ["Bronx"]')
# bronx = query_table.unstack().reset_index().pickups.Bronx
# plt.hist(bronx, num_bins, density=False, color='blue', alpha=0.5, label='Bronx', edgecolor='black', linewidth=1)

# query_table = new_df.query('borough == ["Brooklyn"]')
# brooklyn = query_table.unstack().reset_index().pickups.Brooklyn
# plt.hist(brooklyn, num_bins, density=False, color='blue', alpha=0.5, label='Brooklyn', edgecolor='black', linewidth=1)

# query_table = new_df.query('borough == ["EWR"]')
# ewr = query_table.unstack().reset_index().pickups.EWR
# plt.bar(index, ewr, bar_width, alpha=opacity, yerr=None, error_kw=error_config, label='EWR', color='green', bottom=brooklyn)# plt.hist(ewr, num_bins, density=False, color='blue', alpha=0.5, label='EWR', edgecolor='black', linewidth=1)

# query_table = new_df.query('borough == ["Manhattan"]')
# manhattan = query_table.unstack().reset_index().pickups.Manhattan# print(manhattan)
# plt.hist(manhattan, num_bins, density=False, color='blue', alpha=0.5, label='Manhattan', edgecolor='black', linewidth=1)

# query_table = new_df.query('borough == ["NA"]')
# na = query_table.unstack().reset_index().pickups.NA
# plt.hist(na, num_bins, density=False, color='blue', alpha=0.5, label='NA', edgecolor='black', linewidth=1)

# query_table = new_df.query('borough == ["Queens"]')
# queens = query_table.unstack().reset_index().pickups.Queens
# plt.hist(queens, num_bins, density=False, color='blue', alpha=0.5, label='Queens', edgecolor='black', linewidth=1)

query_table = new_df.query('borough == ["Staten Island"]')
staten_island = query_table.unstack().reset_index().pickups["Staten Island"]
plt.hist(staten_island, num_bins, density=False, color='blue', alpha=0.5, label='Staten Islands', edgecolor='black', linewidth=1)

plt.xlabel('Number of Pickups')
plt.ylabel('Count')
plt.title('Histogram of Pickups per day')
plt.legend()
plt.tight_layout()
t2 = time.time()
print(t2-t1)
plt.show()