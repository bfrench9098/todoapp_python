import sys
import random
import math

tossCount = 0
targetTossCount = 0

###### START FUNCTIONS
def DoTosses(tossCount):
    myTosses=0
    headsCount = 0
    headsRatio = 0.00
    headsPercent = 0

    print(f"Performing {tossCount} tosses. Please wait ...")

    ### 1 = heads; 2 = tails
    while myTosses < tossCount:
        myTosses = myTosses + 1
        tossResult = random.randint(1,2)
        if tossResult == 1:
            headsCount = headsCount + 1
            headsRatio = headsCount / myTosses

    headPercent = (round_half_up(headsRatio, 4) * 100)

    print(f"\nOut of {tossCount} tosses")
    print(f"\tHeads was rolled {headsCount} times, or {headPercent}% of the tosses")
    tailsCount = (tossCount - headsCount)
    tailPercent = (100 - headPercent)
    print(f"\tTails was rolled {tailsCount} times, or {tailPercent}% of the tosses")

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier + 0.5) / multiplier
###### END FUNCTIONS
#-------------------------------------------------------------------------
#### START SCRIPT
promptNumberOfTosses='How Many Tosses Would You Like to Perform?(1 - 10,000)'
tosses=input(promptNumberOfTosses)

if (tosses.isnumeric()):
    targetTossCount = int(tosses)

    if (targetTossCount < 1) or (targetTossCount > 10000):
        print('You must enter a number between 1 and 10,000')
        sys.exit(1)
    else:
        DoTosses(targetTossCount)
else:
    print('You must enter a number between 1 and 10,000')
    sys.exit(1)
    