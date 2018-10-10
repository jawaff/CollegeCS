"""
Program: Library.py
Authors: Evan Randall and Jacob Waffle

1. Significant Constants:
    -Manager._options    #That's a tuple for the options available for the user.

2. Inputs:
    -answer              #This denotes the decision the user has chosen to do.
    -title               #This denotes a book's title.
    -author              #This denotes a book's author.
    -name                #This denotes a patron's name.

3. Computations:
    -All inputs are filtered to eschew errors.
    -Searching through dictionaries for already existing elements was used multiple times.
    -Adding/removing elements from a dictionary
    -When a book is checked-out/-in, patron._numBooks is changed accordingly

4. Outputs:
    -The options for the user's actions are outputted so that the user knows what it can do at the start of each loop.
    -Whenever something is successfully completed, a message is outputted to let the user know what's going on.
    -Whenever incorrect input is given, this outputs a message saying that the input is wrong.
    -A list of books is displayed after the user chooses to select a book.
    -A list of patrons is displayed after the user chooses to select a patron.
    -And finally, there is a "Have a nice day!" message upon choosing to exit the program
    

"""




def getString(prompt):
    """This is for universalized input and filtering."""
    finished = False
    string = ""
    while not finished:
        string = raw_input(prompt)
        if string.isdigit():
            print "\nPlease retry your entry."
        else:
            finished = True

    return string
        

class Book(object):
    """A class meant to represent a book."""
    def __init__(self,title,author):
        """Constructing a book instance and initializing instance variables needed."""
        self._title = title
        self._author = author
        #patron represents the patron that has checked this book out
        self._patron = ""         #Start out with None, because it isn't checked out
        self._waitList = []
    
    def __str__(self):
        """This defines how we want to display our books to the user as a string"""
        return "\n" + "Title: " + self._title + "\n" \
            + "Author: " + self._author      
        
    def getTitle(self):
        """Returns the title of the book object."""
        return self._title
        
    def checkOut(self, patron):
        """This is for checking books out of the library and if it's already checked out, add the patron to the waitList."""
        #Check to see if the book is checked out
        if self._patron != "":
            if patron._numBooks < 3:    
                self._waitList.append(patron._name)
                #This is the first line to be printed following the
                #users decision to checkOut a book, so NEWLINE!
                print "\nPatron:", patron._name, "has been added to", \
                      self._title + "\'s waitlist!"
            else:
                #NEWLINE, same reason as above
                print "\nPatron:", patron._name, "already has three books checked out, sorry."
        else:
            if patron._numBooks < 3: 
                self._patron = patron._name
                print "\nPatron:", patron._name, "has successfully checked out Book:", self._title
                patron.bookCheckOut()
            else:
                print "\nPatron:", patron._name, "already has three books checked out, sorry."
                
    def checkIn(self, patron):
        """This is for checking books into the library and returning the next patron on the waitList."""
        if patron._name == self._patron:
            self._patron = ""
            print "\nPatron:", patron._name, "has successfully checked in Book:", self._title
            patron.bookCheckIn()
            if len(self._waitList) > 0:
                return self._waitList[0]
            else:
                return ""
        
        else:
            print self._title, "is not currently checked out by Patron:", patron._name
            return ""

class Patron(object):
    """A class meant to represent a patron."""
    def __init__(self,name):
        """The contstructor that initializes instance variables and returns an instance of the new object"""
        self._numBooks = 0
        self._name = name
    
    def getName(self):
        """This returns the name of the patron"""
        return self._name
        
    def __str__(self):
        """This defines how we want the patron to be displayed as a string to the user."""
        return "\n" + "Name: " + self._name + "\n" \
            + "Number of books: " + str(self._numBooks)
    
    def bookCheckOut(self):
        """This method's purpose is to increment the amount of books currently checked out by
        the patron."""
        self._numBooks += 1
        print "Patron:", self._name, "now has", self._numBooks, "book(s) checked out!\n"

    def bookCheckIn(self):
        """Alike bookCheckOut(), this method decrements the amount of books currently checked out
        by the patron."""
        self._numBooks -= 1
        print "Patron:", self._name, "now has", self._numBooks, "book(s) checked out!\n"

    def compareNames(name1, name2):
        """This allows us to check if two patron's names are equivalent or not."""
        if name1 == name2:
            return True
        else:
            return False
        

