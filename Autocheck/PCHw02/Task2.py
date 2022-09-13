is_active = bool(int(input("Is the user active? ")))
is_admin = bool(int(input("Is the user administrator? ")))
is_permission = bool(int(input("Does the user have access? ")))

access = is_admin or (is_active and is_permission)
print(access)