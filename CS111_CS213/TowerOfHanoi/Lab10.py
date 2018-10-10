"""
Program:
Authors: Jake Waffle, Katy Phipps, Mark Kelly

1. Constants
    None

2. Inputs
    -numberOfRings    -    Denotes the number of rings for the game
    -startPeg         -    An integer denoting the list for the starting peg
    -sparePeg         -    An integer denoting the list for the spare peg
    -finishPeg        -    An integer denoting the list for the finishing peg

3. Computations

4. Outputs

"""

peg1 = None
peg2 = None
peg3 = None

def moveRing(fromCone, toCone):
    global peg1, peg2, peg3
    ring = None

    if fromCone == 1:
        ring = peg1.pop()
    elif fromCone == 2:
        ring = peg2.pop()
    else:
        ring = peg3.pop()

    if toCone == 1:
        peg1.append(ring)
    elif toCone == 2:
        peg2.append(ring)
    else:
        peg3.append(ring)
    

def towers(howMany, source, spare, target):
    if howMany == 1:
        moveRing(source, target)
    else:
        towers(howMany-1, source, target, spare)
        moveRing(source, target)
        towers(howMany-1, spare, source, target)

def main():
    global peg1, peg2, peg3
    
    finished = False
    while not finished:
        numberOfRings = raw_input("\nEnter some odd number of rings: ")

        if not numberOfRings.isdigit():
            print "\nIncorrect input!"
            continue

        numberOfRings = int(numberOfRings)
        
        peg1 = []
        peg2 = []
        peg3 = []

        startPeg = raw_input("\nEnter the peg number for the starting peg: ")
        sparePeg = raw_input("\nEnter the peg number for the spare peg: ")
        finishPeg = raw_input("\nEnter the peg number for the finishing peg: ")
        
        if startPeg.isdigit() and sparePeg.isdigit() and finishPeg.isdigit()    \
                and int(startPeg) >= 1 and int(startPeg) <= 3    \
                and int(sparePeg) >= 1 and int(sparePeg) <= 3    \
                and int(finishPeg) >= 1 and int(finishPeg) <= 3:
    
            peg = None
            if startPeg == 1:
                peg = peg1
            elif startPeg == 2:
                peg = peg2
            elif startPeg == 3:
                peg = peg3
                
            #Add rings to our stack
            for ringNum in xrange(numberOfRings, 0, -1):
                peg.append(ringNum)
                
            towers(numberOfRings, int(startPeg), int(sparePeg), int(finishPeg))
    
            print peg1
            print peg2
            print peg3
    
            quitting = raw_input("\nEnter something to continue: ")
            if quitting == "":
                finished = True


main()
