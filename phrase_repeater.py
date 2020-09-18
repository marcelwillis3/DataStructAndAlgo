# Phrase Repeater
# Author: Marcel Willis

# Request user input for their phrase
phrase = input("Input your phrase: ")

# Request user input for the number of repeats
repeater = eval(input("How many times should it be repeated? "))

# Print the phrase for the number of times requested
for index in range(repeater):
    print(str(index+1) + (" ") + phrase)