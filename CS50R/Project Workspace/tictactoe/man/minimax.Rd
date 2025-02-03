\name{minimax}
\alias{minimax}
\title{Tic-Tac-Toe Minimax AI}
\description{Implement the minimax algorithm in Tic-Tac-Toe}
\usage{
  minimax(board, first, symbol, min_max, get_max = FALSE)
}
\arguments{
  board: numeric vector of [1:9]\cr
  first: character of player which moves first\cr
  symbol: character of player's point of view to consider\cr
  get_max: bool to enable returning of numeric best move
}
\value{
  If get_max is FALSE, minimax() returns the numeric evaluation for
  a symbol (player) at the current board state\cr
  (bigger values means better position)
  \cr\cr
  If get_max is TRUE, minimax() returns the numeric best move
  at current board state\cr
  (symbol has to be the one taking the next move)
}
\examples{
  minimax(\cr
    c("X","O","X","X","O","O","O","X","X"),\cr
    "X",\cr
    "X",\cr
  )
  >>> 0
  minimax(\cr
    c("X","X","","","","","O","","O"),\cr
    "X",\cr
    "O",\cr
  )
  >>> -1
  minimax(\cr
    c("X","X","","","","","O","","O"),\cr
    "X",\cr
    "X",\cr
  )
  >>> 1
  minimax(\cr
    c("X","X","","","","","O","","O"),\cr
    "X",\cr
    "X",\cr
    get_max = TRUE\cr
  )
  >>> 3
  minimax(\cr
    c("X","X","","X","","","O","","O"),\cr
    "X",\cr
    "O",\cr
    get_max = TRUE\cr
  )
  >>> 3
}
