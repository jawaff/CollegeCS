'''

Author: Mark Kelly, Jake Waffle
Program: Project 9 of chapter 6

Compute and display the average of numbers within a text file.
1.Significant Constants
    No constants... EVER
2.Input
    filename
    decision
3.Computations
    computing the average of numbers in a list
4.Displays
    The average of numbers!!!!

'''
def getContents(filename):
    '''Given a filename, this takes the contents from the file and puts it into a list using split().'''
    f = open(filename, 'r')
    contents = f.read()
    numList = contents.split()
    return numList

def findAverage(numList):
    '''Given a list of numbers, this finds and returns the average'''
    summ = 0.0
    count = 0
    for i in numList:
        summ += float(i)
        count += 1
    average = summ / count
    return average

def main():
    '''Main function, it prompts the user if it wants to find the average of numbers on files
    and Displays the result after getting input.'''
    done = False
    #Main loop
    while done == False:
        filename = raw_input("Please enter a filename that contains numbers that you would like the average of: ")
        contents = getContents(filename)
        average = findAverage(contents)
        print "\n"
        print "The average of the numbers in the file you specified is", 
        print "\n"
        decision = raw_input("Would you like to find the average of numbers in another file(y or n?) ")
        answer = False        
        while answer == False:
            if (decision == 'n'):
                answer = True
                done = True
            elif (decision == 'y'):
                answer = True
            else:
                print "\n"
                decision = raw_input("Please enter either a y or n!")
                print "\n"
                
main()
