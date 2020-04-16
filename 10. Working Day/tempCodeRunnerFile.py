query_table = df.query('pickup_dt == ["Weekday"] and borough == ["NA"]')
# weekday = query_table.pickups
# query_table = df.query('pickup_dt == ["Weekend"] and borough == ["NA"]')
# weekend = query_table.pickups
# data_to_plot = np.array([weekday, weekend])
# axs[3, 0].boxplot(data_to_plot)
# axs[3, 0].set_title('NA')