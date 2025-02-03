# Processes csv file into a data frame
filename <- readline("Enter a file name:")
pitstops <-read.csv(filename)

# Prints number of pit stops and minimum, maximum, and total pit stop times
print(nrow(pitstops))
print(min(pitstops$time))
print(max(pitstops$time))
print(sum(pitstops$time))

# Clears environment at the end
rm(list = ls())