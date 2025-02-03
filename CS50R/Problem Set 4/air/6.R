# install.packages("tidyverse")
suppressWarnings(library("dplyr"), library("tidyr"))

load("air.RData")

air <- air |>
  dplyr::group_by(pollutant) |>
  # emissions was previously not numeric as as_tibbles was used (not used readr)
  dplyr::summarize(emissions = sum(as.numeric(emissions), na.rm = TRUE)) |>
  dplyr::arrange(dplyr::desc(emissions))

save(air, file = "6.RData")
rm(list = ls())
