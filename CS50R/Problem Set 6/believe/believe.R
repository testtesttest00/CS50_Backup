# ChatGPT 4.0 Code for cipher text (made after DIY ver.)

caesar <- function(original_text, key) {
  # Check for missing inputs
  if (missing(original_text) || missing(key)) {
    stop("Both 'original_text' and 'key' must be provided.")
  }

  # Check if original_text is a character vector and not NULL or NA
  if (!is.character(original_text) || length(original_text) != 1 || is.null(original_text) || is.na(original_text)) {
    stop("'original_text' must be a single non-NULL, non-NA string.")
  }

  # Check if key is a numeric value, a single element, and an integer, not Inf or -Inf
  if (!is.numeric(key) || length(key) != 1 || key != floor(key) || is.infinite(key)) {
    stop("'key' must be a single integer, and cannot be Inf or -Inf.")
  }

  # Normalize the key to be within the range of 0-25
  key <- key %% 26

  # Function to encrypt a single character
  encrypt_char <- function(char) {
    if (grepl("[A-Za-z]", char)) {
      ascii_offset <- ifelse(grepl("[A-Z]", char), 65, 97)
      new_char <- intToUtf8((utf8ToInt(char) - ascii_offset + key) %% 26 + ascii_offset)
      return(new_char)
    }
    return(char)  # Return non-alphabetic characters unchanged
  }

  # Create the ciphertext
  ciphertext <- sapply(strsplit(original_text, NULL)[[1]], encrypt_char)

  return(paste(ciphertext, collapse = ""))
}

# Example usage
# caesar("Hello, World!", 3)  # Output: "Khoor, Zruog!"
