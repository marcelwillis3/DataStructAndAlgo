# Golf Helper
# Author: Marcel Willis

print("Welcome to the Golf Club Helper! \nTell me your situation, and I'll recommend a club\n")

greenHit = input("Did you hit it on the green (y/n)? ")
holeDistance = int(input("How far is the ball from the hole? "))
clubs = ['Putter','Driver','5-Iron','9-Iron','Pitching Wedge']

if greenHit.lower() == 'y':
    print("I recommend using your {0}".format(clubs[0]))
else:
    if holeDistance >= 200:
        print("I recommend using your {0}".format(clubs[1]))
    elif holeDistance >= 140:
        print("I recommend using your {0}".format(clubs[2]))
    elif holeDistance >= 100:
        print("I recommend using your {0}".format(clubs[3]))
    else:
        print("I recommend using your {0}".format(clubs[4]))