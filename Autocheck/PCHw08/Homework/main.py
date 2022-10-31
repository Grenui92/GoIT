from datetime import datetime, timedelta
def main(employee: list):

    result = {}

    for person in employee:
        employee_birthday = person['birthday']  # Берем дататайм обьект конкретного сотрудника (день рождения)
        days_dif = (employee_birthday - datetime.now()).days  # Находим разницу ДР сотрудника и текущей даты, потому что нам же нужны только те у кого ДР в ближайшие 7 дней

        #Отсеиваем сотрудников у которых ДР не попадает в ближайшие 7 дней
        if days_dif >= 7 or -1 > days_dif:
            continue
        #Проверяем на ДР в субботу или воскресенье
        if employee_birthday.strftime("%A") in ('Saturday', 'Sunday'):
            employee_birthday = from_sturday_and_sunday_to_monday(employee_birthday=employee_birthday)

        result.setdefault((employee_birthday.strftime("%A"), employee_birthday.date()), []).append(person['name'])
    show_days_to_be_blessed(result=result)


def from_sturday_and_sunday_to_monday(employee_birthday):
    if employee_birthday.strftime('%A') == 'Saturday':
        employee_birthday += timedelta(days=2)
        return employee_birthday
    elif employee_birthday.strftime('%A') == 'Sunday':
        employee_birthday += timedelta(days=1)
        return employee_birthday

def show_days_to_be_blessed(result):
    for k, v in sorted(result.items(), key=lambda x: x[0][1]):
        print('Who needs to be blessed with a birthday on {}, {}: {}'.format(*k, ', '.join(v)))



# test_dicts = [{'name': 'Jhon', 'birthday': datetime(year=2022, month=11, day=6)},
#               {'name': 'Peter', 'birthday': datetime(year=2022, month=11, day=5)},
#               {'name': 'Roland', 'birthday': datetime(year=2022, month=11, day=8)},
#               {'name': 'Kate', 'birthday': datetime(year=2022, month=11, day=1)},
#               {'name': 'Lili', 'birthday': datetime(year=2022, month=11, day=5)},
#               {'name': 'Rim', 'birthday': datetime(year=2022, month=10, day=31)},
#               {'name': 'Kiti', 'birthday': datetime(year=2022, month=11, day=2)},
#               {'name': 'Toma', 'birthday': datetime(year=2022, month=10, day=31)},
#               {'name': 'Saha', 'birthday': datetime(year=2022, month=11, day=1)},
#               {'name': 'Fila', 'birthday': datetime(year=2022, month=11, day=4)},
#               {'name': 'Sreda', 'birthday': datetime(year=2022, month=11, day=3)}]


if __name__ == "__main__":
    main(test_dicts)