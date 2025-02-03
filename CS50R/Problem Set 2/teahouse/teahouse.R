flavour = readline("Flavor: ")
# Check for valid flavor input
if (flavour %in% c("Light", "Bold")){

  caffeine = readline("Caffeine: ")
  # Check for valid caffeine input
  if (caffeine %in% c("Yes", "No")){

    # Process tea for light flavors
    if (flavour == "Light"){
      if (caffeine == "No"){
        print("Yout might like chamomile")
      }else{
        print("You might like green tea")
      }
    # Process tea for bold flavors
    }else{
      if (caffeine == "No"){
        print("You might like rooibos")
      }else{
        print("You might like black tea")
      }
    }

  }else{
    cat("Enter either \"No\" or \"Yes\" for caffeine")
  }

}else{
  cat("Enter either \"Light\" or \"Bold\" for flavor")
}

# Clear environment
rm(list = ls())
