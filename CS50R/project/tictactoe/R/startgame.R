startgame <- function(gamemode = "", symbol = "", first = ""){
  board <- c("", "", "", "", "", "", "", "", "")

  while (!(gamemode %in% c("AI", "VS"))){
    cat("\n")
    gamemode <- toupper(readline("Choose your game mode: \n(Enter AI or VS)\n"))
  }
  while (!(symbol %in% c("X", "O"))){
    cat("\n")
    symbol <- toupper(readline("Choose your symbol: \n(Enter X or O)\n"))
  }
  while (!(first %in% c("X", "O"))){
    cat("\n")
    first <- toupper(readline("Who should go first? \n(Enter X or O)\n"))
  }

  return(c(
    gamemode,
    symbol,
    first,
    board
  ))
}