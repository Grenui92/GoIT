from datetime import datetime


def get_str_date(date):
    y, m, d = [int(i) for i in date.split()[0].split('-')]
    str_date = datetime(year=y, month=m, day=d).date()
    pretty_date = str_date.strftime('%A %d %B %Y')
    return pretty_date


print(get_str_date("2021-05-27 17:08:34.149Z"))