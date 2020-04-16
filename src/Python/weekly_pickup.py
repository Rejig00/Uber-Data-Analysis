import pandas as pd 
import datetime 
import matplotlib.pyplot as plt 
import numpy as np

all_date = []
#=============================================================================================================#
df = pd.read_csv("uber_nyc_enriched.csv")
df.fillna(value="NA", inplace=True)

for i in enumerate(df["pickup_dt"]):
    all_date.append(datetime.datetime.strptime(i[1], "%Y-%m-%d %H:%M:%S").date().strftime('%A'))

df["pickup_dt"] = all_date

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
