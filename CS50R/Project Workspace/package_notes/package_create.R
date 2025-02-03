# Create directory for your package
dir.create("your package")
setwd("your package")

# Create description and license files for your package
file.create(DESCRIPTION)
# Package: your package
# Title:
# Description:
# Version:
# Authors@R: person("first", "last", email = "", role = c("aut", "cre", "cph"))
# License: MIT + file LICENSE
# Suggests:
# Requires:
file.create(LICENSE)
# YEAR: ...
# COPYRIGHT HOLDER: your package authors

# Use devtools package to create own packages
install.packages(devtools)
library(devtools)

# Create test directory
use_testthat()
# Automatically updates description
# Suggests:
#   testthat (>= 3.0.0)
# Config/testthat/edition: 3

# Run all files in test directory
test()

# Create R directory and/or a R file inside
use_r("function_name")

# Creates namespace of all functions
file.create(NAMESPACE)
# export(function_name)

# Loads or tests all functions present in namespace file
load_all()

# Create function manuals (?alias >> opens help tab)
dir.create("man")
file.create("man/function_name.Rd")
# \name{function_name}
# \alias{function name}
# \title{}
# \description{}
# \usage{
#   function_name()
# }
# \value{
#   return value
# }
# \examples{
#   function_name()
# }

# Create and use your package
build()
install.packages("your_package.tar.gz")
