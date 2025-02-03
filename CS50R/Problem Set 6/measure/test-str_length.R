library(stringr)
library(testthat)

test_that("str_length handles string", {
  expect_equal(str_length("cat"), 3)
  expect_equal(str_length("123&/^>]=.,'"), 12)
  expect_equal(str_length(""), 0)
})

test_that("str_length handles bulk input", {
  expect_equal(str_length(c("123","abc")), c(3, 3))
  expect_equal(str_length(data.frame(c("abc"))), c(3))
})

test_that("str_length handles NA values", {
  expect_equal(str_length(NA), as.numeric(NA))
  expect_equal(str_length(c("dog", NA)), c(3, NA))
})

test_that("str_length handles non-character inputs", {
  expect_equal(str_length(123), 3)
  expect_equal(str_length(NaN), 3)
  expect_equal(str_length(NULL), numeric(0))
  expect_equal(str_length(Inf), 3)
  expect_equal(str_length(-Inf), 4)
})

test_that("str_length handles error", {
  expect_error(str_length())
})