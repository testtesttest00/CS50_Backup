alphabet <- c(
  "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
  "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
)
characters <- 20
pause <- 0.25

random_character <- function() {
  return(sample(alphabet, 1))
  # alphabet can be replaced by in-built "letters", i.e.,
  # return(sample(letters, 1))
}

print_sequence <- function(length) {
  while (length > 0){
    cat(random_character())
    Sys.sleep(pause)
    length <- length - 1
  }
  cat("\n")
}

print_sequence(characters)

rm(list = ls())
