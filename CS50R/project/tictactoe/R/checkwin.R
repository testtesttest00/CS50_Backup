checkwin <- function(board){
  if (missing(board)){
    stop("Insufficient arguments provided. Stopping...")
  }

  for (player in c("X", "O")){
    # Check vertical
    for (i in 1:3){
      if (player == board[i] && player == board[i+3] && player == board[i+6]){
        return(player)
      }
    }

    # Check horizontal
    for (i in c(1, 4, 7)){
      if (player == board[i] && player == board[i+1] && player == board[i+2]){
        return(player)
      }
    }

    # Check diagonal
    for (i in c(1, 3)){
      j = 4 - (i - 1) #j = 4 if i = 1, j = 2 if i = 3
      if (player == board[i] && player == board[i+j] && player == board[i+2*j]){
        return(player)
      }
    }
  }

  return(NA)
}