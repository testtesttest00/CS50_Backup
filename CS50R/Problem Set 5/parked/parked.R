# install.packages("tidyverse")
library("tidyverse")

lyrics <- readr::read_file("lyrics/astley.txt")

# Clean up lyrics, split into vector, coerce into tibble
lyrics <- lyrics |>
  stringr::str_to_lower() |>
  stringr::str_replace_all("[^\\w']", " ") |>
  stringr::str_split("\\s+")

lyrics <- lyrics[[1]]
lyrics <- lyrics[ !lyrics == "" ] |>
  tidyr::as_tibble() |>
  dplyr::group_by(value) |>
  dplyr::summarize(count = n()) |>
  #dplyr::filter(count > 5) |>
  dplyr::arrange(desc(count)) |>
  dplyr::slice(1:20)

# Locks x value sequence in place using factor
lyrics$value <- factor(
  lyrics$value, lyrics$value
)

# Plot column graph
p <- ggplot2::ggplot(
  lyrics,
  ggplot2::aes(x = value, y = count)
) +
  ggplot2::geom_col(
    ggplot2::aes(fill = value)
  ) +
  ggplot2::guides(
    fill = "none"
  ) +
  ggplot2::labs(
    x = "words",
    y = "count",
    title = "top 20 frequent lyrics in astley"
  ) +
  ggplot2::theme_classic() +
  ggplot2::theme(
    axis.text.x = element_text(angle = 45, hjust = 1)
  )

# Save and clear environment
ggplot2::ggsave(
  "lyrics.png",
  p,
  height = 900,
  width = 1200,
  units = "px"
)

rm(list = ls())
