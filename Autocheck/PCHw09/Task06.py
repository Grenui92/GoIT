import re
def generator_numbers(string=""):
    result = re.findall(r'(\d+|[+*\-()])', string)
    return result

def sum_profit(string):
    return sum(int(i) for i in generator_numbers(string = string))