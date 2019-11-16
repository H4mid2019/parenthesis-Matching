def parntcheck(exper):
    if exper == '' or exper == ' ':
        return 'False'
    char_frerq = {}
    lst = []
    po = tuple('({[')
    pc = tuple(')}]')
    for p in exper:
        if p in po or p in pc:
            lst.append(p)
            if p in char_frerq:
                char_frerq[p] += 1
            else:
                char_frerq[p] = 1

    for i in lst:
        if ')' in lst and '(' in lst:
            if lst.index(')') < lst.index('('):
                return 'False'
            if char_frerq['('] != char_frerq[')']:
                return 'False'
            if lst[lst.index(')')-1] != '(':
                return 'False'
        elif ']' in lst and '[' in lst:
            if lst.index(']') < lst.index('['):
                return 'Flase'
            if char_frerq['['] != char_frerq[']']:
                return 'False'
            if lst[lst.index('[')-1] != ']':
                return 'False'
        elif '}' in lst and '{' in lst:
            if lst.index('}') < lst.index('{'):
                return 'False'
            if char_frerq['{'] == char_frerq['}']:
                return 'False'
            if lst[lst.index('{')-1] != '}':
                return 'False'
        elif ')' in lst and '(' not in lst or ']' in lst and '[' not in lst or '}' in lst and '{' not in lst:
            return 'False'
        elif '(' in lst and ')' not in lst or '[' in lst and ']' not in lst or '{' in lst and '}' not in lst:
            return 'False'

    return 'True'


for i in range(9):
    print(parntcheck(str(input())))
