# install.packages("tidyverse")
suppressWarnings(library("dplyr"), library("tidyr"))

load("air.RData")

air <- air |>
  dplyr::filter(county == "OR - Clackamas")

save(air, file = "3.RData")
rm(list = ls())