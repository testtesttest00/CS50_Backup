# install.packages("tidyverse")
suppressWarnings(library("dplyr"), library("tidyr"))

load("air.RData")

air <- air |>
  dplyr::group_by(source = level_1, pollutant) |>
  dplyr::summarize(emissions = sum(emissions), .groups = "drop") |>
  dplyr::arrange(source, pollutant)

save(air, file = "7.RData")
rm(list = ls())
