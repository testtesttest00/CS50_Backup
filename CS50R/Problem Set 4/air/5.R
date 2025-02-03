# install.packages("tidyverse")
suppressWarnings(library("dplyr"), library("tidyr"))

load("air.RData")

air <- air |>
  dplyr::group_by(county) |>
  dplyr::slice_max(emissions) |>
  dplyr::arrange(county)

save(air, file = "5.RData")
rm(list = ls())
