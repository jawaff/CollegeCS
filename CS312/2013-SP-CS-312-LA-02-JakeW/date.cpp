#include "date.hpp"

///Constructor for the Date class
/// @post The day, month and year variables are set to something.
/// @param  d is an integer that represents the day of month.
/// @param  m is an integer that represents the month of year.
/// @param  y is an integer that represents the year.
/// @return An instance for the Date class
Date::Date(int d, int m, int y)
{
	month = m;
	day = d;
	year = y;
}

///Progress one day in time
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

///This is for setting the date
///@post The day, month and year variables will be set as something new.
/// @param  d is an integer that represents the day of month.
/// @param  m is an integer that represents the month of year.
/// @param  y is an integer that represents the year.
void Date::setDate(const int d, const int m, const int y)
{
	day = d;
	month = m;
	year = y;
}

///To get the current day
///@return The day variable gets returned
int Date::getDay() const
{
	return day;
}

///To get the current month
///@return The month variable gets returned
int Date::getMonth() const
{
	return month;
}

///To get the current year
///@return The year variable gets returned
int Date::getYear() const
{
	return year;
}
