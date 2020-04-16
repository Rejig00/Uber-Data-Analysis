library(dplyr)
library(tidyr)
library(ggplot2)

filename <- "uber_nyc_enriched.csv"
df <- read.csv(filename, header = TRUE)

query_table = subset(df, df$borough=='Manhattan')
query_table$hday <- as.factor(query_table$hday)

t.test(query_table$pickups~query_table$hday, mu=0, alt="two.sided", conf=0.95, paired=FALSE)