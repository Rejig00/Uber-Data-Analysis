library(dplyr)
library(tidyr)
library(ggplot2)

filename <- "uber_nyc_enriched.csv"
df <- read.csv(filename, header = TRUE)

df$pickup_dt <- as.POSIXct(df$pickup_dt)

pivot <- df %>%
  select(pickup_dt, pickups) %>%
  group_by(pickup_dt)%>%
  summarise(total_pickups = sum(pickups))

ggplot(pivot, aes(x=pickup_dt, y=total_pickups))+geom_bar(stat = "identity", fill = "steelblue", col="black") + xlab("Date") + ylab("Number of Pickups") + ggtitle("Pickups per day in New York City")