class Library(object):
    """A class that represents a library of books and patrons involved."""
    def __init__(self):
        """The contructor for initializing and loading of
        various tidbits that will be needed."""
        self._patrons = {}
        self._books = {}
        self.loadExistingBooks()

    def loadExistingBooks(self):
        """Load all the books, so I don't have to input them anymore!"""
        self._patrons["Apples"] = Patron("Apples")
        self._patrons["Jaleh"] = Patron("Jaleh")
    
        self._books["Magnanimous Man"] = Book("Magnanimous Man", "Magna Marsh")
        self._books["My Barbequed Cat"] = Book("My Barbequed Cat", "John Smith")
        self._books["My Apples and I"] =  Book("My Apples and I", "John Gnash")
        self._books["Pistol Shrimp: A Working Biography"] = Book("Pistol Shrimp: A Working Biography", "Patrick Star")
        self._books["The Necronomicon"] = Book("The Necronomicon", "Abdul Alhazred")
        self._books["Harangue: A Way of War"] = Book("Harangue: A Way of War", "durrrrr")

    def addBook(self, title, author):
        """Initializing a book instance and putting it into the list of books."""
        #Check to see if the book already exists or not
        tmpObject = self._books.get(title,None) 
        if tmpObject != None:
            print "Already existent in the Library!\n"
            
        else:
            self._books[title] = Book(title,author)
            print title, "has successfully been added into the Library!\n"
        
    def removeBook(self, title):
        """Removes a particular book from the dictionary."""
        book = self._books.pop(title, None)
        if book == None:
            print "That book does not exist in the Library currently!\n"
        else:
            print title, "has been removed from the Library, by force!\n"
    
    def findBook(self):
        """Returns the corresponding book object."""
        tmpObject = None
        finished = False
        while not finished:
            #This lets the user know what inputs are possible
            print "\nHere is a list of our books:\n"
            for bookObj in self._books.values():
                print bookObj
                
            title = getString("\nEnter the book's title: ")
            #Check to see if the book exists
            tmpObject = self._books.get(title, None)
            if  tmpObject != None:
                print "Book:", title, "is currently selected and ready to check-out/-in!\n"
                finished = True
            else:
                print "Book:", title, "isn't listed in our database, sorry.\n"
        return tmpObject

    def addPatron(self, name):
        """Initializes a patron instance and puts it into the dictionary.
        And it may overwrite patrons with the same name."""
        #Check to see if the patron already exists or not
        tmpObject = self._patrons.get(name, None)
        if tmpObject != None:
            print "This patron already exists!\n"
        else:
            self._patrons[name] = Patron(name)
            print name, "has successfully been added into the Library\n"

    def removePatron(self, name):
        """Removes a particular patron from the patron's list."""
        patron = self._patrons.pop(name, None)
        if patron == None:
            print "That patron does not exist in the Library currently!\n"
        else:
            print name, "has been removed from the Library, by force!\n"

    def findPatron(self):
        """Returns the corresponding patron object."""
        tmpObject = None
        finished = False
        while not finished:
            #This lets the user know what inputs are possible
            print "\nHere is a list of our patrons:\n"
            for patronObj in self._patrons.values():
                print patronObj
                
            name = getString("\nEnter the patron's name: ")
            #Check to see if the patron exists
            tmpObject = self._patrons.get(name, None)
            if  tmpObject != None:
                print "Patron:", name, "is now selected and ready to check-out/-in books!\n"
                finished = True
            else:
                print "Patron:", name, "was not found in our database, sorry.\n"
        return tmpObject
                
