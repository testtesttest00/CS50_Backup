# install.packages("tidyverse")
suppressWarnings(library("tidyverse"))

air <- readr::read_csv("air.csv")

air <- air |>
  dplyr::select(
    state = State,
    county = "State-County",
    pollutant = POLLUTANT,
    emissions = "Emissions (Tons)",
    level_1 = "SCC LEVEL 1",
    level_2 = "SCC LEVEL 2",
    level_3 = "SCC LEVEL 3",
    level_4 = "SCC LEVEL 4"
  )

save(air, file = "air.RData")
rm(list = ls())