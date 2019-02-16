
import math

def f(c,s):
    global i
    i = 0
    while c < s:
        c+=1
        if c > s and c % 1 != 0:
            break
        else:    
            i+=1

while True:
    c = float(input())
    s = float(input())
    f(c, s)
    print(i)
