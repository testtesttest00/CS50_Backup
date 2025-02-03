test_that("printboard returns pretty print string", {
  expect_equal(
    printboard(c("","","","O","X","X","","X","")),
    "    1 2 3 \n  1       \n  4 O X X \n  7   X   \n"
  )

  expect_output(cat(printboard(c("","","","O","X","X","","X",""))))
})