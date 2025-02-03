\name{startgame}
\alias{startgame}
\title{Start a Tic-Tac-Toe Game}
\description{Initialises a game vector}
\usage{
  startgame()
  startgame(gamemode = "", symbol = "", first = "")
}
\arguments{
  gamemode: character string of game mode\cr
  symbol: character string of player symbol\cr
  first: character string of first move symbol
}
\value{
  Returns a informational vector containing: \cr
  \cr
  1) Character game mode (AI or VS) \cr
  2) Character player's symbol (X or O) \cr
  3) Character first move symbol (X or O) \cr
  4) Numeric vector of starting board state
}
\examples{
  startgame(gamemode = "AI", symbol = "X", first = "X")
  >>> c("AI", "X", "X", "", "", "", "", "", "", "", "", "")
}
