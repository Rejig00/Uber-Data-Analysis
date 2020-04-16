z = np.polyfit(tList, new_df.reset_index()["pickups"], 3)
# p = np.poly1d(z)
# plt.plot(tList, p(tList),"k") 