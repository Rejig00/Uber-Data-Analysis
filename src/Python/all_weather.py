import pandas as pd
import math
import datetime
import matplotlib.pyplot as plt 
import numpy as np

all_date = []
#=============================================================================================================#
df = pd.read_csv("uber_nyc_enriched.csv")
df.fillna(value="NA", inplace=True)
for i in enumerate(df["pickup_dt"]):
    all_date.append(datetime.datetime.strptime(i[1], "%Y-%m-%d %H:%M:%S").date())
df["pickup_dt"] = all_date
new_df = pd.pivot_table(df, index=["pickup_dt"], values=['temp'], aggfunc=np.mean)

num_bins = 30
plt.hist(new_df.temp, num_bins, density=False, color='b', alpha=0.5, edgecolor='black', linewidth=1)
plt.xlabel('Temperature (Fahrenheit)')
plt.ylabel('Count')
plt.title('Average Temperature Histogram')
plt.legend()
plt.tight_layout()
# plt.yscale('log')
plt.show()
