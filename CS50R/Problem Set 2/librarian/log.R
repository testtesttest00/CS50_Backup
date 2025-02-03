# Load database:
books <- read.csv("books.csv")
authors <- read.csv("authors.csv")


# Question 1 - The Writer
# Your first reader of the day walks up to your desk and greets you:
# Dearest librarian, curator, cataloger!
# I yearn, hunger, dream for the author Mia Morgan’s sole, only, exclusive book!
# Please uncover it, fetch it, retrieve it for me.
# I will owe you a great debt, a wonderful sum, an immortal obligation.

cat(
  "The Writer -",
  books[books$author == "Mia Morgan", ]$title,
  "\n"
)

# Question 2 - The Musician
# A reader with a ukulele walks up to your desk:
# Hey, I’m on the lookout for a book on the topic of music, a real classic.
# I think it hit the shelves back in 1613. Music history is just so fascinating,
# don’t you think?

cat(
  "The Musician -",
  books[books$year == "1613" & books$topic == "Music",]$title,
  "\n"
)

# Question 3 - The Traveler
# A hunched, cloaked figure approaches your desk,
# handing you a sheet of paper without saying a word.
# On it, you see two possible author names:
# Lysandra Silverleaf or Elena Petrova.
# Below, you see the year in which the book was published: 1775

cat("The Traveler -",
    as.character(subset(
      books,
      (author == "Lysandra Silverleaf" | author == "Elena Petrova")
      & year == "1775"
    )$title),
    "\n"
)

# Question 4 - The Painter
# From behind, you hear a reader call to you:
# Oh, I remember this wonderful book on the topic of art from my childhood!
# It was like a burst of colors—vivid reds, soothing blues, vibrant yellows.
# It was not too long, not too short, probably between 200 and 300 pages.
# And it was definitely published in either 1990 or 1992,
# but absolutely not 1991.

cat("The Painter -",
    as.character(subset(
      books,
      as.integer(pages) >= 200 & as.integer(pages) <= 300
      & (year == "1990" | year == "1992")
    )$title),
    "\n"
)

# Question 5 - The Scientist
# You receive a phone call:
# I need the book with “Quantum Mechanics” in the title.

cat("The Scientist -",
    as.character(subset(
      books,
      grepl("*Quantum Mechanics*", title)
    )$title),
    "\n"
)

# Question 6 - The Teacher
# A small knock on the door reveals your next reader:
# Apologies for the trouble,
# but I’m looking for a book on the topic of education published in the 1700s.
# Unfortunately, I can’t recall the author,
# but I do remember they hailed from the town of Zenthia.

cat("The Teacher -",
    books[1700 <= books$year & books$year <=1800
          & books$author %in%
            authors[authors$hometown == "Zenthia",]$author,]$title,
    "\n"
)

# Clear environment
rm(list = ls())