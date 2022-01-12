def remove_mults(list2, upper, p):
    i = 2
    while p*i <= upper:
        if p*i in list2: list2.remove(p*i)
        i += 1
    return list2

def prime_nums_sum(lower, upper):
    list2 = [i for i in range(lower, upper+1)]
    if list2[0]%2 == 0: oddlist = list2[1:-1:2]
    else: oddlist = list2[0:-1:2]
    if oddlist[0] == 1: del oddlist[0]
    c = 0
    p = oddlist[c]
    while p**2 < upper:
        oddlist = remove_mults(oddlist, upper, p)
        c += 1
        p = oddlist[c]
    return sum(oddlist) + 2

print(prime_nums_sum(1, 2000000))
