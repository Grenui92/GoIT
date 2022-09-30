def is_reachable(start, end):
    [A,B,C],[D,E,F],[G,H,I] = start
    [a,b,c],[d,e,f],[g,h,i] = end
    st = ''.join(v for v in [A,F,G,B,I,D,C,H] if v != '_')
    en = ''.join(v for v in [a,f,g,b,i,d,c,h] if v != '_')
    return E==e and st == en or len(st) < 8 and (any(st[i:] + st[:i] == en for i in range(len(st))))
    
print(is_reachable([['W', 'W', 'W'],['W', '_', 'B'],['B', 'B', 'B']],[['W', 'W', 'W'],['W', '_', 'B'],['B', 'B', 'B']]))