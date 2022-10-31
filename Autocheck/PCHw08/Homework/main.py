from datetime import datetime, timedelta
def main(employee: dict):

    result = {}

    for i in employee:
        employee_birthday = i['birthday']  # Берем дататайм обьект конкретного сотрудника (день рождения)
        days_dif = (employee_birthday - datetime.now()).days  # Находим разницу ДР сотрудника и текущей даты, потому что нам же нужны только те у кого ДР в ближайшие 7 дней

        if days_dif >= 7 or -1 > days_dif:  # Прерываем данную итерацию, если ДР нам не подходит
            continue
        if employee_birthday.strftime('%A') in ('Saturday', 'Sunday'):
            while employee_birthday.strftime('%A') != "Monday": #увеличиваем дату пока она не выпадет на ближайший понедельник
                employee_birthday += timedelta(days=1)
            result.setdefault((employee_birthday.strftime("%A"), employee_birthday.date()), []).append(i['name'])
            continue

        result.setdefault((employee_birthday.strftime("%A"), employee_birthday.date()), []).append(i['name'])

    for k, v in sorted(result.items(), key=lambda x: x[0][1]):
        print('Who needs to be blessed with a birthday on {}, {}: {}'.format(*k, ', '.join(v)))



# test_dicts = [{'name': 'Jhon', 'birthday': datetime(year=2022, month=11, day=6)},
#               {'name': 'Peter', 'birthday': datetime(year=2022, month=11, day=5)},
#               {'name': 'Roland', 'birthday': datetime(year=2022, month=11, day=8)},
#               {'name': 'Kate', 'birthday': datetime(year=2022, month=11, day=1)},
#               {'name': 'Lili', 'birthday': datetime(year=2022, month=11, day=5)},
#               {'name': 'Rim', 'birthday': datetime(year=2022, month=12, day=8)},
#               {'name': 'Kiti', 'birthday': datetime(year=2022, month=11, day=2)},
#               {'name': 'Toma', 'birthday': datetime(year=2022, month=10, day=31)},
#               {'name': 'Saha', 'birthday': datetime(year=2022, month=11, day=1)},
#               {'name': 'Fila', 'birthday': datetime(year=2022, month=11, day=4)},
#               {'name': 'Sreda', 'birthday': datetime(year=2022, month=11, day=3)}]


if __name__ == "__main__":
    main(test_dicts)