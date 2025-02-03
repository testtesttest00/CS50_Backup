# install.packages("tidyverse")
suppressWarnings(library("dplyr"), library("tidyr"))

load("air.RData")

air <- air |>
  dplyr::arrange(dplyr::desc(emissions))

save(air, file = "2.RData")
rm(list = ls())