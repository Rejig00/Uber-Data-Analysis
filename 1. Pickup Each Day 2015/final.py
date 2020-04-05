import csv
import datetime
import matplotlib.pyplot as plt 
import numpy as np

all_date = []           # Store all datea from CSV
all_pickup = []         # Store all pickups from CSV
pickup = []             # Pickup Count each day
sum_of_pickup = 0

# =======================Open file and create necessary lists ==========================================#
with open("uber_nyc_enriched.csv", "r") as datafile:
    csvfile = csv.reader(datafile)
    for row in csvfile:
        if row[0] != "pickup_dt":       # ignoring the header row
            all_date.append(datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S").date())      # Create a list of only dates
            all_pickup.append(int(row[2]))
    date_object = list(dict.fromkeys(all_date))      # Get unique date values
    date_object.sort()
    for i in range(len(date_object)):
        for j in range(len(all_date)):
            if(all_date[j] == date_object[i]):
                sum_of_pickup += all_pickup[j]
        pickup.append(sum_of_pickup)
        sum_of_pickup = 0
#=============================================================================================================#
#================================ Plot =======================================================================#
index = np.arange(len(date_object))
bar_width = 0.35
opacity = 0.4
error_config = {
    'ecolor': '0.3'
}
rects = plt.bar(index, pickup, bar_width, alpha=opacity, yerr=None, error_kw=error_config, label='Pickup count in each day of 2015')
plt.xlabel('Date')
plt.ylabel('Pickup')
plt.title('Datewise Pickup Analysis')
plt.legend()
plt.xticks([],[])
plt.tight_layout()
plt.show()