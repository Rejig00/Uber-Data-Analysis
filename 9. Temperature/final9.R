library(dplyr)
library(tidyr)
library(ggplot2)

filename <- "uber_nyc_enriched.csv"
df <- read.csv(filename, header = TRUE)

# df$pickup_dt <- as.POSIXct(df$pickup_dt)

pivot <- df %>%
  select(temp, borough, pickups)%>%
  group_by(temp)

ggplot(pivot, aes(x=temp, y=pickups, col=borough))%>%
  +geom_jitter(alpha=0.3)%>%
  +xlab("Temperature (Fahrenheit)")%>%
  +ylab("Pickups")%>%
  +ggtitle("Pickups at New York City")%>%
  +scale_y_log10()
