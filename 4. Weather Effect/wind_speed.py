import pandas as pd
import math
import datetime
import matplotlib.pyplot as plt 
import numpy as np

all_date = []
#=============================================================================================================#
df = pd.read_csv("uber_nyc_enriched.csv")
for row in df.iterrows():
    row[1]["pickup_dt"] = datetime.datetime.strptime(row[1]["pickup_dt"], "%Y-%m-%d %H:%M:%S").date()
    all_date.append(row[1]["pickup_dt"])
    # print(row[1]["pickup_dt"])
df["pickup_dt"] = all_date
new_df = pd.pivot_table(df, index=["pickup_dt"], values=['sd'], aggfunc=np.mean)
# for row in new_df.iterrows():
#     row[1]['sd'] = math.sqrt(row[1]['sd'])
# print(min(new_df.dewp))

num_bins = 30
print(new_df.sd)
plt.hist(new_df.sd, num_bins, density=False, color='b', alpha=0.5, label='Average Snow Depth per day', edgecolor='black', linewidth=1)
plt.xlabel('Snow Depth (inches)')
plt.ylabel('Count')
plt.title('Snow Depth Histogram')
# plt.xticks(np.arange(6), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])
plt.legend()
plt.yscale('log')
plt.tight_layout()
plt.show()
