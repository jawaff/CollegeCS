#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include "Date.h"


///Constructor for the Date class. It's assumed that the date passed is valid.
///@post The day, month and year variables are set to something. The 
///@param m The day of month for the Date
///@param d The day of month for the Date
///@param y The day of month for the Date
///@return An instance for the Date class
Date::Date(int m, int d, int y)
{
	setDate(m,d,y);
}

///This is for setting the date. It's assumed that the date passed is valid.
///@post The day, month and year variables will be set as something new.
///@param m The day of month for the Date
///@param d The day of month for the Date
///@param y The day of month for the Date
void Date::setDate(int m, int d, int y)
{
	day = d;
	month = m;
	year = y;
}

///To get the current day
///@return The day variable gets returned
int Date::getDay()
{
	return day;
}

///To get the current month
///@return The month variable gets returned
int Date::getMonth()
{
	return month;
}

///To get the current year
///@return The year variable gets returned
int Date::getYear()
{
	return year;
}

///Progress one day in time assuming that there are 31 days in each month.
///@post The day variable will be altered
void Date::progressOneDay()
{
	//This will check to see if this is the last day within the month
	//	(assuming generic months of 31 days.)
	if(day == 31)
	{
		day = 1;
		if(month == 12)
		{
			month = 1;
		}
		else
		{
			month += 1;
		}
	}
	else
	{
		day += 1;
	}
}

///This will progress the date by one month
///@post The month and possibly the year variables will change
void Date::progressOneMonth()
{
	if(month == 12)
	{
		month = 1;
		year += 1;
	}
	else
	{
		month += 1;
	}
}

///This will progress the date by one year
///@post The year variable will be changed
void Date::progressOneYear()
{
	year += 1;
}

///Computes and retrieves the numbered date string 
///	representation.
///@return A string that has the integer month, 
///	day and year variables separated by "/"s.
string Date::getNumDate()
{
	//The assembled date should be similar to "2/13/2013"
	stringstream converter(stringstream::in | stringstream::out);
	
	converter << month << "/" << day << "/" << year;

	return converter.str();
}

///Computes and returns the named date string representation.
///	It is assumed that each month starts on a Sunday.
///@return A string that has the names of the 
///	month and day along with the integer year
///	separated by "/"s.
string Date::getNamedDate()
{
	//The assembled date should be similar to "Sunday, 27, January, 2013"
	stringstream converter(stringstream::in | stringstream::out);

	//Determine the current day of the week and append it into date.
	//Note that we need to start on day #0 instead of day #1.
	//	Without it day #1 would start on a Tuesday every month.
	//	The modulo 7 is the reason behind this!
	switch((day-1) % 7)
	{
	case 0:
		converter << "Sunday";
		break;
	case 1:
		converter << "Monday";
		break;
	case 2:
		converter << "Tuesday";
		break;
	case 3:
		converter << "Wednesday";
		break;
	case 4:
		converter << "Thursday";
		break;
	case 5:
		converter << "Friday";
		break;
	case 6:
		converter << "Saturday";
		break;
	}

	converter << ", " << day << ", ";

	//Determine the name of the current month based on an integer value.
	switch(month)
	{
	case 1:
		converter << "January";
		break;
	case 2:
		converter << "February";
		break;
	case 3:
		converter << "March";
		break;
	case 4:
		converter << "April";
		break;
	case 5:
		converter << "May";
		break;
	case 6:
		converter << "June";
		break;
	case 7:
		converter << "July";
		break;
	case 8:
		converter << "August";
		break;
	case 9:
		converter << "September";
		break;
	case 10:
		converter << "October";
		break;
	case 11:
		converter << "November";
		break;
	case 12:
		converter << "December";
		break;
	}

	converter << ", " << year;

	return converter.str();
}
