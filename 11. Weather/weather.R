library(dplyr)
library(tidyr)
library(ggplot2)

filename <- "uber_nyc_enriched.csv"
df <- read.csv(filename, header = TRUE)

query_table <- subset(df, df$borough=='Manhattan')

ggplot(query_table, aes(x=slp, y=pickups))%>%
  +geom_point(alpha=0.2)%>%
  +geom_smooth()%>%
  +xlab("Sea Level Pressure")%>%
  +ylab("Pickups")
