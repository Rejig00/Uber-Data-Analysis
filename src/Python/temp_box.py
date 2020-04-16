import pandas as pd 
import datetime 
import matplotlib.pyplot as plt 
import numpy as np

df = pd.read_csv("uber_nyc_enriched.csv")

data_to_plot = np.array([df.query('temp >= 75 and borough == ["Manhattan"]').pickups.values, df.query('temp < 75 and borough == ["Manhattan"]').pickups.values])

plt.boxplot(data_to_plot)
plt.xlabel('Temperature (Fahrenheit)')
plt.ylabel('Pickups')
plt.title('Temperature Vs Pickups in Manhattan')
plt.xticks(range(1, 3, 1), (">=75", "<75"))
plt.legend()
plt.tight_layout()
plt.show()