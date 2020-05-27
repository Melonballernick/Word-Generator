import random
import ast

w = []
i = []
n = 'X'

def load(a):
    global w
    g = open(a + ".txt", "r").readlines()
    for x in g:
        if x == "\n":
            x = ''
    w = ast.literal_eval('[' + ''.join(g) + ']')

def gen(l):
    global w
    global i
    global n
    s = []
    k = 0
    while k < l:
        i = 0
        q = random.randint(1,1000000)
        p = 0
        while i < len(w):
            p = p + (w[i][1] * 10000)
            i = i + 1
        i = 0
        while i < len(w):
            p = p - (w[i][1] * 10000)
            if q >= p:
                if res() == 1:
                    s.append(w[i][0])
                    n = w[i][2]
                    break
                else:
                    k = k - 1
                    break
            i = i + 1
        k = k + 1
    return''.join(s)

def res():
    global n
    if w[i][2] == 'X':
        return 1
    elif w[i][2] == 'C':
        if n == 'X': return 1
        elif n == 'C': return 0
        elif n == 'V': return 1
    elif w[i][2] == 'V':
        if n == 'X': return 1
        elif n == 'C': return 1
        elif n == 'V': return 0
        
    
