hunger = readline("How hungry are you: ")
# Check for valid hunger input
if (hunger %in% c("Very", "Not really")){

  money = readline("How much money do you have: ")
  # Check for valid money input
  if (money %in% c("A lot", "None")){

    # For hungry people
    if (hunger == "Very"){
      if (money == "A lot"){
        print("Steak")
      }else{
        print("Rice")
      }
    # For not-that-hungry people
    }else{
      if (money == "A lot"){
        print("Scallop")
      }else{
        print("Biscuit")
      }
    }

  }else{
    cat("Enter \"A lot\" or \"None\"")
  }

}else{
  cat("Enter \"Very\" or \"Not really\"")
}

# Clear environment
rm(list = ls())
