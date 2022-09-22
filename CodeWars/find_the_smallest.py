def smallest(n):
    n = list(str(n))
    old_index = len(n)-n[::-1].index(min(n[1:]))-1
    minimum = n.pop(old_index)
    for i in range(len(n)):
        if int(n[i]) > int(minimum):
            n.insert(i, minimum)
            return [int(''.join(n)), i, old_index] if minimum == '0' else [int(''.join(n)), old_index, i]

print(smallest(119989884756))
# testing(209917, [29917, 0, 1]);
# testing(285365, [238565, 3, 1]);
# testing(269045, [26945, 3, 0]);
# testing(296837, [239687, 4, 1]);
