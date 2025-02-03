\name{checkwin}
\alias{checkwin}
\title{Check Tic-Tac-Toe Win}
\description{Check if a player has 3-in-a-row on a board state}
\usage{
  checkwin(board)
}
\arguments{
  board: numeric vector of [1:9]
}
\value{
  Returns the character symbol of the winner, or NA if no winner is found
}
\examples{
  checkwin(board = c("X","X","X","O","O","","","",""))
  >>> "X"
  checkwin(board = c("","","","","","","","",""))
  >>> NA
}
