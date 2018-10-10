//1. Year and Semester : 2013 SPRING
//2. Course Number : CS-312
//3. Course Title : OO Design/Implementation
//4. Work Number : LA-09
//5. Work Name : LinkedBag Ch04
//6. Work Version : Version 1
//7. Long Date : Sunday, 17, March, 2013
//8. Author(s) Name(s) : Jake Waffle

///@file main.cpp

#include <iostream>
#include "LinkedBag.h"

using namespace std;

void testLinkedBag()
{
	LinkedBag<int> bag;

	int item = 5;

	for(int i = 0; i < 10; i++)
	{
		bag.addWithResize(item);
	}

	///If there is more items than the DEFAULT_CAPACITY,
	///	then the new add method works with regard to resizing.
	///If there is a "5" in the bag, it was added into the bag.
	///And if there are 10 "5"'s in the bag, all of them
	///	were added successfully.
	if (bag.getCurrentSize() > 6 &&
		bag.contains(5)	&&
		bag.getFrequencyOf(5) == 10)
	{
		cout << "The ArrayBag's new addWithResize method was successful!" << endl;
	}
	else
	{
		cout << "The ArrayBag's new addWithResize method failed!" << endl;
	}
}

int main()
{
	testLinkedBag();
	return 0;
}
