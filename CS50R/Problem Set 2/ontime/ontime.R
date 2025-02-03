# Loads database
routes <- rbind(read.csv("bus.csv"), read.csv("rail.csv"))

# Processes route reliability
request <- readline("Route: ")
if (request %in% routes$route){

  # Trim required data
  routes <- subset(routes, route == request)
  peak <- subset(routes, peak == "PEAK")
  offpeak <- subset(routes, peak == "OFF_PEAK")

  # Reliability calculations
  peak_reliability <- mean(peak$numerator / peak$denominator)
  offpeak_reliability <- mean(offpeak$numerator / offpeak$denominator)

  # Printing conclusions
  cat("On time",
      paste(round(peak_reliability, 2)*100, "%", sep=""),
      "of the time during off-peak hours.",
      "\n"
  )
  cat("On time",
      paste(round(offpeak_reliability, 2)*100, "%", sep=""),
      "of the time during off-peak hours.",
      "\n"
  )

}else{
  print("Invalid route")
}

# Clear environment
rm(list = ls())