library(dplyr)
library(tidyr)
library(ggplot2)

filename <- "uber_nyc_enriched.csv"
df <- read.csv(filename, header = TRUE)

df$pickup_dt <- as.POSIXct(df$pickup_dt)
# head(df)

pivot <- df %>%
  select(pickup_dt, pickups) %>%
  group_by(pickup_dt)%>%
  summarise(total_pickups = sum(pickups))
# head(pivot)

ggplot(pivot, aes(x = total_pickups))+geom_histogram(bins=49) + xlab("Pickups") + ylab("Count") + ggtitle("Pickup Histogram of New York City")
