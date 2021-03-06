///page 115 Problem #2

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
#include "Date.h"

///Contributers:
///I referenced www.cpluplus.com/forum/general/13135 to determine how to convert
///		from a string to an integer using atoi().
///I referenced http://stackoverflow.com/questions/190229/where-is-the-itoa-function-in-linux
///		when needing a way to convert an integer to a string (itoa isn't in stdlib.h.)

using namespace std;

int main()
{
	bool finished = false;
	//These will hold the user's inputs for the date.
	string day, month, year;

	//cout is C++'s print (comparing to Python.)
	cout << "Enter in an integer that represents the day: "; 

	//getline uses cin to get the user's input, then it stores that input in the
	//	given variable (which is day in this case.)
	getline(cin, day);

	cout << "Enter in an integer that represents the month: ";
	getline(cin, month);

	cout << "Enter in an integer that represents the year: ";
	getline(cin, year);

	if ((atoi(day.c_str()) > 31 || atoi(day.c_str()) < 1) || (atoi(month.c_str()) > 12 || atoi(month.c_str()) < 1))
	{
		cout << "The date you entered is invalid!\n";
		finished = true;
	}

	//This is an instance of the Date class that was created for Excercise #2.
	//atoi is used for converting c-style strings into integers (it also ignores
	//	all non-number characters in the string.)
	//Because atoi requires c-style strings and the imported string container is
	//	different, we have to call the string's "c_str()" method to get the 
	//	c-style string.
	Date currentDay(atoi(month.c_str()), atoi(day.c_str()), atoi(year.c_str()));

	while(!finished)
	{
		//This displays the current date according to the currentDay Date
		//	instance.
		cout << "The current date is " << currentDay.getNumDate() << " (numbered)" << endl;
		cout << "The current date is " << currentDay.getNamedDate() << " (named)" << endl;

		//This checks to see by which time period the user wishes to advance
		cout << "Enter a character to advance the associated time period (d = day, m = month, y = year): ";

		//This variable will store the user's input
		string decision;
		getline(cin, decision);

		//This checks for inputs of meaning and executes the appropriate class 
		//	method.
		if(decision == "d")
		{
			currentDay.progressOneDay();
		}
		else if(decision == "m")
		{
			currentDay.progressOneMonth();     
		}
		else if(decision == "y")
		{
			currentDay.progressOneYear();      
		}
		else if (decision == "")
		{
			finished = true;
		}
	}
	return 0;
}
