# Reads tsv source file as a data frame
survey = read.table("tests.tsv", sep="\t", header=TRUE)

# Replaces gender values with textual representation
survey$gender <- factor(
  survey$gender,
  labels=c("Unanswered", "Male", "Female", "Other")
)

# Adds trait results from column vectors
survey$extroversion <- round(((survey$E1 + survey$E2 + survey$E3) / 15), digits=2)
survey$neuroticism <- round(((survey$N1 + survey$N2 + survey$N3) / 15), digits=2)
survey$agreeableness <- round(((survey$A1 + survey$A2 + survey$A3) / 15), digits=2)
survey$conscientiousness <- round(((survey$C1 + survey$C2 + survey$C3) / 15), digits=2)
survey$openness <- round(((survey$O1 + survey$O2 + survey$O3) / 15), digits=2)

# Save data frame into csv destination file
write.csv(survey, "analysis.csv")
# Alternatively
# write.table(survey, file="analysis.csv", sep=",")

# Clear environment
rm(list = ls())
