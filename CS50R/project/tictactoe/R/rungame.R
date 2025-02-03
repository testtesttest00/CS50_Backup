rungame <- function(){
  message("\n==== Tic-Tac-Toe v1 ====")
  game_info <- startgame()
  gamemode <- game_info[1]
  player <- game_info[2]
  player2 <- c("X", "O")[which(c("X", "O") != player)]
  first <- game_info[3]
  board <- game_info[4:12]
  turn <- 0
  winner <- NA

  message("\nGame start...")
  while (is.na(winner)){
    initiative <- nextmove(board, first, 1)[1]
    cat(
      "\n== Turn: ", turn, " ==\n\n",
      printboard(board), "\n",
      "== ", initiative, "  move ==", sep = ""
    )
    move <- NA
    while (!(move %in% availablemoves(board))){
      if (gamemode == "AI" & initiative == player2){
        cat("\nAI Moving...\n")
        move <- minimax(board, first, player2, get_max = TRUE)
        break
      }
      move <- suppressWarnings(as.integer(readline("Enter your move (1-9): ")))
    }
    board <- nextmove(board, first, move)
    turn <- turn + 1
    winner <- checkwin(board)
    if (turn >= 9){
      turn <- 9
      break
    }
  }

  if (!is.na(winner)){
    cat(
      "\n== Turn: ", turn, " ==\n\n",
      printboard(board), "\n",
      "=== ", winner, " won ===", sep = ""
    )
  } else {
    cat(
      "\n== Turn: ", turn, " ==\n\n",
      printboard(board), "\n",
      "==== Tie ====", sep = ""
    )
  }
  message("\n\nThank you for playing")
}