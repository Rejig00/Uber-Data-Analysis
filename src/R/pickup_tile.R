library(dplyr)
library(tidyr)
library(ggplot2)

filename <- "uber_nyc_enriched.csv"
df <- read.csv(filename, header = TRUE)

df$day <- weekdays(as.POSIXct(df$pickup_dt), abbreviate = FALSE)
df$hour <- df$pickup_dt <- format(as.POSIXlt(df$pickup_dt, format="%Y-%m-%d %H:%M:%S"), "%H")

query_table = subset(df, df$borough=='Manhattan')
query_table$day <- factor(query_table$day, c("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"))

ggplot(query_table, aes(x=day, y=hour, fill=pickups))%>%
  +geom_tile()%>%
  +xlab("Days")%>%
  +ylab("Time of the day")%>%
  +scale_fill_distiller(palette = 'Spectral')%>%
  +ggtitle("Pickups at Manhattan")
