import pandas as pd
import numpy as np

df = pd.read_csv("uber_nyc_enriched.csv")

df.fillna(value="NA", inplace=True)

# print(df)