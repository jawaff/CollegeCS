#ifndef _DATEINT
#define _DATEINT

#include <string>

using namespace std;

class DateInt
{
public:
	virtual void progressOneDay() = 0;
	virtual void progressOneMonth() = 0;
	virtual void progressOneYear() = 0;
	virtual string getNumDate() = 0;
	virtual string getNamedDate() = 0;
};

#endif
