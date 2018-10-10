#ifndef _Date
#define _Date

class Date
{
  private:
    int month;
    int day;
    int year;

  public:
    Date(const int d, const int m, const int y);
    void progressOneDay();
    void progressOneMonth();
    void progressOneYear();
    void setDate(const int d, const int m, const int y);
    int getDay() const;
    int getMonth() const;
    int getYear() const;
};
#endif
