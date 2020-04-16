library(dplyr)
library(tidyr)
library(ggplot2)

filename <- "uber_nyc_enriched.csv"
df <- read.csv(filename, header = TRUE)

df$pickup_dt <- as.POSIXct(df$pickup_dt)
# head(df)

pivot <- df %>%
  select(pickup_dt, pickups, borough) %>%
  group_by(pickup_dt, borough)%>%
  summarise(total_pickups = sum(pickups))
head(pivot,20)

ggplot(pivot, aes(x = total_pickups, fill=borough))%>%
  +geom_histogram(bins=50)%>%
  +xlab("Pickups")%>%
  +ylab("Count")%>%
  +ggtitle("Pickup Histogram of New York City")
  