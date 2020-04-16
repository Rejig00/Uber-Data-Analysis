library(dplyr)
library(tidyr)
library(ggplot2)

filename <- "uber_nyc_enriched.csv"
df <- read.csv(filename, header = TRUE)

df$pickup_dt <- format(as.POSIXlt(df$pickup_dt), "%m")

pivot <- df %>%
  select(pickup_dt, borough, pickups) %>%
  group_by(pickup_dt, borough) %>%
  summarise(total_pickups = sum(pickups))
# print(pivot)

ggplot(pivot, aes(x=pickup_dt, y=total_pickups, fill=borough))+geom_bar(stat = "identity")+xlab("Months")+ylab("Pickups")+ggtitle("Pickups per month")
