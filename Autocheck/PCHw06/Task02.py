def write_employees_to_file(employee_list, path):
    file = open(path, 'w')
    for employee in employee_list:
        if type(employee) == list:
            for i in employee:
                file.write(f'{i}\n')
        else:
            file.write(f'{employee}\n')
    file.close()

write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']], 'Task02.txt')