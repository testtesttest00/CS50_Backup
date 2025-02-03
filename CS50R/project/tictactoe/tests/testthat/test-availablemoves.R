test_that("availablemoves return a vector of remaining moves", {
  expect_equal(
    availablemoves(c("X","X","O","O","","","","","X")),
    c(5, 6, 7, 8)
  )
  expect_equal(
    availablemoves(c("X","X","O","O","X","X","O","O","X")),
    numeric()
  )
})