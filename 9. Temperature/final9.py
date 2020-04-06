import pandas as pd 
import datetime 
import matplotlib.pyplot as plt 
import numpy as np

# query_table = pd.DataFrame()
opacity = 0.3
opacity2 = 0.1
#=============================================================================================================#
df = pd.read_csv("uber_nyc_enriched.csv")

query_table = df.query('borough == ["Manhattan"]')
plt.scatter(query_table.temp.values, query_table.pickups.values, alpha=opacity, color="b", label='Manhattan')
# z = np.polyfit(query_table.temp, query_table.pickups, 1)
# p = np.poly1d(z)
# plt.plot(query_table.temp.values, p(query_table.temp.values),"b-", label="Manhattan") 

# query_table = pd.DataFrame()
query_table = df.query('borough == ["Bronx"]')
plt.scatter(query_table.temp.values, query_table.pickups.values, alpha=opacity, color='r', label='Bronx')
# z = np.polyfit(query_table.temp.values, query_table.pickups.values, 1)
# p = np.poly1d(z)
# plt.plot(query_table.temp.values, p(query_table.temp.values),"r-", label='Bronx')

# query_table = pd.DataFrame()
query_table = df.query('borough == ["Brooklyn"]')
plt.scatter(query_table.temp.values, query_table.pickups.values, alpha=opacity, color='y', label='Brooklyn')
# z = np.polyfit(query_table.temp.values, query_table.pickups.values, 1)
# p = np.poly1d(z)
# plt.plot(query_table.temp.values, p(query_table.temp.values),"y-", label='Brooklyn')

# query_table = pd.DataFrame()
query_table = df.query('borough == ["EWR"]')
plt.scatter(query_table.temp.values, query_table.pickups.values, alpha=opacity2, color='g', label='EWR')
# z = np.polyfit(query_table.temp.values, query_table.pickups.values, 1)
# p = np.poly1d(z)
# plt.plot(query_table.temp.values, p(query_table.temp.values),"g-", label='EWR')

# query_table = pd.DataFrame()
query_table = df.query('borough == ["Queens"]')
plt.scatter(query_table.temp.values, query_table.pickups.values, alpha=opacity2, color='c', label='Queens')
# z = np.polyfit(query_table.temp.values, query_table.pickups.values, 1)
# p = np.poly1d(z)
# plt.plot(query_table.temp.values, p(query_table.temp.values),"c-", label='Queens')

# query_table = pd.DataFrame()
query_table = df.query('borough == ["Staten Island"]')
plt.scatter(query_table.temp.values, query_table.pickups.values, alpha=opacity2, color='m', label='Staten Island')
# z = np.polyfit(query_table.temp.values, query_table.pickups.values, 1)
# p = np.poly1d(z)
# plt.plot(query_table.temp.values, p(query_table.temp.values),"m-", label='Staten Island')

plt.xlabel('Temperature (Fahrenheit)')
plt.ylabel('Pickups')
plt.title('Temp Vs Pickups')
plt.legend()
# plt.colorbar(orientation='horizontal')
# plt.xticks(range(1, 24, 5), ('1 a.m.', '6 a.m.', '11 a.m.', '4 p.m.', '9 p.m.'))
plt.show()
