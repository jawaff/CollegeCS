#include <string>
#include <sstream>
//This is only needed for debugging
#include <iostream>
#include "BinarySearchTree.h"

using namespace std;

BinarySearchTree::BinarySearchTree():
	rootPtr(nullptr){}
BinarySearchTree::~BinarySearchTree() {
	this->clear(this->rootPtr);
}
void BinarySearchTree::clear(BinaryNode* subtree) {
	//The base case is when the subtree is a leaf node.
	//	So the recursive calls will be skipped once a leaf
	//	node is hit.
	if (!subtree->isLeaf()) {
		if (subtree->getLeft != nullptr) {
			this->clear(subtree->getLeft);
		}
		if (subtree->getRight != nullptr) {
			this->clear(subtree->getRight);
		}		
	}
	//At this point, all nodes within this subtree
	//	should be deallocated already.
	//	So we deallocate the leaf node. 
	delete subtree;
}
///This is for checking to see if the tree is 
///	empty or not.
///@return A boolean, true means the tree is
///	empty, false means the tree isn't.
bool BinarySearchTree::isEmpty(BinaryNode* tree) const{
	return (tree == nullptr);
}
///This is for checking to see if an item
///	already exists within the tree.
bool BinarySearchTree::contains(const unsigned int item) const{
	
}

//This is just to call the add method with the rootPtr
//	as an arguement, because the rootPtr is private.
void BinarySearchTree::add(const unsigned int item) {
	add(item, this->rootPtr);
}

void BinarySearchTree::add(const unsigned int item, 
						   BinaryNode* subtree) {
	//Create a new node for the tree
	BinaryNode* newNode = new BinaryNode(item);
	
	//Case 1 - the tree is empty.
	//(This is also the base case.)
	if (this->isEmpty(subtree)) {
		//Do a soft-copy to add in the new node.
		subtree = newNode;
	}
	//Case 2 - The tree isn't empty and we want
	//	to add to the right subtree.
	else if (item >= subtree->getItem()) {
		//Make a recursive call that moves towards
		//	the base case.
		this->add(item, subtree->getRight());
	}
	//Case 3 - The tree isn't empty and we want
	//	to add to the left subtree.
	else {
		//Make a recursive call that moves towards
		//	the base case.
		this->add(item, subtree->getLeft());
	}
}

//This is just to call the remove method with the rootPtr
//	as an arguement, because the rootPtr is private.
bool BinarySearchTree::remove(const unsigned int item) {
	return remove(item, this->rootPtr);
}

