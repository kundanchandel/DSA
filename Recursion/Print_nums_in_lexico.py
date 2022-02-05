'''
You will be given a value n, print first n+1 whole number in lexiographical order.
0
1
10
100
1000
101
102
103 ... 109
11
110
111
112
'''

# Hint: Build recusion tree.


def printLexico(n,i):
    if n<i:
        return
    print(i)
    for j in range(1 if i == 0 else 0,10):
        printLexico(n,10*i + j)

printLexico(19,0)
