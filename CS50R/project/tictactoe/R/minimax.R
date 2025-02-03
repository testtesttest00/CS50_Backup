minimax <- function(board, first, symbol, get_max = FALSE){
  # Checks if terminal state is reached
  if (!is.na(checkwin(board))){
    if (get_max){
      return(NA)
    }
    if (checkwin(board) == symbol){
      return(1)
    } else if(checkwin(board) != symbol){
      return(-1)
    }
  } else if (length(availablemoves(board)) == 0){
    if (get_max){
      return(NA)
    }
    return(0)
  }

  # Since symbol is defined to be +ve scoring,
  # if symbol goes next, find best score it can make
  # else, find worst score it can take
  # e.g. minimax < c(X,X, , , , , ,O,O),X,O
  # finding max score o can make is pointless
  # if it cant even make that move
  info <- c(board, "", "")
  initiative <- nextmove(info, first, length(info))[length(info)]
  # space_left <- 0
  # for (space in seq_along(board)){
  #   if (board[space] == ""){
  #     space_left <- space_left + 1
  #   }
  # }
  # initiative <- NA
  # if (space_left %% 2 == 1){
  #   initiative <- first
  # } else {
  #   initiative <- c("X", "O")[which(c("X", "O") != first)]
  # }
  min_max <- NA
  if (initiative == symbol){
    min_max <- "max"
  } else {
    min_max <- "min"
  }

  # Situation - available moves and no winners yet
  if (min_max == "max"){
    best_score <- -Inf
    if (get_max){
      best_move <- NA
    }
    for (action in availablemoves(board)){
      temp_board <- nextmove(board, first, action)
      new_score <- minimax(temp_board, first, symbol)
      if (new_score > best_score){
        best_score <- new_score
        if (get_max){
          best_move <- action
        }
      }
    }
    if (get_max){
      return(best_move)
    }
    return(best_score)
  } else if (min_max == "min"){
    worst_score <- Inf
    for (action in availablemoves(board)){
      temp_board <- nextmove(board, first, action)
      new_score <- minimax(temp_board, first, symbol)
      if (new_score < worst_score){
        worst_score <- new_score
      }
    }
    return(worst_score)
  }
}