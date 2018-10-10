"""
author: Jake Waffle
program: Proj_8-11_testModule.py


"""

from linkedStructures import *

head = None
TwoWay = False      #Tells whether or not the head variable is a TwoWay or OneWay list

ACTIONS = ("\n1. Create a singly linked list (overwrites old list)",  \
           "2. Insert into the current list",   \
           "3. Remove from the current list",   \
           "4. Convert singly linked list list to doubly linked list",  \
           "5. Print information about the current linked list")
        
def doAction(action):
    """This executes the action that the user chose."""
    global head, TwoWay
    
    if action == 1:
        #Create a singly linked list
        number = raw_input("\nEnter the amount of items you'd like in your list: ")
        default = raw_input("\nEnter the default value of the items: ")

        if number.isdigit() and int(number) > 0 and int(number) < 50 and default != "":
            head =  buildLinkedList(int(number), default)

        else:
            print "\nGive me proper input you dingus!"
            
    elif action == 2:
        #Insert into the list
        index = raw_input("\nEnter the index you'd like to insert at: ")
        item = raw_input("\nEnter the item you'd like to place inside the list: ")

        if index.isdigit() and int(index) > 0 and int(index) < length(head) and item != "":
            head = insert(item, int(index), head, TwoWay)

        else:
            print "\nGive me proper input you dingus!"
            
    elif action == 3:
        #Remove from the list
        index = raw_input("\nEnter the index you'd like to insert at: ")

        if index.isdigit() and int(index) > 0 and int(index) < length(head):
            (lyst, removedItem) = remove(int(index), head, TwoWay)
            head = lyst
            
            print "\n" + removedItem, "has been removed from your list!"

        else:
            print "\nGive me proper input you dingus!"
            
    elif action == 4:
        #Convert from singly to doubly linked list!
        (one, two) = makeTwoWay(head, TwoWay)
        head = one

        if TwoWay == False and two == True:
            TwoWay = two
            print "\nYour list has been converted to a doubly linked list!"
        elif TwoWay:
            print "\nYour list is already doubly linked you dingus!"
        else:
            print "\nSomething went wrong!"
        
    elif action == 5:
        #Prints information on the head variable
        print "\nHere's the contents of the list:"
        printList(head)

        if TwoWay:
            print "\nYour list is doubly linked!"
        else:
            print "\nYour list is singly linked"
        

def main():
    global ACTIONS
    
    finished = False
    while not finished:
        #Displays the user's options
        for i in ACTIONS:
            print i

        #Get the user's intended action
        decision = raw_input("\nEnter a number that is next to your intended action from the list above: ")

        #Filter that input!
        if decision.isdigit() and int(decision) > 0 and int(decision) <= 5:
            doAction(int(decision))
     
main()
