availablemoves <- function(board){
  if (missing(board)){
    stop("Insuffient arguments provided. Stopping...")
  }

  available <- numeric()
  for (space in seq_along(board)){
    if (board[space] == ""){
      available <- c(available, space)
    }
  }

  return(available)
}