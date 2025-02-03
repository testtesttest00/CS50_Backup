# install.packages("tidyverse")
library(tidyverse)

# Singapore CMPB Gross Allowance for Service Vocations in National Service
scheme <- data.frame(
  Rank = c("REC", "PTE", "LCP", "CPL"),
  Gross.Allowance = c(680+75, 680+75, 700+75, 750+75)
)

# Rank Progression Over the Past 2 Years
progression <- c(
  "REC","REC","PTE","PTE","PTE","PTE","PTE","PTE","PTE","PTE","PTE","PTE",
  "PTE","PTE","LCP","LCP","LCP","LCP","LCP","LCP","LCP","LCP","CPL","CPL"
)

# Total Allowance Earned
allowance <- c(0)
for (rank in progression){
  allowance <- c(
    allowance,
    scheme[scheme$Rank == rank,]$Gross.Allowance + allowance[length(allowance)]
  )
}
allowance <- allowance[2:length(allowance)]

# Add Months to Allowance
allowance <- data.frame(
  Allowance = allowance,
  Month = 1:length(allowance)
)

# Plot and Save Allowance Line Graph
p <- ggplot(
  allowance,
  aes(x = Month, y = Allowance),
  color ="black"
) +
  geom_line(
    color = "#6FBB5FFF"
  ) +
  geom_point(
    shape = 4,
    color = "#1F4F2FCF"
  ) +
  geom_hline(
    yintercept = 10000,
    linetype = 2,
    color = "#1F6F2FCF"
  ) +
  geom_vline(
    xintercept = 12,
    linetype = 10,
    color = "#8FBB5FFF"
  ) +
  scale_y_continuous(
    limits = c(0, 20000),
    breaks = seq(0, 20000, by = 2500)
  ) +
  scale_x_continuous(

    breaks = unique(allowance$Month)
  ) +
  labs(
    title = "Accumulated NS Allowance ($SGD)"
  ) +
  theme(
    plot.background = element_rect(fill = "#4F8F4F40"),
    panel.background = element_rect(fill = "#9FFF7F50"),
    title = element_text(color = "#103010FF", family = "mono-bold"),
    axis.line = element_line(color = "#1A4F1FFF"),
    axis.text= element_text(
      color = "#123F21F3",family = "sans-bold",angle = 60, hjust = 1
    )
  )

ggsave(
  "visualization.png",
  p,
  height = 900,
  width = 1200,
  units = "px"
)
rm(list = ls())