ery_table = new_df.query('borough == ["Queens"]')
queens = query_table.unstack().reset_index().pickups.Queens
# plt.hist(queens, num_bins, density=False, color='blue', alpha=0.5, label='Queens', edgecolor='black', linewidth=1, stacked=True, bottom=manhattan)
plt.bar(index, queens, bar_width, alpha=opacity, yerr=None, color='purple', error_kw=error_config, label='Queens', edgecolor='black', linewidth=1, bottom=manhattan)

query_table = new_df.query('borough == ["Staten Island"]')
staten_island = query_table.unstack().reset_index().pickups["Staten Island"]
# plt.hist(staten_island, num_bins, density=False, color='blue', alpha=0.5, label='Staten Islands', edgecolor='black', linewidth=1, stacked=True, bottom=queens)
plt.bar(index,