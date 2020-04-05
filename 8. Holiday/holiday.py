import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv("uber_nyc_enriched.csv")
new_df = pd.pivot_table(df, index=["hday"], values=['pickups'], aggfunc=np.sum)

index = np.arange(2)
bar_width = 0.35
opacity = 0.4
error_config = {
    'ecolor': '0.3'
}

plt.bar(index, new_df.pickups, bar_width, alpha=opacity, yerr=None, color='b')
plt.xlabel('Holidays')
plt.ylabel('Pickups')
plt.title('Holiday Pickups')
plt.xticks(index, ['No', 'Yes'])
plt.legend()
plt.tight_layout()
plt.show()