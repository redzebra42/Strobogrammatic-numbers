import sys
import math


def rot(i:int) -> int:
    if i in [0, 1, 8]:
        return i
    elif i == 6:
        return 9
    elif i == 9:
        return 6
    else:
        raise RuntimeError

def strobo_power_max(n_init, n, max_num):
    '''returns the number of strobogrammatic numbers between 10^(n-1) and min(max_num, 10^n)'''
    if n == 0:
        if n_init%2 == 0:
            return [rot(k)+k*10**(n_init-1) for k in [1, 6, 8, 9]]
        else:
            print([rot(k)+k*10**(n_init-1)+s*(n_init//2) for k in [1, 6, 8, 9] for s in [0, 1, 8]])
            return [rot(k)+k*10**(n_init-1)+s*(10**(n_init//2)) for k in [1, 6, 8, 9] for s in [0, 1, 8]]
    res = []
    for num in strobo_power_max(n_init, n-1, max_num):
        for i in [0, 1, 6, 8, 9]:
            if n%2 == 0:
                new_num = num + rot(i)*(10**n) + i*(10**(n_init-n-1))
            else:
                new_num = num + rot(i)*(10**n) + i*(10**(n_init-n-1))
            if new_num < max_num:
                res.append(new_num)
            else:
                break
    return res

print(strobo_power_max(17, 7, 100000000000000000000000000000))

