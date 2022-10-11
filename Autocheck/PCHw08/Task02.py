from datetime import date


def get_days_in_month(month, year):
    d = date(month=month,year=year,day=1)
    if month == 12:
        sd = date(month=1, year=year+1, day=1)
    else:
        sd = date(month=month+1, year=year, day=1)
    return (sd-d).days


print(get_days_in_month(int(input()), int(input())))