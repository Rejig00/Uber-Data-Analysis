import pandas as pd
import datetime
import matplotlib.pyplot as plt 
import numpy as np
import time

all_date = []

df = pd.read_csv("uber_nyc_enriched.csv")
df.fillna(value="NA", inplace=True)

for i in enumerate(df["pickup_dt"]):
    all_date.append(datetime.datetime.strptime(i[1], "%Y-%m-%d %H:%M:%S").date())
df["pickup_dt"] = all_date
new_df = pd.pivot_table(df, index=["pickup_dt"], values=['pickups'], aggfunc=np.sum)

tList = []
t = 0
while t < len(new_df.reset_index().pickup_dt):
    ti = int(time.mktime(new_df.reset_index().pickup_dt[t].timetuple()))
    tList.append(ti)
    t = t + 1

plt.scatter(tList, new_df.reset_index().pickups, alpha=0.4, color='grey', label='Pickups')
z = np.polyfit(tList, new_df.reset_index().pickups, 3)
p = np.poly1d(z)
plt.plot(tList,p(tList),"b--", label='Best fit line')
plt.xticks(np.linspace(1.420e9, 1.436e9, num=6), ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'))
plt.xlabel('Months')
plt.ylabel('Pickups')
plt.title('Scatter Plot of Pickups')
plt.legend()
plt.show()