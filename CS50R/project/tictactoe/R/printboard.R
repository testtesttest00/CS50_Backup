printboard <- function(board){
  if (missing(board)){
    stop("Insufficient arguments provided. Stopping..")
  }

  for (value in seq_along(board)){
    if (board[value] == ""){
      board[value] <- " "
    }
  }

  pretty <- paste(
    "   ", "1", "2", "3", "\n",
    " 1", board[1], board[2], board[3], "\n",
    " 4", board[4], board[5], board[6], "\n",
    " 7", board[7], board[8], board[9], "\n"
  )

  return(pretty)
}