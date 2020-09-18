# The Strange Case of the Deflated Cows
# Author: Marcel Willis

import sys
from random import *

class DeflatedCows:
    def __init__(self, evidence, health):
        self.evidence = evidence
        self.health = health

    def getEvidence(self):
        return self.evidence
    
    def setEvidence(self,evidence):
        self.evidence = evidence
    
    def getHealth(self):
        return self.health
    
    def setHealth(self,health):
        self.health = health

    def loseEvidence(self,lost):
        self.evidence = self.evidence - lost
        return self.evidence
        
    def gainEvidence(self,gain):
        self.evidence = self.evidence + gain
        return self.evidence

    def loseHealth(self,lost):
        self.health = self.health - lost
        return self.health
    
    def gainHealth(self,gain):
        self.health = self.health + gain
        return self.health        
    
    def printStats(self):
        print("Evidence Count = {0}     Health = {1}%".format(self.evidence,self.health))
        
    def confrontation(self,opponentHealth):
        while opponentHealth > 0 and self.health > 0:
            action = input("(t)ackle your opponent, (s)hoot your opponent, or (n)o action against your opponent: ")
            prob = random()
            if action.lower() == 't': # You attempt to tackle the opponent
                if prob >= 0.9: # You successfully tackle the opponent. 10% chance
                    opponentHealth = opponentHealth/2
                else: # You miss the opponent and the opponent counterattacks. 90% chance
                    self.health = self.health/2 - 10
                print("\nOpponent Health: {}%".format(opponentHealth))
                print("Your Health:     {}%".format(self.health))
            elif action.lower() == 's': # You attempt to shoot your opponent
                if prob >= 0.6: # You successfully shoot the opponent center-mass 40% chance
                    opponentHealth = 0
                else: # You miss center-mass and graze the opponent 60% chance
                    opponentHealth = opponentHealth - 20
                print("\nOpponent Health: {}%".format(opponentHealth))
                print("Your Health:     {}%".format(self.health))
            elif action.lower() == 'n': # You decide to take no action
                if prob >= 0.8: # Taking no action causes your opponent to take avantage and attack you. 20% chance
                    self.health = 0
                    print("\nYour opponent managed to kill you!\n")
                else: # Taking no action causes your opponent to walk away and avoid confrontation. 80% chance
                    opponentHealth = 0
                    print("\nYour opponent decided not to attack and vanished!\n")
                print("\nOpponent Health: {}%".format(opponentHealth))
                print("Your Health:     {}%".format(self.health))
            else:
                action = input("(t)ackle your opponent, (s)hoot your opponent, or (n)o action against your opponent: ")
        # Check to make sure the player is not dead.
        if self.health <= 0:
            print("You Died! Game Over!")
            sys.exit()
        
        return self.health
    

