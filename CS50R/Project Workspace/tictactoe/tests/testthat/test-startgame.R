test_that("startgame initialises game vector", {
  expect_equal(
    startgame(gamemode="AI", symbol="X", first = "X"),
    c(
      "AI", # Game mode
      "X", # Player's symbol
      "X", # First move symbol
      c("", "", "", "", "", "", "", "", "") # Game board
    )
  )
})