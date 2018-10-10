BinaryNode::BinaryNode() {
	this->leftNode = nullptr;
	this->rightNode = nullptr;
	
	this->item = 0;
}
BinaryNode::BinaryNode(unsigned int value) {
	this->leftNode = nullptr;
	this->rightNode = nullptr;
	
	this->item = value;
}
void BinaryNode::setItem(unsigned int value) {
	this->item = value;
}
unsigned int BinaryNode::getItem() {
	return this->value;
}

bool BinaryNode::isLeaf() {
	return ( (this->leftNode == nullptr) 
			&& (this->rightNode == nullptr) );
}

void BinaryNode::setLeft(BinaryNode* subtree) {
	this->leftNode = subtree;
}
void BinaryNode::setRight(BinaryNode* subtree) {
	this->rightNode = subtree;
}

BinaryNode* BinaryNode::getLeft() {
	return this->leftNode;
}
BinaryNode* BinaryNode::getRight() {
	return this->rightNode;
}