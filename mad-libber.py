# Malib Maker
# Author: Marcel Willis

# Print the title
print("Malib Maker\n")

# Retrieve inputs from user
noun = input("noun: ")
place = input("place: ")
pastTenseVerb = input("past tense verb: ")
adjective = input("adjective: ")

# Print the Mablib
print("\nThere once was a {0} that could be found in a {1}.".format(noun,place,pastTenseVerb,adjective))
print("The {0} typically {2} in the {1}.".format(noun,place,pastTenseVerb,adjective))
print("However, the {1} is now unfortnately {3}.".format(noun,place,pastTenseVerb,adjective))