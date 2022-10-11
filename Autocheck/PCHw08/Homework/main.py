from datetime import datetime
def main(employee):
    result = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
    for i in employee:
        days = i['birthday']  # Берем дататайм обьект конкретного сотрудника (день рождения)
        days_dif = (days - datetime.now()).days  # Находим разницу ДР сотрудника и текущей даты, потому что нам же нужны только те у кого ДР в ближайшие 7 дней
        if days_dif > 7 or 0 > days_dif:  # Прерывам данную итерацию, если ДР нам не подходит
            continue
        week_day_str = i['birthday'].strftime('%A')  # Буквенный день недели
        if week_day_str in ('Saturday', 'Sunday'):
            result['Monday'].append(i['name'])  # Если день недели сб или вс - переносим поздравления на понедельник - добавляем в список понедельника
            continue

        result[week_day_str].append(i['name'])
    # Вот дальше у меня загвоздка. Нужно будет у препода спрашивать как правильно вывод делать. Оно и сейчас выводит правильно, но хз. Мне пока не нравится что
    # все время с понедельника начинается и непонятно какой понедельник. Понятно что при требовании "вывести инфу на ближайшие семь дней" дни недели
    # встретятся только один раз, но все равно тупо - если на улице среда, то все равно вывод начинается с понедельника. Нужно или самому подумать или совета
    # у препода спросить
    for k, v in result.items():
        print(f"Whose birthdays you need to congratulate on {k}: {', '.join(v)}")



test_dicts = [{'name': 'Jhon', 'birthday': datetime(year=2022, month=10, day=16)},
              {'name': 'Peter', 'birthday': datetime(year=2022, month=10, day=18)},
              {'name': 'Roland', 'birthday': datetime(year=2022, month=10, day=19)},
              {'name': 'Kate', 'birthday': datetime(year=2022, month=10, day=23)},
              {'name': 'Lili', 'birthday': datetime(year=2022, month=10, day=11)},
              {'name': 'Rim', 'birthday': datetime(year=2022, month=12, day=12)},
              {'name': 'Kiti', 'birthday': datetime(year=2022, month=10, day=13)},
              {'name': 'Toma', 'birthday': datetime(year=2022, month=10, day=14)},
              {'name': 'Saha', 'birthday': datetime(year=2022, month=10, day=15)},
              {'name': 'Fila', 'birthday': datetime(year=2022, month=10, day=17)},
              {'name': 'Sreda', 'birthday': datetime(year=2022, month=10, day=12)}]
if __name__ == "__main__":
    main(test_dicts)