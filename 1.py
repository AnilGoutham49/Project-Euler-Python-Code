def projeuler(n):
    list1 = []
    for i in range(1,n):
        if i%3==0: list1.append(i)
        if i%5==0: list1.append(i)
    set1 = set(list1)
    return sum(set1)

print(projeuler(1000))
