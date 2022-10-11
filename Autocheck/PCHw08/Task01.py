from datetime import datetime


def get_days_from_today(date):
    y, m, d = [int(i) for i in date.split('-')]
    data = datetime(year=y, month=m, day=d).date()
    now = datetime.now().date()
    return (now - data).days

print(get_days_from_today("2021-10-09"))