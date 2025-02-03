test_that("checkwin determines winner", {
  expect_equal(
    checkwin(c("X","X","X","O","O","","","","")),
    "X"
  )
  expect_equal(
    checkwin(c("","","","","","","","","")),
    NA
  )
})