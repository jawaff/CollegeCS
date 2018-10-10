"""
author: Jake Waffle
program: LinkedStructure.py

Constants
    No constants here

Inputs
    Not doing any inputs in this file

Computations
    makeTwoWay(linkedList, TwoWay)              -This loops through a singly linked list and copies its contents into a newly created doubly
                                                linked list.

    buildLinkedList(items, defaultDatum)        -This loops for items iterations and creates a singly linked list while doing the looping.
    
    length(linkedList)                          -This loops throught the linked structure counting the elements and returns the count.

    insert(newItem, index, linkedList, TwoWay)  -This loops through the linkedList to find the index, then it inserts an element
                                                and rebuilds the list so that it can return the head variable of the list.

    remove(index, linkedList, TwoWay)           -This loops through the linkedList to find the index, then it removes the element
                                                and rebuilds the list so that it can return the head variable of the list.

Outputs
    There are no outputs here!
"""

class Node(object):
    def __init__(self, data, next = None):
        # Instantiates a Node with default next of none
        self.data = data
        self.next = next


class TwoWayNode(Node):
    def __init__(self, data, previous = None, next = None):
        # Instantiates a TwoWayNode.
        Node.__init__(self,data,next)
        self.previous = previous

def makeTwoWay(linkedList, TwoWay):
    """From a singly linked list, this converts it into a doubly linked list."""
    #Check to see if the list isn't already doubly linked
    if TwoWay == False:
        elements = []
        
        #Setup the head
        elements.append(TwoWayNode(linkedList.data, None, linkedList.next))
        linkedList = linkedList.next
        
        #Creating a TwoWayNode for every oneWayNode
        while linkedList != None:
            elements.insert(0, TwoWayNode(linkedList.data, elements[0], linkedList.next))
            linkedList = linkedList.next

        #Placing the tail for the doubly linked list
        linkedList = elements[0]

        #looping until linkedList is the head variable.
        while linkedList.previous != None:
            linkedList = linkedList.previous

        #Returns the doubly linked list
        return (linkedList, True)
    
    else:
        #Returns the original list
        return (linkedList, False)

def buildLinkedList(items, defaultDatum):
    """This builds a linked list with the given number of items and defaultDatum value and returns the head value of it."""
    linkedList = None

    for i in xrange(items):
        linkedList = Node(defaultDatum, linkedList)

    return linkedList

def printList(linkedList):
    """This is used to display a linkedList"""
    elements = []
    while linkedList != None:
        elements.append(linkedList.data)
        linkedList = linkedList.next
        
    print elements

def length(linkedList):
    """Project 8, returns the number of elements within a singly linked structure."""
    count = 0

    if linkedList != None:
        while linkedList != None:
            linkedList = linkedList.next
            count += 1
            
    else:
        print "\nCreate a linked structure first you dingus!"

    return count

def insert(newItem, index, linkedList, TwoWay):
    """Project 9, inserts an item into a linked structure at a given position. Returns the modified linked list. TwoWay is a boolean signaling the type of node."""
    if linkedList is None or index <= 0:
        linkedList = Node(newItem, linkedList)

    else:
        elements = []      
        
        while index > 1 and linkedList != None:
            elements.append(linkedList)
            linkedList = linkedList.next
            index -= 1

        print len(elements)
        if TwoWay == False:
            elements.append(Node(newItem, linkedList.next))

            #Rebuilding the linkedList so that we can return the head and not the node at index.
            while len(elements) >= 2:
                elements[len(elements)-2].next = elements.pop(len(elements)-1)

            #elements should only have one element now (the head)
            linkedList = elements[0]
            
        else:
            linkedList = TwoWayNode(newItem, linkedList, linkedList.next)
            
            while linkedList.previous != None:
                linkedList = linkedList.previous

    return linkedList

def remove(index, linkedList, TwoWay):
    """Project 10, removes an item in a linked structure at a given position and returns a tuple containing the removed Item and the new linked list. TwoWay is a boolean signaling the type of node."""
    if index <= 0 or linkedList.next is None:
        removedItem = linkedList.data
        linkedList = linkedList.next
    
    else:
        elements = []
        
        while index > 1 and linkedList.next != None:
            elements.append(linkedList)
            linkedList = linkedList.next
            index -= 1

        #Save the removed item and then overwrite it
        removedItem = linkedList.next.data
        elements[len(elements)-1].next = linkedList.next.next

        if TwoWay == False:
            #Rebuilding the linkedList so that we can return the head and not the node at index.
            while len(elements) >= 2:
                elements[len(elements)-2].next = elements.pop(len(elements)-1)

            #elements should only have one element now (the head)
            linkedList = elements[0]
            

        else:
            linkedList = TwoWayNode(newItem, linkedList, linkedList.next)
            
            while linkedList.previous != None:
                linkedList = linkedList.previous

        return (linkedList, removedItem)



        
