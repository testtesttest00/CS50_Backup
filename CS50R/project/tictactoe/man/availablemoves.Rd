\name{availablemoves}
\alias{availablemoves}
\title{Available Tic-Tac-Toe Move}
\description{Lists the available moves remaining}
\usage{
  availablemoves(board)
}
\arguments{
  board: numeric vector of [1:9]
}
\value{
  Returns a numeric vector of available moves remaining
}
\examples{
  availablemoves(board = c("X","X","O","O","","","","","X"))
  >>> c(5, 6, 7, 8)
}
