# Fight Song
# Author: Marcel Willis

# Define the chorus
def chorus():
    print("Go, team, go!")
    print("Defeat your foe")
    
# Define the verse
def verse():
    print("Simply the best,")
    print("Better than the rest.")
    
# Define the Fight Song lyrics
def sing_fight_song():
    # 1st Stanza
    chorus()
    print(" ")
    # Loop for 2nd and 3rd Stanza
    for x in range(2):
        chorus()
        verse()
        chorus()
        print(" ")
    # 4th Stanza
    chorus()   

# Sing the Fight Song
sing_fight_song()