#ifndef BINARY_SEARCH_TREE_INTERFACE
#define BINARY_SEARCH_TREE_INTERFACE

#include <string>

class BinarySearchTreeInterface {
	public:
		virtual void clear() = 0;
		
		virtual bool isEmpty() = 0 const;
		virtual bool contains(const unsigned int item) = 0 const;
		
		virtual void add(const unsigned int item) = 0;
		virtual bool remove(const unsigned int item) = 0;
		
		virtual std::string str() const;
		
		virtual std::string inorderTraverse() = 0 const;
		virtual std::string postorderTraverse() = 0 const;
		virtual std::string preorderTraverse() = 0 const;
};

#endif