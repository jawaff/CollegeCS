#include <iostream>
#include "BinarySearchTreeInterface.h"
#include "BinarySearchTree.h"

using namespace std;

void testAdd(BinarySearchTreeInterface* tree) {
	//loop through the items to be added.
	for (int i = 0; i < 10; i++) {
		//Using an alternating sequence to produce
		//	an item for the tree.
		unsigned int item = (unsigned int)pow(-1.0, i)*i + 15;
		tree->add(item);
	}
	
	cout << "testAdd(), adding in 10 items" << endl;
	cout << tree->str() << endl;
}

void testRemove(BinarySearchTreeInterface* tree)

int main() {
	BinarySearchTreeInterface* testTree = new BinarySearchTree();

	testAdd(testTree);
	testRemove(testTree);
	
	//Deallocate the testTree from the heap.
	delete testTree;
	testTree = nullptr;
	
	return 0;
}