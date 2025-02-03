# install.packages("tidyverse")
suppressWarnings(library("tidyverse"))

load("zelda.RData")

zelda <- zelda[stringr::str_detect(zelda$producers, ","), ] |>
  dplyr::group_by(title) |>
  dplyr::slice_min(year) |>
  dplyr::arrange(year, title, system)

save(zelda, file = "5.RData")
rm(list = ls())