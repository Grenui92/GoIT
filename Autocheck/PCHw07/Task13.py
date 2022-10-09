def get_employees_by_profession(path, profession):
    result = []
    with open(path, 'r') as file:
        for strin in file.readlines():
            name, job = strin.split()
            if job == profession:
                result.append(name)
    return ' '.join(result)

print(get_employees_by_profession('Task13.txt', 'courier'))
    