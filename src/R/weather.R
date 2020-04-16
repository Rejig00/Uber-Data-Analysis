library(dplyr)
library(tidyr)
library(ggplot2)

filename <- "uber_nyc_enriched.csv"
df <- read.csv(filename, header = TRUE)

df$pickup_dt <- as.POSIXct(df$pickup_dt)

pivot <- df %>%
  select(pickup_dt, spd, vsb, temp, dewp, slp, sd) %>%
  group_by(pickup_dt) %>%
  summarise(spd = mean(temp))

ggplot(pivot, aes(spd))%>%
  +geom_histogram(bins = 30, fill='palegreen4', col='black')%>%
  + xlab("Temperature (Fahrenheit)")%>%
  +ylab("Count")%>%
  +ggtitle("Average Temperature Histogram")
  # +scale_y_log10()