//If there's time, remove using a lower/upper bound
///This is meant to remove a single item from the tree.
///	If there are multiple of the same item, then
///	we'll only remove the first one we find.
///@return A boolean, true means the item was
///	successfully removed, false means it wasn't.
bool BinarySearchTree::remove(const unsigned int item,
							  BinaryNode* subtree) {
	//Case 1 - the tree is empty, so we'll just return
	//	false (this is a base case.)
	if (this->isEmpty(subtree)) {
		return false;
	}

	//Case 2 - The tree isn't empty and we want
	//	to remove from the right subtree.
	if (item >= subtree->getItem()) {
		//Checks to see if the right node off of the
		//	root (of the subtree) contains the item
		//	we're looking for.
		//This is a sort of base case.
		if (subtree->getRight()->getItem() == item) {
			//This just is for clarity.
			BinaryNode* rightNode = subtree->getRight();
			
			//SubCase 1 - The right Node has no children.
			if (rightNode->isLeaf()) {
				//deallocate the node that was found
				//	from the heap.
				delete rightNode;
				rightNode = nullptr;
				
				//I wasn't sure if assigning 
				//nullptr to rightNode would also alter 
				//subtree->getRight()
				cout << "This should be nullptr: " 
					<< subtree->getRight() << endl;
				
				//Return true, because the removal
				//	suceeded.
				return true;
			}
			//SubCase 2 - The rightNode has 1 child
			//It checks to see if the right and left nodes
			//	off of the rightNode aren't both empty or
			//	not empty (one is empty, the other is not.)
			else if (this->isEmpty(rightNode->getLeft())
					!= this->isEmpty(rightNode->getRight())) {
				//If the rightNode's right node is the one that
				//	wasn't empty.
				if (!this->isEmpty(rightNode->getRight())) {
					//Then we'll replace the rightNode with the
					//	rightNode's right node in the tree.
					subtree->setRight(rightNode->getRight());
					
					//deallocate the node that was found
					//	from the heap.
					delete rightNode;
					rightNode = nullptr;
					
					return true;
				}
				//If the rightNode's left node is the one that
				//	wasn't empty.
				else {
					//Then we'll replace the rightNode with the
					//	rightNode's left node in the tree.
					subtree->setRight(rightNode->getLeft());
					
					//deallocate the node that was found
					//	from the heap.
					delete rightNode;
					rightNode = nullptr;
					
					return true;
				}
			}
			//SubCase 3 - The rightNode has 2 children
			else {
				//Make a tmpPtr for searching through
				//	the right children of rightNode->getLeft()
				BinaryNode* tmpPtr = rightNode->getLeft();
				
				//This loops through the right children
				//	of tmpPtr until it reaches the end.
				while (tmpPtr->getRight() != nullptr) {
					//Move the tmpPtr to its right child.
					tmpPtr = tmpPtr->getRight();
				}
				
				//Now we can add rightNode->getRight()
				//	to the right node of tmpPtr. This
				//	will concatenate rightNode->getLeft()
				//	and rightNode->getRight().
				tmpPtr->setRight(rightNode->getRight());
				
				//Then if we add rightNode->getLeft()
				//	to the subtree, it'll also be adding
				//	rightNode->getRight().
				subtree->setRight(rightNode->getLeft());
				
				//deallocate the rightNode from the heap.
				delete rightNode;
				rightNode = nullptr;
				tmpPtr = nullptr;
				
				return true;
			}
		}
		//We haven't found the item we're looking 
		//	for yet.
		else {
			//Recursively call remove and move
			//	towards the base case.
			return this->remove(item, subtree->getRight());
		}
	}
	//Case 3 - The tree isn't empty and we want
	//	to remove from the left subtree.
	else {
		//Checks to see if the right node off of the
		//	root (of the subtree) contains the item
		//	we're looking for.
		//This is a sort of base case.
		if (subtree->getLeft()->getItem() == item) {
			//This just is for clarity.
			BinaryNode* leftNode = subtree->getLeft();
			
			//SubCase 1 - The right Node has no children.
			if (leftNode->isLeaf()) {
				//deallocate the node that was found
				//	from the heap.
				delete leftNode;
				leftNode = nullptr;
				
				//I wasn't sure if assigning 
				//nullptr to leftNode would also alter 
				//subtree->getLeft()
				cout << "This should be nullptr: " 
					<< subtree->getLeft() << endl;
				
				//Return true, because the removal
				//	suceeded.
				return true;
			}
			//SubCase 2 - The leftNode has 1 child
			//It checks to see if the right and left nodes
			//	off of the leftNode aren't both empty or
			//	not empty (one is empty, the other is not.)
			else if (this->isEmpty(leftNode->getLeft())
					!= this->isEmpty(leftNode->getRight())) {
				//If the leftNode's right node is the one that
				//	wasn't empty.
				if (!this->isEmpty(leftNode->getRight())) {
					//Then we'll replace the leftNode with the
					//	leftNode's right node in the tree.
					subtree->setLeft(leftNode->getRight());
					
					//deallocate the node that was found
					//	from the heap.
					delete leftNode;
					leftNode = nullptr;
					
					return true;
				}
				//If the leftNode's left node is the one that
				//	wasn't empty.
				else {
					//Then we'll replace the leftNode with the
					//	leftNode's left node in the tree.
					subtree->setLeft(leftNode->getLeft());
					
					//deallocate the node that was found
					//	from the heap.
					delete leftNode;
					leftNode = nullptr;
					
					return true;
				}
			}
			//SubCase 3 - The leftNode has 2 children
			else {
				//Make a tmpPtr for searching through
				//	the right children of rightNode->getLeft()
				BinaryNode* tmpPtr = leftNode->getLeft();
				
				//This loops through the right children
				//	of tmpPtr until it reaches the end.
				while (tmpPtr->getRight() != nullptr) {
					//Move the tmpPtr to its right child.
					tmpPtr = tmpPtr->getRight();
				}
				
				//Now we can add leftNode->getRight()
				//	to the right node of tmpPtr. This
				//	will concatenate leftNode->getLeft()
				//	and leftNode->getRight().
				tmpPtr->setRight(leftNode->getRight());
				
				//Then if we add leftNode->getLeft()
				//	to the subtree, it'll also be adding
				//	rightNode->getRight().
				subtree->setLeft(leftNode->getLeft());
				
				//deallocate the leftNode from the heap.
				delete leftNode;
				leftNode = nullptr;
				tmpPtr = nullptr;
				
				return true;
			}
		}
		//We haven't found what we're looking for yet.
		else {
			return this->remove(item, subtree->getLeft());
		}
	}	
}

string BinarySearchTree::strHelper(BinaryNode* tree, unsigned int level) const{
	stringstream result;
	
	if (!tree->isEmpty()) {
		result << strHelper(tree->getRight(), level+1)
		for (int i = 0; i < level; i++) {
			result << "| ";
		}
		result << tree->getItem() << "\n";
		result << strHelper(tree->getLeft(), level+1);
	}
	return result.str();
}

string BinarySearchTree::str() const{
        return strHelper(self, 0)
}


string BinarySearchTree::inorderTraverse() const{
	
}
string BinarySearchTree::postOrderTraverse() const{
	
}
string BinarySearchTree::preorderTraverse() const{
	
}