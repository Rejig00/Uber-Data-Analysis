import pandas as pd 
import datetime 
import matplotlib.pyplot as plt 
import numpy as np

all_date = []
#=============================================================================================================#
df = pd.read_csv("uber_nyc_enriched.csv")
for row in df.iterrows():
    row[1]["pickup_dt"] = datetime.datetime.strptime(row[1]["pickup_dt"], "%Y-%m-%d %H:%M:%S")
    all_date.append(row[1]["pickup_dt"].strftime('%A'))

df["pickup_dt"] = all_date
# new_df = pd.pivot_table(df, index=["pickup_dt"], values=['pickups'], aggfunc=np.mean)
# df.plot.box()
# print(new_df)

query_table = df.query('pickup_dt == ["Sunday"] and borough == ["Manhattan"]')
sunday = query_table.pickups

query_table = df.query('pickup_dt == ["Monday"] and borough == ["Manhattan"]')
monday = query_table.pickups

query_table = df.query('pickup_dt == ["Tuesday"] and borough == ["Manhattan"]')
tuesday = query_table.pickups

query_table = df.query('pickup_dt == ["Wednesday"] and borough == ["Manhattan"]')
wednesday = query_table.pickups

query_table = df.query('pickup_dt == ["Thursday"] and borough == ["Manhattan"]')
thursday = query_table.pickups

query_table = df.query('pickup_dt == ["Friday"] and borough == ["Manhattan"]')
friday = query_table.pickups

query_table = df.query('pickup_dt == ["Saturday"] and borough == ["Manhattan"]')
saturday = query_table.pickups

data_to_plot = np.array([sunday, monday, tuesday, wednesday, thursday, friday, saturday])

plt.boxplot(data_to_plot)
plt.xlabel('Days')
plt.ylabel('Pickups')
plt.title('Box Plot of Pickups in Manhattan')
plt.xticks(range(1, 8, 1), ('Sun', 'Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat'))
plt.show()
