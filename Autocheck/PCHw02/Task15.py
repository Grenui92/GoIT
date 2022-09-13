result = None
operand = int
operator = str
wait_for_number = False

while True:
    try:
        if result == None:
            result = int(input('Operand: '))
        if wait_for_number == False:
            operator = input("Operator: ")
            if operator not in '+-*/=':
                print('This is not operator')
                continue
            wait_for_number = True
        if operator =='=':
                break
        if wait_for_number:
            operand = int(input('Operand: '))
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

print(result)