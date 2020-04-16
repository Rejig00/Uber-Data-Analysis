library(dplyr)
library(tidyr)
library(ggplot2)
library(viridis)

filename <- "uber_nyc_enriched.csv"
df <- read.csv(filename, header = TRUE)

query_table = subset(df, df$borough=='Manhattan')

ggplot(query_table, aes(x=temp, y=pickups, col=temp))%>%
  +geom_point(alpha=0.4)%>%
  +geom_smooth(col='black', se=F)%>%
  +scale_color_gradient(low = "blue", high = "red")%>%
  +xlab("Temperature (Fahrenheit)")%>%
  +ylab("Pickups")%>%
  +ggtitle("Pickups at Manhattan")
