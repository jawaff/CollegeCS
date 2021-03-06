
#ifndef _DATE
#define _DATE

#include <string>
#include "DateInt.h"

using namespace std;

class Date: public DateInt
{
  private:
    int month, day, year;

  public:
    Date(int m, int d, int y);

    void setDate(int m, int d, int y);
    int getDay();
    int getMonth();
    int getYear();

    virtual void progressOneDay();
    virtual void progressOneMonth();
    virtual void progressOneYear();
	virtual string getNumDate();
	virtual string getNamedDate();
};

#endif
