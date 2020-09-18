# Total Service Score Calculator
# Author: Marcel Willis

# Initialize the score value
totalscore = 0

# Prompt user to input number of days
days = eval(input("How many days of scores? "))

# Loop through days to allow user to input score
for i in range(1,days+1):
    score = eval(input("Enter score for day " +str(i) +": "))
    totalscore = totalscore + score

# Return the total score to the user for review
print("The total score of the " +str(days) +" days is " +str(totalscore))