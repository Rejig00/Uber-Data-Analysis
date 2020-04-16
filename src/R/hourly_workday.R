library(dplyr)
library(tidyr)
library(ggplot2)

filename <- "uber_nyc_enriched.csv"
df <- read.csv(filename, header = TRUE)

df$day <- weekdays(as.POSIXct(df$pickup_dt), abbreviate = FALSE)
df$hour <- format(as.POSIXlt(df$pickup_dt, format="%Y-%m-%d %H:%M:%S"), "%H")
df <- df%>%
  mutate(weekday=ifelse(day=="Saturday" | day=="Sunday", 'Weekend', 'Weekday'))
df$day <- factor(df$weekday, c("Weekday", "Weekend"))

query_table <- subset(df, borough=='Brooklyn')

ggplot(query_table, aes(hour, pickups))%>%
  +geom_jitter(alpha = 0.3, aes(colour = weekday))%>%
  +xlab("Hours")%>%
  +ylab("Pickups")%>%
  +ggtitle("Pickups at Brooklyn")
