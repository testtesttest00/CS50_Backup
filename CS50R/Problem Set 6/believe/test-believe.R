# ChatGPT 4.0 Code for cipher text (made after DIY ver.)

source("./believe.R")
library(testthat)

test_that("caesar handles normal input", {
  expect_equal(caesar("ABC", 1), "BCD")
  expect_equal(caesar("abc", 1), "bcd")
  expect_equal(caesar("zZ", 1), "aA")
  expect_equal(caesar("123!@#-=_+;',./", 1), "123!@#-=_+;',./")
  expect_equal(caesar("", 1), "")
})

test_that("caesar handles missing inputs", {
  expect_error(caesar(,1))
  expect_error(caesar("abc",))
})

test_that("caesar handles invalid string input", {
  expect_error(caesar(NA, 1))
  expect_error(caesar(NULL, 1))
  expect_error(caesar(c("abc", "ABC"), 1))
})

test_that("caesar handles invalid key input", {
  expect_error(caesar("abc", "1"))
  expect_error(caesar("abc", ""))
  expect_error(caesar("abc", Inf))
  expect_error(caesar("abc", -Inf))
  expect_error(caesar("abc", c(1, 2, 3)))
  expect_error(caesar("abc", 10.5))
})
