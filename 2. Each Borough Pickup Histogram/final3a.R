library(dplyr)
library(tidyr)
library(ggplot2)

filename <- "uber_nyc_enriched.csv"
df <- read.csv(filename, header = TRUE)

df$pickup_dt <- as.POSIXct(df$pickup_dt)

pivot <- df %>%
  select(pickup_dt, borough, pickups) %>%
  group_by(pickup_dt, borough)%>%
  summarise(total_pickups = sum(pickups))

query_table <- subset(pivot, pivot$borough == 'Staten Island')
# print(query_table)

ggplot(query_table, aes(x=total_pickups)) + geom_histogram(bins = 30, fill='palegreen4', col='black') + xlab("Total Pickups") + ylab("Count") + ggtitle("Histogram of Pickups per day at Staten Island") 
