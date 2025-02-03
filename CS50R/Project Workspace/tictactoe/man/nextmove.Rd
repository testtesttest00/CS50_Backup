\name{nextmove}
\alias{nextmove}
\title{Next Tic-Tac-Toe Move}
\description{Updates the game board}
\usage{
  startgame(board, first, position)
}
\arguments{
  board: numeric vector of [1:9]\cr
  first: character of player that goes first\cr
  position: numeric board position to make next move
}
\value{
  Returns the updated numeric game board vector
}
\examples{
  startgame( \cr
    board = c("","","","","","","","","X"),\cr
    first = "X",\cr
    position = 1\cr
  )
  >>> "O","","","","","","","","X"
}
