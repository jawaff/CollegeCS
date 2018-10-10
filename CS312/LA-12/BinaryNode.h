#ifndef BINARY_NODE
#define BINARY_NODE

class BinaryNode{
	private:
		BinaryNode* leftNode;
		BinaryNode* rightNode;
		
		unsigned int item;
	public:
		BinaryNode();
		BinaryNode(unsigned int value);
		
		void setItem(const unsigned int value);
		unsigned int getItem() const;
		
		bool isLeaf() const;
		
		void setLeft(BinaryNode* subtree);
		void setRight(BinaryNode* subtree);
		
		BinaryNode* getLeft() const;
		BinaryNode* getRight() const;
};

#endif 