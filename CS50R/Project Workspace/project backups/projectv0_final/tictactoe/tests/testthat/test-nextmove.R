test_that("nextmove handles next move", {
  expect_equal(
    nextmove(c("","","","","","","","",""), "X", 1),
    c("X","","","","","","","","")
  )
})