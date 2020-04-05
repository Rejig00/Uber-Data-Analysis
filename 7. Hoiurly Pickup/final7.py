import pandas as pd 
import datetime 
import matplotlib.pyplot as plt 
import numpy as np

all_date = []
query_table = pd.DataFrame()
#=============================================================================================================#
df = pd.read_csv("uber_nyc_enriched.csv")

for i in enumerate(df["pickup_dt"]):
    modified_date = datetime.datetime.strptime(i[1], "%Y-%m-%d %H:%M:%S").time()
    all_date.append(int(modified_date.strftime('%H')))

df["pickup_dt"] = all_date

for hours in range(1, 24, 1):
     query_table = query_table.append(df.query('pickup_dt == ["' + str(hours) + '"] and borough == ["Manhattan"]'))
# print(query_table)



plt.scatter(query_table["pickup_dt"], query_table["pickups"], alpha=0.2, color='grey', label='Pickups')
z = np.polyfit(query_table["pickup_dt"], query_table["pickups"], 3)
p = np.poly1d(z)
plt.plot(query_table["pickup_dt"], p(query_table["pickup_dt"]),"b--", label='Best fit line') 
plt.xlabel('Hours')
plt.ylabel('Pickups')
plt.title('Hourly Pickup in Manhattan')
plt.legend()
plt.xticks(range(1, 24, 5), ('1 a.m.', '6 a.m.', '11 a.m.', '4 p.m.', '9 p.m.'))
plt.show()
