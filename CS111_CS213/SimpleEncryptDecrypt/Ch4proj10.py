'''
Program: Ch4 Project 10
Authors: Jake Waffle, Greg Mcatee and BreAnne Baird

Display file contents in tabular form
1. Constants
    WORD_PER_ROW
2. Input
    filename
3. Computations
    Display the header for the information.
    Iterate through each row of the file's contents and display the corresponding words in tabular form.
4. Display
    A header for the data
    The data for each person distributed among rows that are displayed in tabular form and conforming to the header's format.
'''
#Constants
WORD_PER_ROW = 3

#INPUT
filename = raw_input("Enter the filename for the file that contains your past work statistics: ")

#Open and read the specified file
f = open(filename, 'r+')
contents = f.read()

#Setup the header
line = "-------------------------------------------------------------------\n"
format = "%-14s%-14s%-14s%-10s"
header = format % ("Last Name" ,"Hourly Wage", "Hours Worked", "Earnings")
print line
print header

#Split the contents up so we can deal with them separately
wordList = contents.split()

#Initialize variables
earnings = 0
row = ""
#Calculating the amount of rows
rows = len(wordList) / WORD_PER_ROW
#For loop to iterate through each row in rows
for i in xrange(0,rows):
    #Compute earnings with string numbers from the file
    earnings += float(wordList[(i*3)+1])
    earnings *= float(wordList[(i*3)+2])
    earnings = str(earnings)
    
    #Setup the format for one row and print
    row = format % (wordList[(i*3)], wordList[(i*3)+1], wordList[(i*3)+2], earnings)
    print row
    
    #Reset variables
    row = ""
    earnings = 0
    
