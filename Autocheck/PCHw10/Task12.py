class IDException(Exception):
    pass



def add_id(id_list, employee_id):
    if employee_id[:2] != "01":
        raise IDException
    else:
        id_list.append(employee_id)
        return id_list



print(add_id([], "113"))