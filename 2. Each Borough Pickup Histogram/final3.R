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
# head(pivot)

ggplot(pivot, aes(x = total_pickups, fill=borough)) + geom_histogram(bins = 30) + xlab("Total Pickups") + ylab("Count") + ggtitle("Histogram of Pickups per day in all boroughs")
