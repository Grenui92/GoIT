result = None
operand = None
operator = None
wait_for_number = True

while True:
    try:
        if result == None:
            result = float(input('Operand: '))
            wait_for_number = False
        if wait_for_number == False:
            operator = input("Operator: ")
            if operator not in '+-*/=':
                print('This is not operator')
                continue
            wait_for_number = True
        if operator == '=':
            break
        if wait_for_number:
            operand = float(input('Operand: '))
            wait_for_number = False
        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        elif operator == '*':
            result *= operand
        elif operator == '/':
            result /= operand
        
    except ValueError:
        print('Value error')
    except ZeroDivisionError:
        print('Zero Division. Try other operator or operand')

print(result)
