
import geopandas as gpd
from matplotlib import pyplot as plt




df = gpd.read_file('readable_k.json')
# df.plot()
# df.plot(figsize=(10,10), edgecolor='purple', facecolor='green')
# df.boundary.plot(figsize=(10,10))
# df.shape
# print(df.head())
df_23 = df.loc[df['WARD'] == '23']
df_23.boundary.plot(figsize=(10,10))

plt.show()