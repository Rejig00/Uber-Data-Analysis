import pandas as pd 
import datetime 
import matplotlib.pyplot as plt 
import numpy as np

all_date = []
#=============================================================================================================#
df = pd.read_csv("uber_nyc_enriched.csv")
df.fillna(value="NA", inplace=True)

for i in enumerate(df["pickup_dt"]):
    if(datetime.datetime.strptime(i[1], "%Y-%m-%d %H:%M:%S").date().strftime('%A')==("Saturday" or "Sunday")):
        all_date.append("Weekend")
    else:
        all_date.append("Weekday")
    # all_date.append(datetime.datetime.strptime(i[1], "%Y-%m-%d %H:%M:%S").date().strftime('%A'))

df["pickup_dt"] = all_date
# print(df)

query_table = df.query('pickup_dt == ["Weekday"] and borough == ["Bronx"]')
weekday = query_table.pickups
query_table = df.query('pickup_dt == ["Weekend"] and borough == ["Bronx"]')
weekend = query_table.pickups
data_to_plot = np.array([weekday, weekend])
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.boxplot(data_to_plot)
ax1.set_title('Bronx')
ax1.set_ylabel('Pickups')

query_table = df.query('pickup_dt == ["Weekday"] and borough == ["Brooklyn"]')
weekday = query_table.pickups
query_table = df.query('pickup_dt == ["Weekend"] and borough == ["Brooklyn"]')
weekend = query_table.pickups
data_to_plot = np.array([weekday, weekend])
ax2.boxplot(data_to_plot)
ax2.set_title('Brooklyn')
ax2.set_ylabel('Pickups')

plt.sca(ax1)
plt.xticks(range(1, 3, 1), ('Weekday', 'Weekend'))
plt.sca(ax2)
plt.xticks(range(1, 3, 1), ('Weekday', 'Weekend'))
plt.show()
fig, (ax1, ax2) = plt.subplots(1, 2)

query_table = df.query('pickup_dt == ["Weekday"] and borough == ["EWR"]')
weekday = query_table.pickups
query_table = df.query('pickup_dt == ["Weekend"] and borough == ["EWR"]')
weekend = query_table.pickups
data_to_plot = np.array([weekday, weekend])
ax1.boxplot(data_to_plot)
ax1.set_title('EWR')
ax1.set_ylabel('Pickups')

query_table = df.query('pickup_dt == ["Weekday"] and borough == ["Manhattan"]')
weekday = query_table.pickups
query_table = df.query('pickup_dt == ["Weekend"] and borough == ["Manhattan"]')
weekend = query_table.pickups
data_to_plot = np.array([weekday, weekend])
ax2.boxplot(data_to_plot)
ax2.set_title('Manhattan')
ax2.set_ylabel('Pickups')

plt.sca(ax1)
plt.xticks(range(1, 3, 1), ('Weekday', 'Weekend'))
plt.sca(ax2)
plt.xticks(range(1, 3, 1), ('Weekday', 'Weekend'))
plt.show()
fig, (ax1, ax2) = plt.subplots(1, 2)

query_table = df.query('pickup_dt == ["Weekday"] and borough == ["Queens"]')
weekday = query_table.pickups
query_table = df.query('pickup_dt == ["Weekend"] and borough == ["Queens"]')
weekend = query_table.pickups
data_to_plot = np.array([weekday, weekend])
ax1.boxplot(data_to_plot)
ax1.set_title('Queens')
ax1.set_ylabel('Pickups')

query_table = df.query('pickup_dt == ["Weekday"] and borough == ["Staten Island"]')
weekday = query_table.pickups
query_table = df.query('pickup_dt == ["Weekend"] and borough == ["Staten Island"]')
weekend = query_table.pickups
data_to_plot = np.array([weekday, weekend])
ax2.boxplot(data_to_plot)
ax2.set_title('Staten Island')
ax2.set_ylabel('Pickups')

plt.sca(ax1)
plt.xticks(range(1, 3, 1), ('Weekday', 'Weekend'))
plt.sca(ax2)
plt.xticks(range(1, 3, 1), ('Weekday', 'Weekend'))
plt.show()
