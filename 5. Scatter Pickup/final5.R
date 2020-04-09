library(dplyr)
library(tidyr)
library(ggplot2)

filename <- "uber_nyc_enriched.csv"
df <- read.csv(filename, header = TRUE)

df$pickup_dt <- as.POSIXct(df$pickup_dt)

query_table = subset(df, df$borough=='Manhattan')

pivot <- df %>%
  select(pickup_dt, pickups) %>%
  group_by(pickup_dt) %>%
  summarise(total_pickups = sum(pickups))

ggplot(df, aes(x=pickup_dt, y=pickups, col=borough))+geom_smooth(se=FALSE, col='black')+geom_point(alpha=0.05)+stat_summary(geom = "line", fun = "mean", col='black')+stat_summary(geom = "line", fun = "quantile", fun.args = list(probs=0.25), col='blue', linetype=2)+stat_summary(geom = "line", fun = "quantile", fun.args = list(probs=0.75), col='blue', linetype=2)+facet_wrap(~borough, scales = 'free')
ggplot(query_table, aes(x=pickup_dt, y=pickups))+geom_smooth(se=FALSE)+geom_point(alpha=0.1)+stat_summary(geom = "line", fun = "mean")+stat_summary(geom = "line", fun = "quantile", fun.args = list(probs=0.25), col='blue', linetype=2)+stat_summary(geom = "line", fun = "quantile", fun.args = list(probs=0.75), col='blue', linetype=2)
