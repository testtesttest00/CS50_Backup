# install.packages("tidyverse")
suppressWarnings(library("tidyverse"))

load("zelda.RData")

zelda <- zelda |>
  dplyr::group_by(title) |>
  dplyr::slice_min(year) |>
  dplyr::arrange(year, title, system)

save(zelda, file = "3.RData")
rm(list = ls())