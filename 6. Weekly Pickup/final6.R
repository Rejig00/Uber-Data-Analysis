library(dplyr)
library(tidyr)
library(ggplot2)

filename <- "uber_nyc_enriched.csv"
df <- read.csv(filename, header = TRUE)

df$pickup_dt <- weekdays(as.POSIXct(df$pickup_dt), abbreviate = FALSE)

query_table = subset(df, df$borough=='Manhattan')
query_table$pickup_dt <- factor(query_table$pickup_dt, c("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"))
# query_table[order(query_table$pickup_dt)]

# pivot <- df %>%
#   select(pickup_dt, pickups) %>%
#   group_by(pickup_dt) %>%
#   summarise(total_pickups = sum(pickups))

ggplot(query_table, aes(x=pickup_dt, y=pickups))+geom_boxplot()
