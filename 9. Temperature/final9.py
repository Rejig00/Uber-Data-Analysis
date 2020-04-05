import pandas as pd 
import datetime 
import matplotlib.pyplot as plt 
import numpy as np

query_table = pd.DataFrame()
#=============================================================================================================#
df = pd.read_csv("uber_nyc_enriched.csv")

query_table = query_table.append(df.query('borough == ["Manhattan"]'))
plt.scatter(query_table.temp.values, query_table.pickups.values, alpha=0.1, color="blue", label='Manhattan')
z = np.polyfit(query_table.temp.values, query_table.pickups.values, 1)
p = np.poly1d(z)
plt.plot(query_table.temp.values, p(query_table.temp.values),"k--") 

query_table = query_table.append(df.query('borough == ["Bronx"]'))
plt.scatter(query_table.temp.values, query_table.pickups.values, alpha=1, color='red', label='Bronx')
z = np.polyfit(query_table.temp.values, query_table.pickups.values, 1)
p = np.poly1d(z)
plt.plot(query_table.temp.values, p(query_table.temp.values),"k--")

query_table = query_table.append(df.query('borough == ["Brooklyn"]'))
plt.scatter(query_table.temp.values, query_table.pickups.values, alpha=1, color='yellow', label='Brooklyn')
z = np.polyfit(query_table.temp.values, query_table.pickups.values, 1)
p = np.poly1d(z)
plt.plot(query_table.temp.values, p(query_table.temp.values),"k--")

query_table = query_table.append(df.query('borough == ["EWR"]'))
plt.scatter(query_table.temp.values, query_table.pickups.values, alpha=1, color='green', label='EWR')
z = np.polyfit(query_table.temp.values, query_table.pickups.values, 1)
p = np.poly1d(z)
plt.plot(query_table.temp.values, p(query_table.temp.values),"k--")

query_table = query_table.append(df.query('borough == ["Queens"]'))
plt.scatter(query_table.temp.values, query_table.pickups.values, alpha=1, color='purple', label='Queens')
z = np.polyfit(query_table.temp.values, query_table.pickups.values, 1)
p = np.poly1d(z)
plt.plot(query_table.temp.values, p(query_table.temp.values),"k--")

query_table = query_table.append(df.query('borough == ["Staten Island"]'))
plt.scatter(query_table.temp.values, query_table.pickups.values, alpha=1, color='pink', label='Staten Island')
z = np.polyfit(query_table.temp.values, query_table.pickups.values, 1)
p = np.poly1d(z)
plt.plot(query_table.temp.values, p(query_table.temp.values),"k--")

plt.xlabel('Temperature (Fahrenheit)')
plt.ylabel('Pickups')
plt.title('Temp Vs Pickups')
plt.legend()
# plt.colorbar(orientation='horizontal')
# plt.xticks(range(1, 24, 5), ('1 a.m.', '6 a.m.', '11 a.m.', '4 p.m.', '9 p.m.'))
plt.show()
