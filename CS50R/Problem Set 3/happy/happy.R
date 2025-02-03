# Version 2

years <- c("2020", "2021", "2022", "2023", "2024")

country <- readline("Country: ")

for (year in years){
  data <- read.csv(paste0(year, ".csv"))
  if (country %in% data$country){
    data <- data[country == data$country, ]
    data <- data[!c(is.na(suppressWarnings(as.integer(data))))]
    score <- round(apply(data, MARGIN = 1, sum), 2)
  }else{
    score <- "Unavailable"
  }
  cat(
    country, " (", year, ")", ": ", score, "\n",
    sep = ""
  )
}

rm(list = ls())


# Version 1
#
# years <- c("2020", "2021", "2022", "2023", "2024")
#
# print_score <- function(country, year, matrix){
#   if (nrow(matrix) == 0){
#     score <- "Unavailable"
#   }else{
#     score <- round(sum(suppressWarnings(as.numeric(matrix)), na.rm = TRUE) , 2)
#   }
#   cat(country," (", year, ")", ": ", score , "\n", sep="")
# }
#
# country <- readline("Country: ")
#
# for (year in years){
#   data <- read.csv(paste0(year, ".csv"))
#   print_score(
#     country, year, data[country == data$country,]
#   )
# }