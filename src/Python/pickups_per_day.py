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
index = np.arange(len(new_df.reset_index()["pickup_dt"]))
bar_width = 0.35
opacity = 0.4
error_config = {
    'ecolor': '0.3'
}
plt.bar(index, new_df["pickups"], bar_width, alpha=opacity, yerr=None, error_kw=error_config, label='Pickup count per day')
plt.xlabel('Date')
plt.ylabel('Pickup')
plt.title('Datewise Pickup Analysis')
plt.legend()
plt.xticks(np.linspace(0, 180, num=7), ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'))
plt.tight_layout()
plt.show()