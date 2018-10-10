"""
program: Chapter 16 project 7
author: Jake Waffle

1. Constants
    None
2. Inputs
    fileName - This is the file name for the file that we'll be reformatting

    lineWidth - This attribute will be what the reformatting is based off of
    
3. Computations
    wrapAround(fileName, lineWidth) - This function will grab the text from the fileName that is given, reformat the text using lineWidth
        and then the text will be saved to a new file under the name "reformatted"+fileName.

4. Outputs
    There are three prompts: there's one for the fileName, another for the lineWidth and the last sees if the user would like to quit or continue

    And the other output is the reformatted text file that is created/overwritten.
"""

def wrapAround(fileName, lineWidth):
    """This function will open up a text file and reformat it to match the lineWidth.
    Then it will save the file."""
    failedFlag = False
    try:
        f = open(fileName, 'r')
    except:
        failedFlag = True

    if not failedFlag:
        reformattedLines = []
        overflowWords = []
        #This iterates through the lines of the file
        for line in f:
            reformattedLines.append([])
            words = line.split()
            currentWidth = 0
            wordBuffer = []      #This will prevent our infinite loop in the next for loop

            #Here we will be adding words that overflowed to the current line
            for i in xrange(len(overflowWords)):
                #If the current line won't be filled up by the current word
                if currentWidth + len(overflowWords[0]) <  lineWidth:
                    currentWidth += len(overflowWords[0])+1     #The one represents a space after the word
                    reformattedLines[-1].append(overflowWords.pop(0))
                else:
                    #If this was the first item to be added to the line
                    if i == 0:
                        #Add it anyway
                        currentWidth += len(overflowWords[0])+1     #The one represents a space after the word
                        reformattedLines[-1].append(overflowWords.pop(0))
                        
                    #Words after this word may be able to fit in the line
                    break
                
            complete = False
            #Then we will be adding words from the current line
            for j in xrange(len(words)):
                #If the current line won't be filled up by the current word
                if currentWidth + len(words[0]) <  lineWidth and not complete:
                    currentWidth += len(words[0])+1     #The one represents a space after the word
                    reformattedLines[-1].append(words.pop(0))
                    
                else:
                    overflowWords.append(words.pop(0))
                    complete = True

        reformattedLines.append([])
        currentWidth = 0

        complete = False
        #Here we will account for the words that have been overflowed
        while not complete:
            if len(overflowWords) == 0:
                complete = True
                
            #If the current line won't be filled up by the current word
            elif currentWidth + len(overflowWords[0]) <  lineWidth:
                currentWidth += len(overflowWords[0])+1         #The one represents a space after the word
                reformattedLines[-1].append(overflowWords.pop(0))

            #Transition to the next line down
            else:
                #If this was the first item to be added to the line
                if currentWidth == 0:
                    #Add it anyway
                    currentWidth += len(overflowWords[0])+1         #The one represents a space after the word
                    reformattedLines[-1].append(overflowWords.pop(0))
                else:
                    reformattedLines.append([])
                    currentWidth = 0

        failedFlag = False
        try:
            f = open("reformatted"+fileName,'w')
        except Exception:
            failedFlag = True

        if not failedFlag:
            reformattedText = ""
            #Reconstruct our list of reformatted lines so that it is in a string representation.
            for line in reformattedLines:
                #Each line also contains a list of words
                for word in line:
                    #Each word is added along with a space
                    reformattedText += word + " "
                reformattedText.strip()     #This gets rid of our extra space at the end of the line
                reformattedText += "\n"     #This will move represent the line transition within the text

            f.write(reformattedText)

def main():
    finished = False
    while not finished:
        fileName = raw_input("\nEnter the name of the file name that you'd like to reformat: ")
        lineWidth = raw_input("\nEnter the line width that you'd like to set for the reformatted file: ")

        #Check to see if we like the input that was given
        if lineWidth.isdigit() and int(lineWidth) > 0 and int(lineWidth) < 100:
            #I approve of this input
            wrapAround(fileName, int(lineWidth))

        decision = raw_input("\nEnter something to continue: ")
        if decision == "":
            finished = True


main()
