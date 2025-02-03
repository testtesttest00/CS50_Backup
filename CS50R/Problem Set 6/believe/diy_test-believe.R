# DIY Code (just for fun)

source("./diy_believe.R")
library(testthat)

test_that("caesar handles normal input", {
  expect_equal(caesar("ABC", 1), "BCD")
  expect_equal(caesar("abc", 1), "bcd")
  expect_equal(caesar("zZ", 1), "aA")
  expect_equal(caesar("123!@#-=_+;',./", 1), "123!@#-=_+;',./")
})

test_that("caesar handles missing inputs", {
  expect_error(caesar(,1))
  expect_error(caesar("abc",))
})

test_that("caesar handles invalid string input", {
  expect_error(caesar(NA, 1))
  expect_error(caesar(NULL, 1))
  expect_error(caesar("", 1))
})

test_that("caesar handles invalid key input", {
  expect_warning(caesar("abc", "1"))
  expect_equal(suppressWarnings(caesar("abc", "1")), "abc")
  expect_warning(caesar("abc", ""))
  expect_equal(suppressWarnings(caesar("abc", "")), "abc")
})

test_that("caesar handles Inf and -Inf as string input", {
  expect_equal(caesar(Inf, 1), "Jog")
  expect_equal(caesar(-Inf, 1), "-Jog")
})

test_that("caesar handles Inf and -Inf as key input", {
  expect_warning(caesar("abc", Inf))
  expect_equal(suppressWarnings(caesar("abc", Inf)), "abc")
  expect_warning(caesar("abc", -Inf))
  expect_equal(suppressWarnings(caesar("abc", -Inf)), "abc")
})