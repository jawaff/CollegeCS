#ifndef BINARY_SEARCH_TREE
#define BINARY_SEARCH_TREE

#include <string>
#include "BinarySearchTreeInterface.h"
#include "BinaryNode.h"

class BinarySearchTree 
: BinarySearchTreeInterface {
	private:
		BinaryNode* rootPtr;
		
		void add(const unsigned int item, BinaryNode* subtree);

		bool remove(const unsigned int item, BinaryNode* subtree);
		
		std::string stdHelper() const;
	public:
		BinarySearchTree();
		~BinarySearchTree();
		void clear(BinaryNode* subtree);
		
		bool isEmpty() const;
		bool contains(const unsigned int item) const;
		
		void add(const unsigned int item);

		bool remove(const unsigned int item);

		std::string str() const;
		
		std::string inorderTraverse() const;
		std::string postOrderTraverse() const;
		std::string preorderTraverse() const;
};

#endif