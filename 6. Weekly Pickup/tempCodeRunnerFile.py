plt.boxplot(data_to_plot)
plt.xlabel('Days')
plt.ylabel('Pickups')
plt.title('Box Plot of Pickups in Manhattan')
plt.xticks(range(1, 8, 1), ('Sun', 'Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat'))
plt.show()