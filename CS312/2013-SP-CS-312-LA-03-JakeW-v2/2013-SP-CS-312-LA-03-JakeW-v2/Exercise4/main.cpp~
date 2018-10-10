///page 115 Exercise #4

///1. Year and Semester : 2013 SPRING
///2. Course Number : CS-312
///3. Course Title : OO Design/Implementation
///4. Work Number : LA-03
///5. Work Name : Exercises Ch 03
///6. Work Version : Version 2
///7. Long Date : Wednesday, 13, February, 2013
///8. Author(s) Name(s) : Jake Waffle

#include <string>
#include <iostream>
#include <stdlib.h>
#include <sstream>
#include "Rectangle.h"

using namespace std;

int main()
{
	bool finished = false;
	string xa, ya, wa, ha;
	float xb, yb, wb, hb;

	Rectangle rect;
	string exitCondition;

	cout << "\nYou're going to be adding in the dimensions for a Rectangle and this will print the results of some calculations\n\n";

	while(!finished)
	{
		cout << "Enter in an x-value: ";
		getline(cin,xa);

		cout << "Enter in a y-value: ";
		getline(cin,ya);

		cout << "Enter in a width: ";
		getline(cin,wa);

		cout << "Enter in a height: ";
		getline(cin,ha);

		istringstream(xa) >> xb;
		istringstream(ya) >> yb;
		istringstream(wa) >> wb;
		istringstream(ha) >> hb;

		rect.setDimensions(xb, yb, wb, hb);

		cout << "The computed perimeter is: " << rect.getPerimeter() << endl
			<< "The computer area is: " << rect.getArea() << endl;

		cout << "Enter something if you'd like to quit: ";
		getline(cin, exitCondition);

		if(exitCondition != "")
		{
			finished = true;
		}
	}
	return 0;
}

