class EmptyTree(object):

    def isEmpty(self):
        return True
        
    def __str__(self):
        return ""
        
    def __iter__(self):
        #Iterator for the tree
        return iter([])
        
    def getLeft(self):
        return BinaryTree.THE_EMPTY_TREE
        
    def getRight(self):
        return BinaryTree.THE_EMPTY_TREE
        
    def height(self):
        return 0
        
    def preorder(self,lyst):
        return
        
    def inorder(self,lyst):
        return
        
    def postorder(self,lyst):
        return
        
    def levelorder(self,lyst):
        return
        
    def getRoot(self):
        raise AtrributeError, "Empty tree"
    
class BinaryTree(object):
    THE_EMPTY_TREE = EmptyTree()
    
    def __init__(self, item):
        self._root = item
        self._left = BinaryTree.THE_EMPTY_TREE
        self._right = BinaryTree.THE_EMPTY_TREE
        
    def isEmpty(self):
        return False
        
    def getRoot(self):
        return self._root
        
    def setRoot(self, item):
        self._root = item
        
    def getLeft(self):
        return self._left
    
    def getRight(self):
        return self._right
        
    def removeLeft(self):
        left = self._left
        self._left = BinaryTree.THE_EMPTY_TREE
        return left
        
    def setLeft(self, newItem):
        self._left = BinaryTree(newItem)
        
    def setRight(self, newItem):
        self._right = BinaryTree(newItem)
    
    def __iter__(self):
        lyst = []
        self.inorder(lyst)
        return iter(lyst)
        
    def inorder(self, lyst):
        self.getLeft().inorder(lyst)
        lyst.append(self.getRoot())
        self.getRight().inorder(lyst)
        
    def __str__(self):
        def strHelper(tree, level):
            result = ""
            if not tree.isEmpty():
                result += strHelper(tree.getRight(), level+1)
                result += "| " * level
                result += str(tree.getRoot()) + "\n"
                result += strHelper(tree.getLeft(), level+1)
            return result
        return strHelper(self, 0)
        
    def height(self, tree, height=-1):
        """A recursive function that computes the height of the tree!"""
        if tree.isEmpty():
            return height
        else:
            leftHeight = self.height(tree.getLeft(), height+1)
            rightHeight = self.height(tree.getRight(), height+1)
    
        if leftHeight > rightHeight:
            return leftHeight
        else:
            return rightHeight
    

    
    def rangeFind(self, mi,mx): 
            """rangeFind method finds the number from minimum to maximum and returns
            the numbers from the tree"""
            minimum = mi    # minimum number in the tree
            maximum = mx    # maximum number in the tree    
    
            treeNodes= []
            self.inorder(treeNodes)

            rangeOfNodes = []
            
            for node in treeNodes:
                    if node >= mi and node <= mx:
                            rangeOfNodes.append(node)

            return rangeOfNodes
            
            
            
    def frontier(self, tree):
        """Returns a list of the leaves of the tree.""" 
        if tree.isEmpty():
            return []
                
        elif tree.getLeft().isEmpty() and tree.getRight().isEmpty():
            return [tree.getRoot()]
        
        else:
            return self.frontier(tree.getLeft()) + self.frontier(tree.getRight())       


class BST(object):

    def __init__(self):
        self._tree = BinaryTree.THE_EMPTY_TREE
        self._size = 0
    
    def isEmpty(self):
        return len(self) == 0
        
    def __len__(self):
        return self._size
    
    def __str__(self):
      return str(self._tree)
      
    def __iter__(self):
      return iter(self.inorder())
    
    def inorder(self):
      lyst = []
      self._tree.inorder(lyst)
      return lyst
    
    def successor(self, item):
        """Given an item, this returns it successor (the next biggest item.)"""
        treeNodes = self.inorder()
        
        for indx in xrange(len(treeNodes)):
            if treeNodes[indx] == item:
                return treeNodes[indx+1]
      
    def predecessor(self,item):
        """Given an item, this returns it predecessor (the next smallest item.)"""
        treeNodes = self.inorder()
        
        for indx in xrange(len(treeNodes)):
            if treeNodes[indx] == item:
                return treeNodes[indx-1]
        
    def Add(self, newItem):
        """Adds newItem to the tree if it's not already in it
        or replaces the existing item if it is in it."""
        
        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self._tree = BinaryTree(newItem)
        
        # Otherwise, search for the item's spot
        else:           
            #Variables that will aid in the storage of the trees that we come across in our endeavors.
            
            currentTree = self._tree
            
            for layer in xrange(self._tree.height(self._tree)+1):
                currentItem = currentTree.getRoot()
                left = currentTree._left
                #left = currentTree.getLeft()
                right = currentTree._right
                #right = currentTree.getRight()
               
                # new item is less, go left until spot is found
                if newItem < currentItem:

                    if left.isEmpty():
                        currentTree._left = BinaryTree(newItem)
                        #currentTree.setLeft(BinaryTree(newItem))
                        break
                    else:
                        currentTree = left
                # new item is greater or equal,
                # go right until spot is found
                else:

                    if right.isEmpty():
                        currentTree._right = BinaryTree(newItem)
                        #currentTree.setRight(BinaryTree(newItem))
                        break
                    else:
                        currentTree = right
            
        self._size += 1
                
    def find(self,target):
         """#Returns data if target is found or None otherwise
         Helper function to search the binary tree"""
         def findHelper(tree):
             if tree.isEmpty():
                 return None
             elif target == tree.getRoot():
                 return tree.getRoot()
             elif target < treegetRoot():
                 return findHelper(tree._left) 
             else:
                 return findHelper(tree._right)
                
         return findHelper(self._tree)
        
    def writeToFile(self, fileObj):
         fileObj.write(str(self._tree))
         fileObj.close()
            


