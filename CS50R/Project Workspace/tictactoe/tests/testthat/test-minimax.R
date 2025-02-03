test_that("minimax handles score evaluation", {
  expect_equal(
    minimax(
      c("X","O","X","X","O","O","O","X","X"),
      "X",
      "O"
    ),
    0
  )

  expect_equal(
    minimax(
      c("","X","","","O","","","","O"),
      "O",
      "O"
    ),
    1
  )

  expect_equal(
    minimax(
      c("X","O","O","","","","X","",""),
      "X",
      "O"
    ),
    -1
  )

  expect_equal(
    minimax(
      c("X","","","","O","","X","",""),
      "X",
      "O"
    ),
    0
  )
})

test_that("minimax handles best move", {
  expect_equal(
    minimax(
      c("","X","","","O","","","","O"),
      "O",
      "X",
      get_max = TRUE
    ),
    1
  )

  expect_equal(
    minimax(
      c("X","O","O","","","","X","",""),
      "X",
      "X",
      get_max = TRUE
    ),
    4
  )
})