def oddnums(n):
    l1 = []
    if n%2==0:
        k = n-1
        while k>1:
            l1.append(k)
            k -= 2
    else:
        k = n
        while k>1:
            l1.append(k)
            k -= 2
    l1.append(1)
    l1 = l1[::-1]
    return l1

import math

def triplets():
    l1 = oddnums(2000000)
    k = [i*i for i in l1[:188]]
    l2 = []
    for i in range(len(k)):
        l2.append(l1.index(k[i]))
    b_sq = []
    for ind, j in enumerate(l2):
        b_sq.append(sum(l1[:j]))
    c_sq = []
    for ind, j in enumerate(l2):
        c_sq.append(sum(l1[:(j+1)]))
    b = []
    c = []
    for i in b_sq:
        b.append(int(math.sqrt(i)))
    for i in c_sq:
        c.append(int(math.sqrt(i)))
    a = [i for i in l1[:188]]
    trips = list(zip(a, b, c))[1:]
    # l3 = []
    # for i in trips:
    #     l3.append(i[0]+i[1]+i[2])
    return trips[-1][2]
        # if i[0]+i[1]+i[2] == 1000: return i
        # else: return 'Sorry, you\'re out of luck'
    # return type(trips[1])

print(triplets())
