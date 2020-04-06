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
plt.scatter(query_table["pickup_dt"], query_table["pickups"], alpha=0.1, color='b', label='Manhattan')
z = np.polyfit(query_table["pickup_dt"], query_table["pickups"], 3)
p = np.poly1d(z)
plt.plot(query_table["pickup_dt"], p(query_table["pickup_dt"]),"b") 

query_table = pd.DataFrame()
for hours in range(1, 24, 1):
     query_table = query_table.append(df.query('pickup_dt == ["' + str(hours) + '"] and borough == ["Bronx"]'))
plt.scatter(query_table["pickup_dt"], query_table["pickups"], alpha=0.1, color='r', label='Bronx')
z = np.polyfit(query_table["pickup_dt"], query_table["pickups"], 3)
p = np.poly1d(z)
plt.plot(query_table["pickup_dt"], p(query_table["pickup_dt"]),"r") 

query_table = pd.DataFrame()
for hours in range(1, 24, 1):
     query_table = query_table.append(df.query('pickup_dt == ["' + str(hours) + '"] and borough == ["Brooklyn"]'))
plt.scatter(query_table["pickup_dt"], query_table["pickups"], alpha=0.1, color='y', label='Brooklyn')
z = np.polyfit(query_table["pickup_dt"], query_table["pickups"], 3)
p = np.poly1d(z)
plt.plot(query_table["pickup_dt"], p(query_table["pickup_dt"]),"y") 

query_table = pd.DataFrame()
for hours in range(1, 24, 1):
     query_table = query_table.append(df.query('pickup_dt == ["' + str(hours) + '"] and borough == ["EWR"]'))
plt.scatter(query_table["pickup_dt"], query_table["pickups"], alpha=0.1, color='g', label='EWR')
z = np.polyfit(query_table["pickup_dt"], query_table["pickups"], 3)
p = np.poly1d(z)
plt.plot(query_table["pickup_dt"], p(query_table["pickup_dt"]),"g")

query_table = pd.DataFrame()
for hours in range(1, 24, 1):
     query_table = query_table.append(df.query('pickup_dt == ["' + str(hours) + '"] and borough == ["Queens"]'))
plt.scatter(query_table["pickup_dt"], query_table["pickups"], alpha=0.1, color='c', label='Queens')
z = np.polyfit(query_table["pickup_dt"], query_table["pickups"], 3)
p = np.poly1d(z)
plt.plot(query_table["pickup_dt"], p(query_table["pickup_dt"]),"c") 

query_table = pd.DataFrame()
for hours in range(1, 24, 1):
     query_table = query_table.append(df.query('pickup_dt == ["' + str(hours) + '"] and borough == ["Staten Island"]'))
plt.scatter(query_table["pickup_dt"], query_table["pickups"], alpha=0.1, color='m', label='Staten Island')
z = np.polyfit(query_table["pickup_dt"], query_table["pickups"], 3)
p = np.poly1d(z)
plt.plot(query_table["pickup_dt"], p(query_table["pickup_dt"]),"m") 

plt.xlabel('Hours')
plt.ylabel('Pickups')
plt.title('Hourly Pickup')
plt.legend()
plt.xticks(range(1, 24, 5), ('1 a.m.', '6 a.m.', '11 a.m.', '4 p.m.', '9 p.m.'))
plt.show()
