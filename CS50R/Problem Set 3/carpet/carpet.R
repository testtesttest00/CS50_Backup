calculate_growth_rate <- function(years, visitors) {
  # Define indices
  earliest = 1
  latest = length(years)

  # Return formula value
  return((visitors[latest]-visitors[earliest])/(years[latest]-years[earliest]))
}

predict_visitors <- function(years, visitors, year) {
  # Handles existing data
  if (year %in% years){
    return(visitors[which(year == years)])
  }

  # Get average yearly growth rate
  rate <- calculate_growth_rate(years, visitors)

  # Define helper values
  if (year < years[1]){
    index <- 1
    multiplier <- -1
  }
  else {
    index <- length(years)
    multiplier <- 1
  }
  steps <- year - years[index]
  people <- visitors[index]

  # Calculates visitor count
  for (i in rep(multiplier, abs(steps))){
    people <- people + rate * i
  }
  return(people)
}

visitors <- read.csv("visitors.csv")
year <- as.integer(readline("Year: "))
predicted_visitors <- predict_visitors(visitors$year, visitors$visitors, year)
cat(paste0(predicted_visitors, " million visitors\n"))
