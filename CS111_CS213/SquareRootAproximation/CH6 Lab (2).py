"""
Created on Mar 29, 2012
Authors:
Jake Waffle, Mark Kelly
Created on:
4/11/12
Title of program:
Question5.py
Significant Constants:
Nones
User Input:
f the text file that will be checked to see if it's sorted.

                        Functions
Main:
The main fuction reads from a file to check if it has been sorted this is
checked by sorting the file and comparing it to the original data.

isSorted:
This function checks to see if two arguments are sorted least to greatest or not.
And it return the corresponding boolean value.

"""

'''def isSorted (List):
    #Builds a sorted list and compares to the original data
    List2=[]
    for elements in List:
        List2.append(elements)
        List.sort()
        condition = False
    if List == List2:
        condition = True

    return condition'''
def isSorted(A, B):
    ''''Checks to see if element A is less than B.'''
    if A < B:
        return True
    else:
        return False

def main():
    #Getting filename, opening the corresponding file, gathering its contents
    #and putting separated characters into a list.
    f=raw_input('Enter the text file you would like checked please: ')
    l=open(f,'r')
    conVert=l.read()
    List = conVert.split
    
    Sorted = False
    #Iterate through the list, but skipping an element each time
    for i in xrange(0,len(List)-1,2):
        #Update the sorted variable with a boolean value from a function that
        #checks if the selected adjacent elements are sorted.
        Sorted = isSorted(List[i],List[i+1])
        
main()

