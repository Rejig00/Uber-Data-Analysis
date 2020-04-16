import pandas as pd
import datetime
import matplotlib.pyplot as plt 
import numpy as np

all_date = []           # Store all data from CSV

# ============================ Read CSV Data ==========================================#
df = pd.read_csv("uber_nyc_enriched.csv")
df.fillna(value="NA", inplace=True)

# ============================ Extracting only date value  ==========================================#
for i in enumerate(df["pickup_dt"]):
    all_date.append(datetime.datetime.strptime(i[1], "%Y-%m-%d %H:%M:%S").date())
df["pickup_dt"] = all_date

# ============================ Pivot Table ==========================================#
new_df = pd.pivot_table(df, index=["pickup_dt"], values=['pickups'], aggfunc=np.sum)

#================================ Plot =======================================================================#
num_bins = 50
n, bins, patches = plt.hist(new_df.reset_index()["pickups"], num_bins, density=False, color='blue', alpha=0.5, edgecolor='k')
plt.xlabel('Pickups per day')
plt.ylabel('Count')
plt.title('Histogram of Pickups')
plt.tight_layout()
plt.show()