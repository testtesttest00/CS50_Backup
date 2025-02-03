\name{printboard}
\alias{printboard}
\title{Print Tic-Tac-Toe Board}
\description{Pretty-prints a Tic-Tac-Toe board}
\usage{
  printboard(board)
}
\arguments{
  board: numeric vector of [1:9]
}
\value{
  Returns a pretty-printed character string to be passed into cat()
}
\examples{
  printboard(c("","","","O","X","X","","X",""))
  >>> "    1 2 3 \n  1       \n  4 O X X \n  7   X   \n"
  cat(printboard(c("","","","O","X","X","","X","")))
  >>>   1 2 3 \cr
      1\cr
      4 O X X\cr
      7   X
}