def main():
    # Start the user off with no evidence and 100% health
    dc = DeflatedCows(0,100)
    
    def manageStats(input1,input2): # Function to maintain the status of the player
        dc.setEvidence(input1)
        dc.setHealth(input2)
        dc.printStats()
    
    # Chapter 0: Introduce the user to the game
    print("Chapter 0\n\n Hello Special Agent Mux Folder, we have a new case for you.\n As the top agent of the X-Division of the FIB, I need you to investigate.")
    print(" We are getting reports from Eastern Oregon about mutilated cows.\n What makes this case stand out from the others you've may seen is that there appears to be no external wounds to the cows.")
    print(" Not a drop of blood is present and all organs are missing. The cow corpses strangly resemble deflated ballons.\n I need you to book a flight to Oregon and gather as much evidence as you can regarding this matter.")
    print(" Be very cautious, there are people in high places trying to bury the truth.\n")
    
    action = input("(s)top by your office first or (b)ook your flight: ")
    while action.lower() != 's' or action.lower() != 'b':
        if action.lower() == 's':
            print("\nYou stopped by your office to pick up the existing case file on mutilated animals.\n")
            evidence = dc.gainEvidence(1)
            break
        elif action.lower() == 'b':
            break
        else:
            action = input("(s)top by your office first or (b)ook your flight: ")
    
    input("\nPress Enter to book your flight: ")
    
    # Chapter 1: Flight to Oregon
    print("\nChapter 1: Flight to Oregon\n")
    evidence = dc.getEvidence()
    health = dc.getHealth()
    manageStats(evidence,health)
    
    print("\nOn your red-eye flight to Oregon, you notice a strange man in a black suit across the aisle that has been watching you since the airport in DC.\n")
    if evidence > 0:
        action = input("(i)gnore him and read the case file that you brought, or (a)sk the flight attendant to move you near the back of the plane: ")
    else:
        action = input("(c)onfront the man about watching you, or (a)sk the flight attendant to move you near the back of the plane: ")
    while action.lower() != 'i' or action.lower() != 'a':
        if action.lower() == 'i': # Ignore the strange man and read the case files.
            print("\nWithout you noticing, the strange man nabs your case file and walks to the rear bathroom!\n")
            action2 = input("(c)hase him down and retrieve the files or (n)otify the flight attendant: ")
            while action2.lower() != 'c' or action2.lower() != 'n':
                if action2.lower() == 'c': # You decide to chase the man but his accomplice attacks you from behind.
                    print("\nAs you chase the strange man, someone a few seats back sneakly sticks you with a needle and injects you with something and you pass out.\nWhen you finally awake, you realized the plane has landed in Oregon and the mysterious men and your case file is nowhere in sight\n")
                    evidence = dc.loseEvidence(1)
                    health = dc.loseHealth(20)
                    manageStats(evidence,health)
                    break
                elif action2.lower() == 'n': # You notify the FA but your materials are destroyed
                    print("\nYou notify the flight attendant that your materials were stolen. The flight attendant approach the restroom that the man entered.\nYou realize the man has flushed your files and vanished!\n")
                    evidence = dc.loseEvidence(1)
                    health = dc.getHealth()
                    manageStats(evidence,health)
                    break
                else:
                    if evidence > 0:
                        action = input("(i)gnore him and read the case file that you brought, or (a)sk the flight attendant to move you near the back of the plane: ")
                    else:
                        action = input("(c)onfront the man about watching you, or (a)sk the flight attendant to move you near the back of the plane: ")
            break
        elif action.lower() == 'a': # Move the back of the plane to avoid any potential threats
            print("\nYou are now alone in the back row. You review the case files covering cases of mutilated cows that were tracked to sacrificial rituals, different \noccults, and some mention of extraterrestrial activity.\n")
            dc.printStats()
            break
        elif action.lower() == 'c': # Confront the man about staring problem
            print("\nYour confrontation draws attention from other passengers. A man sneaks behind and injects you with a knockout drug. You awake now landed in Oregon.")
            health = dc.loseHealth(30)
            break
        else:
            if evidence > 0:
                action = input("(i)gnore him and read the case file that you brought, or (a)sk the flight attendant to move you near the back of the plane: ")
            else:
                action = input("(c)onfront the man about watching you, or (a)sk the flight attendant to move you near the back of the plane: ")
    
    input("\nPress Enter for next chapter: ")
        
    # Chapter 2: Investigating the Scene
    print("\nChapter 2: Investigating the Scene\n")
    evidence = dc.getEvidence()
    health = dc.getHealth()
    manageStats(evidence,health)
    
    print("\nYou reach the eerie scene in Eastern Oregon where the deceased cows look rather like a child took a needle to several cow-shaped ballons.\n")
    action = input("(a)pproach the lead investigator and gather information or (s)tudy a corpse: ")
    while action.lower() != 'a' or action.lower() != 's':
        if action.lower() == 'a': # Approach the investigator
            print("\nThe lead investigator notifies you that there are reports of a satanic cult in the area that are considered suspects.\n")
            evidence = dc.gainEvidence(1)
            health = dc.getHealth()
            manageStats(evidence,health)
            break
        elif action.lower() == 's': # Study the corpse
            print("\nYou approach the corpse and realize there are no puncture wounds on the body, no blood in sight, and there's a large impression in the ground as if \nthe body was dropped from a vertical distance.\nThe lead investigator also approaches you to introduce herself and present information regarding a local satanic cult.\n")
            evidence = dc.gainEvidence(3)
            health = dc.getHealth()
            manageStats(evidence,health)
            break
        else:
            action = input("(a)pproach the lead investigator and gather information or (s)tudy a corpse: ")
            
    input("\nPress Enter for next chapter: ")
            
    # Chapter 3: Talk the local Satanic Cult
    print("\nChapter 3: Investigating the Local Satanic Cult\n")
    evidence = dc.getEvidence()
    health = dc.getHealth()
    manageStats(evidence,health)
    
    print("\nYou approach a dark house in a secluded area and knock on the door. A man introduces himself as Silas, the dark lord's sheppard.\nSilas states that you are trespassing and that your blood must be spilt!\n")
    health = dc.confrontation(100) # Defend yourself against the cult leader's attack.
    print("\nYou've managed to defeat Silas the cult leader and found a document in the house detailing animal sacrifice procedures.\n")
    evidence = dc.gainEvidence(1)
    manageStats(evidence,health)
    
    input("Press Enter for next chapter: ")
    
    # Chapter 4: Drive Back to Town
    print("\nChapter 4: Drive Back to Town\n")
    evidence = dc.getEvidence()
    health = dc.getHealth()
    manageStats(evidence,health)
    
    print("\nAs you drive your rental back towards town, you see a bright blue light beam in the distance ahead. \nYou reach the area where the light beam is and notice that it's emitted from a Tic-Tac-shaped UFO.\n")
    action = input("(s)tep out and investigate or (t)urn around and leave the area without investigating: ")
    while action.lower() != 's' or action.lower() != 't':
        if action.lower() == 's':
            print("\nYou step out of the car to investigate, a Grey Skin teleports from the UFO and stands 10 feet away from you!\n")
            health = dc.confrontation(100) # Determine what to do against the alien
            print("\nThe alien's corpse vanishes and the UFO launches into the night sky with no sound. You investigate the area where the craft hovered and find another animal carass depleted of it's insides!\n")
            evidence = dc.gainEvidence(5)
            break
        elif action.lower() == 't':
            print("\nYou turn around and peel out as you watch the UFO in your rear-view mirror shoot off vertically into the sky with no sound.\n")
            break
        else:
            action = input("(s)tep out and investigate or (t)urn around and leave the area without investigating: ")
            break
    
    manageStats(evidence,health)
    input("\nPress Enter for next chapter: ")
    
    # Chapter 5: Talk to the Locals at the Bar
    print("\nChapter 5: Talk to the Locals at the Bar\n")
    evidence = dc.getEvidence()
    health = dc.getHealth()
    manageStats(evidence,health)
    
    print("\nYou have a seat at the end of the bar. The bartender says you look new in town and offers a menu full of drinks and food.\n")
    action = input("(d)rink only or a (f)ull course meal, drink included. 'Of course, the FIB is paying for it': ")
    while action.lower() != 'd' or action.lower() != 'f':
        if action.lower() == 'd':
            health = dc.gainHealth(20)
            break
        elif action.lower() == 'f':
            dc.setHealth(100)
            health = dc.getHealth()
            break
        else:
            action = input("(d)rink only or a (f)ull course meal, drink included 'Of course, the FIB is paying for it': ")
            
    print("\nWhile enjoying your drink/meal, you overhear the locals talk about what they think is happening to the livestock around the area. \nTheories of aliens, government experiments, the Russians or Chinese, and Bigfoot are all thrown out there. \nHowever, one local knows you are FIB and provides you with files describing a government developed war chemical;\nWhen consumed will dissolve anything at temperatures above 95deg F!\n")
    evidence = dc.gainEvidence(1)
    manageStats(evidence,health)
    
    input("\nPress Enter for next chapter: ")
    
    # Chapter 6: Investigating a New Scene
    print("\nChapter 6: Investigating a New Scene\n")
    evidence = dc.getEvidence()
    health = dc.getHealth()
    manageStats(evidence,health)
    
    print("\nThe next day you get a call from the local sheriff, she has a new scene for you to help investigate.\n15 miles away from the first scene.\n")
    action = input("(l)ook for footprints around the scene or (s)tudy the carcass closely: ")
    while action.lower() != 'l' or action.lower() != 's':
        if action.lower() == 'l':
            print("\nYou were unable to find any footprints or tire treads in and around the scene.")
            break
        elif action.lower() == 's':
            print("\nUnlike the last scene, you find foam at the mouth as if the cow was poisoned.\nThis bring memories of the files you just received at the bar last night.\n")
            evidence = dc.gainEvidence(1)
            break
        else:
            action = input("(l)ook for footprints around the scene or (s)tudy the carcass closely: ")
            
    print("\nAfter investigating the scene, you notice the same man in black from your flight the night before watching you in a car down the road.\nHe notices your attention and drives off!\n")
    evidence = dc.getEvidence()
    health = dc.getHealth()
    manageStats(evidence,health)
    
    input("\nPress Enter for next chapter: ")
    
    # Chapter 7: Meet the Man in Black
    print("\nChapter 7: Meet the Man in Black\n")
    evidence = dc.getEvidence()
    health = dc.getHealth()
    manageStats(evidence,health)
    
    print("\nYou managed to chase down the man in black and ask 'Who are you!? And why are you following me!?'\nThe man responds in deep monotone 'I am Agent I, you are meddling in matters of my concern and you must be destroyed!\n")
    health = dc.confrontation(150) # Defend yourself against the man in black
    print("\nYou approach the body and realize how eerie it looks up close. No eyebrows, eyelashes, or visible fingerprints.\nYou find a business card inside his jacket with only the letter 'I' stamped on it.\n")
    evidence = dc.gainEvidence(1)
    manageStats(evidence,health)
    
    input("\nPress Enter for next chapter: ")
    
    # Chapter 8: Travel Back to HQ with Evidence and Present Findings
    print("\nChapter 8: Travel Back to HQ with Evidence and Present Findings\n")
    evidence = dc.getEvidence()
    health = dc.getHealth()
    manageStats(evidence,health)
    
    print("\nYour plane lands in DC and you take a BuBer back to HQ. The BuBer drops you off a couple of blocks down at a coffee cafe.\nShortly after you see Agent I standing in an alleyway! Construction forces you to walk directly towards him!\n'I thought I killed you!?' 'I am Agent Q, you are meddling in matters of my concern and you must be destroyed!\n")
    health = dc.confrontation(150) # Defend yourself against the man in black
    print("\nEerily Agent Q looks exactly like Agent I. Same height, facial features, and complexion. No eyebrows, eyelashes, or visible fingerprints.\nYou find a business card inside his jacket with only the letter 'Q' stamped on it.\n")
    evidence = dc.gainEvidence(1)
    manageStats(evidence,health)
    
    if evidence >= 7:
        print("\nYou convinced leadership at the FIB that something strange is going on and you presented enough evidence \nto start a few Task Force groups to investigate further.")
    elif evidence >= 1:
        print("\nLeadership at the FIB is not quite convinced to move forward on anymore investigations. They are disappointed in your work.")
    else:
        print("\nYou've completely wasted leadership's time and the taxpayers' money. You are demoted to paper-shredder specialist.")
    
    
    
main()