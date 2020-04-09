library(dplyr)
library(tidyr)
library(ggplot2)

filename <- "uber_nyc_enriched.csv"
df <- read.csv(filename, header = TRUE)

# df$pickup_dt <- as.POSIXct(df$pickup_dt)

# pivot <- df %>%
#   select(temp, borough, pickups)%>%
#   group_by(temp)

query_table <- subset(df, borough=='Manhattan')
# query_table <- query_table[order(query_table$temp),]
 # order(query_table$pickups)
query_table <- query_table%>%
  mutate(over_75=ifelse(temp>75,'>=75','<75'))
# query_table$temp = cut(query_table$temp, breaks = c(-Inf, 75, Inf), labels = c('Low', 'High'), right = F)
# query_table$temp = factor(ifelse(as.numeric(query_table$temp) >=75, "High", "Low"))

ggplot(query_table, aes(x=over_75, y=pickups))%>%
  +geom_boxplot()%>%
  +xlab("Temperature")%>%
  +ylab("Pickups")