class Manager(object):
    """This class is meant for taking the users input and
    doing the according action!"""
    def __init__(self):
        """Initialize anything and everything"""
        self._options = ("AddBook", "AddPatron", "SelectBook", "SelectPatron", "CheckOut", "CheckIn", "Exit")
        #Instance of the Library class
        self._library = Library()
        #Variables for the select d patron/book(their types are objects)
        self._currentBook = None
        self._currentPatron = None
        
    def __str__(self):
        """Print all the options available to the user"""
        tempVar = ""
        for i in xrange(len(self._options)):
            tempVar += str(i+1) + " " + self._options[i] + "\n"
            
        return tempVar

    def getAnswer(self):
        """This takes in input from the user for the action that is
        to be done next."""
        gewd = False
        #I will loop until the user cooperates!
        while not gewd:
            decision = raw_input("Choose a number corresponding with the option wanted from the above list: ")
            #Filtering input all the time
            if decision.isalpha() or int(decision) < 1 or int(decision) > 7:
                print "Incorrect input!!!!!!\n"  
            else:    
                gewd = True
                
        return decision
    
    def doAction(self, decision):
        """This executes the action that the user has given us."""
        if decision == "1":
            #AddBook!
            title = getString("\nEnter the book's title: ")
            author = getString("Enter the book's author: ")
            self._library.addBook(title , author)
            return False
            
        elif decision == "2":
            #AddPatron
            name = getString("\nEnter the patron's name: ")
            self._library.addPatron(name)
            return False

        elif decision == "3":
            #SelectBook
            self._currentBook = self._library.findBook()
            return False
            
        elif decision == "4":
            #SelectPatron
            self._currentPatron = self._library.findPatron()
            return False

        elif decision == "5":
            #CheckOut
            #Check to see if a book and patron are selected
            if self._currentBook != None and self._currentPatron != None:       
                self._currentBook.checkOut(self._currentPatron)
            elif self._currentBook == None and self._currentPatron != None:
                print "\nI\'m sorry to say that there is not a book currently selected. Go select one and try again!\n"
            elif self._currentBook != None and self._currentPatron == None:
                print "\nI\'m sorry to say that there is not a patron currently selected. Go select one and try again!\n"
            else:
                print "\nThere needs to be a book and patron selected before this is possible!\n"
                
            return False
        
        elif decision == "6":
            #CheckIn
            #Check to see if a book and patron are selected            
            if self._currentBook != None and self._currentPatron != None:
                #Where nextPerson is a string containing the name of the next person on the waitList
                nextPerson = self._currentBook.checkIn(self._currentPatron)
                #Check to see if a patron on the book's waitList was returned
                if nextPerson != "":
                    self._currentBook.checkOut(self._library.findPatron(nextPerson))
                    print "\n" + self._currentBook.getTitle() + "has been checked out to" + nextPerson  + "\n"
            elif self._currentBook == None and self._currentPatron != None:
                print "\nI\'m sorry to say that there is not a book currently selected. Go select one and try again!\n"
            elif self._currentBook != None and self._currentPatron == None:
                print "\nI\'m sorry to say that there is not a patron currently selected. Go select one and try again!\n"
            else:
                print "\nThere needs to be a book and patron selected before this is possible!\n"
            
            return False
        
        elif decision == "7":
            print "Have a nice day!"
            return True
        
def main():
    """The main function, mostly just contains the main loop."""
    menu = Manager()
    gewd = False
    
    #I will loop until the user is satisfied and has exited!
    while not gewd:
        print "\n"  #This actually creates two newlines, tmyk
        print menu
        
        #Asks the user what it'd like to do.
        answer = menu.getAnswer()   
        #Do an action, given the users input and see if the program
        #is done.
        if (menu.doAction(answer)):
            #If the program is finished, signal the loop to stop
            gewd = True
            
        #This gives the user time to read what's going on
        #before the menu is printed again.
        raw_input("Press enter to continue!")
main()
