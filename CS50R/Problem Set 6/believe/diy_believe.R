# DIY Code (just for fun)

library(stringr)

upper <- str_to_upper(letters)

# Main function - Caesar text cipher
caesar <- function(str, key){
  # Error handling
  if (missing(str) || missing(key)) {
    stop("No input provided. Stopping...")
  }
  str <- str_flatten(as.character(str))
  if (str %in% c(NA, NULL, "")){
    stop("Invalid string provided. Stopping...")
  }
  if (!is.numeric(key) || key %in% c(Inf, -Inf)){
    warning("Invalid key used. Returning string.")
    return(str)
  }

  # Cipher text generation
  result <- character()
  for (item in str_split(str, "")[[1]]){
    if (!(item %in% c(letters, upper))){
      result <- c(result, item)
      next
    }

    # Character index list
    active <- c()
    if (item %in% letters){
      active <- letters
    } else if (item %in% upper){
      active <- upper
    }

    index <- get_index(item, active)
    index <- (index + key) %% 26
    result <- c(result, active[index])
  }

  return(str_flatten(result))
}


# Helper function - Get index number of value in list
get_index <- function(value, list){
  index <- 1
  for (item in list){
    if (item == value){
      return(index)
    }
    index <- index + 1
  }

  return(NA)
}
