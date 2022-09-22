
from math import factorial
from random import sample


def permutations(s):
    print(s)
    result = set()
    if len(s) == 2:
        while len(result) != factorial(len(s)):
            a = sample(s, k=len(s))
            v = ''.join(a)
            result.add(v)
    elif len(s) == len(set(s)):
        while len(result) != factorial(len(set(s))):
            a = sample(s, k=len(s))
            v = ''.join(a)
            result.add(v)
    else:
        while len(result) != factorial(len(s) - 1):
            a = sample(s, k=len(s))
            v = ''.join(a)
            result.add(v)
    return result

    
print(permutations('aabb'))
