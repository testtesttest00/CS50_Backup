# install.packages("tidyverse")
suppressWarnings(library("dplyr"), library("tidyr"))

load("air.RData")

air <- air |>
  dplyr::filter(county == "OR - Clackamas") |>
  dplyr::arrange(dplyr::desc(emissions))

save(air, file = "4.RData")
rm(list = ls())