def doAction(action, tree):
    """Does the action given the user's inputted action number."""
    
    if action == 1:
        #Add to Tree    
        
        print "\nAdd to Tree"
        item = raw_input("\nEnter something to add into the tree: ")

        #Check if the item is acceptable for our tree
        if item.isdigit():    
            tree.Add(int(item))  #Numbers will be entered in as str data types
                        
            print "\n" + item, "has successfully been added into the Binary Tree"
                
        else:
            print "\nInvalid input:", item
            
    elif action == 2:
        #Print Range of Tree Nodes      
        
        print "\nRange Finder"
        #User eters the minimum number or character for the tree
        mi = raw_input("\nEnter Minimum number/character: ")
        #user enters the maximum number or character for the tree
        mx = raw_input("\nEnter Maximum number/character: ")
        
        if mi.isdigit() and mx.isdigit():
                
            print "\nHere's the range of nodes requested:\n"        

            #print the range number from the minimum to the maximum
            print tree._tree.rangeFind(int(mi),int(mx))
                
        else:
            print "\nInvalid input:", mi, "or", mx
                                             
    elif action == 3:
        #Print Height of Tree
            
        print "\nThe height of the tree is", tree._tree.height(tree._tree)
            
    elif action == 4:
        #Pint  Leaves of Tree
                    
        print "\nThe leaves of the Binary Tree:\n"
        listOfTrees = tree._tree.frontier(tree._tree)
        
        for i in xrange(len(listOfTrees)):
            print str(listOfTrees[i])

    elif action == 5:
        #Print Successor
            
        # asks user for input for the successor of the item given
        item = raw_input("\nEnter an item you'd like the successor of: ")
                    
        if item.isdigit():
            print "\nHere's the successor of", item + ":", tree._tree.successor(int(item))
                    
        else:
            print "\nInvalid Input!"
                    
    elif action == 6:
        #Print Predecesor
        
        # asks user for input for the predecessor of the item given
        item = raw_input("\nEnter an item you'd like the predecesor of: ")
                
        if item.isdigit():
                
            print "\nHere's the predecesor of", item + ":", tree._tree.predecesor(int(item))
                
        else:
            print "\nInvalid Input!"
    
    elif action == 7:
        #Writes Tree to file
       
        # passes file name to writeToFile method and writes the tree to the file
        tree.writeToFile(open("Tree.txt", "w"))
        print "\nTree has been written to a file"
        
    elif action == 8:
        #Print Tree
        
        print "\nHere's your current tree:\n"
        
        print str(tree._tree)

def main():
    searchTree = BST()
    
    actions = ("Add to Tree", "Print Range of Tree Nodes", "Print Height of Tree", \
                            "Print  Leaves of Tree", "Print Successor", "Print Predecesor", \
                            "Writes Tree to file", "Print Tree")
    
    finished = False
    
    while not finished:
        
        print ""
        for indx in xrange(len(actions)):
            print str(indx+1) + ". " + actions[indx]

                
        action = raw_input("\nEnter a number for your intended action: ")
        
        print ""    
        
        if action.isdigit():
            doAction(int(action), searchTree)
                
        bQuit = raw_input("\nEnter something to quit(or nothing to continue): ")
        
        if bQuit != "":
            finished = True


main()
