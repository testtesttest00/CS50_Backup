# install.packages("tidyverse")
suppressWarnings(library("tidyverse"))

load("zelda.RData")

zelda <- zelda[stringr::str_detect(zelda$producers, "Shigeru Miyamoto"), ] |>
  dplyr::group_by(title) |>
  dplyr::slice_min(year) |>
  dplyr::arrange(year, title, system)

save(zelda, file = "4.RData")
rm(list = ls())