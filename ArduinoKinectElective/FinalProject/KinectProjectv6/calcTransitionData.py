"""
This file is part of the "Theme Song Generation," Kinect Project for CS 312.

The "Theme Song Generation," Kinect Project is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

The "Theme Song Generation," Kinect Project is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""


"""
A quick note:

This program takes in a txt file of numbers that actually represent stuff.
The outputted data needs to be with respect to the key. And since I can't
easily determine how to make the program do that based off of string data ("A B C"),
the note data will be in the form of 0-21, where 1, 8 and 15 are the keyNotes (they represent the key.)
The outputted data is like this so that the actual program can easily change the key of the song.

Important-The reason that the keyNotes are 1, 8 and 15 is because the song data only takes into account
the notes on the scale that the song uses (which could be any scale, except a diminished I believe.)
A common characteristic that scales have are that they contain 7 notes. So with this, I was able
to instead of using all 13 notes in an octave, only allow the 7 notes to be used. This won't affect
the music, because a lot of songs usually don't diverge from the scale and key that they are using.
And those are the types of songs that I tried to use with the Kinect Project.
"""

#This will load and return a list of the data 
#  that is to beparsed. 
#@param fileName A string that represents
#  a filename, this file will be where
#  our song data comes from (those files
#  must be written manually though.)
def getSong(fileName):
    f = open(fileName, 'r')
    contents = f.read()
    contentList = contents.split()
    return contentList

#This will parse a list of notes (values 0-21) and return
#  a list of lists containing data on the transition between notes.
#  Where the first level of the list of lists represents the previous notes
#  and the second level represents the next notes, the positions
#  in the list of lists in the end will represent the probability of transitioning
#  from the previous note to the next note.
#@param notes This is a list containing the actual notes in a song.
#  (The notes are represented with the values 0-21, 0 represents a rest.)
#@return An list of lists that contains the data that we want to put into
#  the Kinect Program.
def calcTransitionData(notes):
    data = []

    numNotes = raw_input("How many possible notes are there \n(22 was decided for the pitches, 9 for the durations:) ")

    numNotes = int(numNotes)
    
    #22 notes are possible for the Markov data
    #And the list of list data needs to be 22 by 22
    for i in xrange(numNotes):
        data.append([])
        for j in xrange(numNotes):
            data[i].append(0.)

    #Presumes the song starts after a rest
    prevNote = 0

    #Iterate through notes and add transitions to the
    #   data
    for i in xrange(len(notes)):
        data[prevNote][int(notes[i])] += 1.

        prevNote = int(notes[i])

    #Iterates over prevNotes
    for i in xrange(numNotes):
        total = 0
        #Iterates to find total number of transitions
        #   from the current prevNote
        for j in xrange(numNotes):
            total += data[i][j]

        #Iterate to change number of note transitions
        #   to the probability of note transition.
        for j in xrange(numNotes):
            if (total != 0):
                data[i][j] /= total

    return data

#This function basically will save the data that
#  is needed for the Kinect Program's ArrayList of
#  ArrayLists. And the format that the data is saved
#  in will be able to be copy-pasted into the Kinect
#  Program.
#@param data This is a list of lists containing
#  the data that is needed for the Kinect program.
def saveSongData(data):
    output = "{ "
    
    for i in xrange(len(data)):
        if (i != 0):
            output += "  {"
        else:
            output += "{"

        for j in xrange(len(data[0])):
            output += str(data[i][j])

            if (j != (len(data[0])-1)):
                output += ", "

        if (i != (len(data)-1)):
            output += "},\n"
        else:
            output += "}"

    output += " };"

    fileName = raw_input("Enter a file name: ")

    f = open(fileName, "w")
    f.write(output)
    f.close()

def main():
    fileName = raw_input("Enter a file name for your song data: ")

    notes = getSong(fileName)

    transitionData = calcTransitionData(notes)

    saveSongData(transitionData)

main()
