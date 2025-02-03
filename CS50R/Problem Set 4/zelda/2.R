# install.packages("tidyverse")
suppressWarnings(library("tidyverse"))

load("zelda.RData")

zelda <- zelda |>
  dplyr::group_by(year) |>
  dplyr::summarize(releases = n()) |>
  dplyr::arrange(desc(releases))

save(zelda, file = "2.RData")
rm(list = ls())