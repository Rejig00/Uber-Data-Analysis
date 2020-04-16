library(dplyr)
library(tidyr)
library(ggplot2)

filename <- "uber_nyc_enriched.csv"
df <- read.csv(filename, header = TRUE)

df$pickup_dt <- format(as.POSIXlt(df$pickup_dt, format="%Y-%m-%d %H:%M:%S"), "%H")

ggplot(df, aes(x=as.numeric(pickup_dt), y=pickups, col=borough))%>%
  +geom_smooth(method = "gam", se=FALSE)%>%
  +geom_point(alpha=0.2)%>%
  +xlab("Hours")%>%
  +ylab("Pickups")%>%
  +ggtitle("Hourly Pickups at New York City")%>%
  +scale_y_log10()
