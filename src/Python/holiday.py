import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv("uber_nyc_enriched.csv")

data_to_plot = np.array([df.query('hday == ["Y"] and borough == ["Manhattan"]').pickups.values, df.query('hday == ["N"] and borough == ["Manhattan"]').pickups.values])

plt.boxplot(data_to_plot)
plt.xlabel('Holidays')
plt.ylabel('Pickups')
plt.title('Holiday Pickups in Manhattan')
plt.xticks(range(1, 3, 1), ('Yes', 'No'))
plt.legend()
plt.tight_layout()
plt.show()