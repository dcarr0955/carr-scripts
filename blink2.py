import time

s = []

dict = {
    '.': lambda: print(s.pop(), end=" "),
    'CR': lambda: print(),
    'MS': lambda: time.sleep(s.pop()/1000),
    'BYE': lambda: time.sleep(0),
    'BLINK': ['1', '.', 'CR', '2000', 'MS', '0', '.', 'CR', '2000', 'MS'],
    'BLINK2':['BLINK', 'BLINK'],
    'MAIN': ['BLINK2', 'BYE']
}

def interpret(l):
    for o in l:
        if o.isdigit(): s.append(int(o))
        elif hasattr(dict[o], '__call__'): dict[o]()
        elif isinstance(dict[o], list): interpret(dict[o])
        else: print("Error = ", o)

interpret(['MAIN'])
