# install.packages("tidyverse")
suppressWarnings(library("tidyverse"))

zelda <- readr::read_csv("zelda.csv") |>
  tidyr::pivot_wider(names_from = role, values_from = names) |>
  tidyr::separate(release, sep = " - ", into = c("year", "system")) |>
  dplyr::rename_with(stringr::str_to_lower)

save(zelda, file = "zelda.RData")
rm(list = ls())