import pandas as pd 
import datetime 
import matplotlib.pyplot as plt 
import numpy as np

query_table = pd.DataFrame()
#=============================================================================================================#
df = pd.read_csv("uber_nyc_enriched.csv")

query_table = query_table.append(df.query('borough == ["Manhattan"]'))
print(query_table)

plt.scatter(query_table.temp.values, query_table.pickups.values, alpha=0.7, c=query_table.temp, label='Pickups', cmap='hot_r', edgecolors='grey')
z = np.polyfit(query_table.temp.values, query_table.pickups.values, 1)
p = np.poly1d(z)
plt.plot(query_table.temp.values, p(query_table.temp.values),"b--", label='Best fit line') 
plt.xlabel('Temperature (Fahrenheit)')
plt.ylabel('Pickups')
plt.title('Temp Vs Pickups in Manhattan')
plt.legend()
plt.colorbar(orientation='horizontal')
plt.show()
