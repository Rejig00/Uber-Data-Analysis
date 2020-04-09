library(dplyr)
library(tidyr)
library(ggplot2)

filename <- "uber_nyc_enriched.csv"
df <- read.csv(filename, header = TRUE)

df$pickup_dt <- as.POSIXct(df$pickup_dt)

pivot <- df %>%
  select(pickup_dt, spd, vsb, temp, dewp, slp) %>%
  group_by(pickup_dt) %>%
  summarise(spd = mean(slp))

# ggplot(pivot, aes(x=spd))+geom_histogram(bins = 30, fill='palegreen4', col='black')+ xlab("Wind Speed (miles/hr)")+ylab("Count")+ggtitle("Average Wind Speed Histogram")
ggplot(pivot, aes(spd))+geom_histogram(bins = 30, fill='palegreen4', col='black')+ xlab("Sea Level Pressure")+ylab("Count")+ggtitle("Average SLP Histogram")
