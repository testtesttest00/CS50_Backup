nextmove <- function(board, first, position){
  if(missing(board) | missing(first) | missing(position)){
    stop("Insufficient arguments provided. Stopping...")
  }

  spaceleft <- 0
  for (space in board){
    if (space == ""){
      spaceleft <- spaceleft + 1
    }
  }

  if (spaceleft %% 2 == 1){
    board[position] <- first
  } else {
    second <- c("X", "O")[c("X", "O") != first]
    board[position] <- second
  }

  return(board)
}