using namespace std

class date
{
private:
    int day, month, year, format;

    nextDay(void)
    {
        if (day == 31 && (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10))
        {
            day = 1;
            month++;
        }
        else if (day == 30 && month % 2 == 0)
        {
            day = 1;
            month++;
        }
        else if (day == 31 && month == 12)
        {
            month = 1;
            year++;
        }
        else
        {
            day++;
        }
        return day, month, year;
    }
    previousDay(void)
    {

    }
    selectFormat(int)
    {

    }

public:

    date(int _day, int _month, int _year)
    {
        day = _day;
        month = _month;
        year = _year;
        format = 0;
    }
    void printDate()
    {
        if (format == 0)
        {
            cout << day << "/" << month << "/" << year << "/" << endl;
        }
        else if (format == 1)
        {
            cout << month << "/" << day << "/" << year << "/" << endl;
        }
        else if (format == 2)
        {
            cout << year << "/" << month << "/" << day << "/" << endl;
        }

    }
};
