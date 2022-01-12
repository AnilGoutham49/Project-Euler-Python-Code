def prime_nums(lower, upper):
    list1 = []
    for num in range(lower,upper + 1):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                list1.append(num)
    return list1

def mult(list1):
    p = 1
    for x in list1:
        p = p*x
    return p

def lcm(n):
    l1 = prime_nums(1,n)
    l2 = [x for x in range(1,n+1)]
    l3 = []
    c1 = 0
    c2 = 0
    for i in range(len(l1)):
        c2 = 0
        for j in range(len(l2)):
            c1 = 0
            while l2[j]>1:
                if l2[j]%l1[i]==0: l2[j] /= l1[i]; c1 += 1
                else: break
            if c1>c2: c2 = c1
        l3.append(l1[i]**c2)
    return mult(l3)

print(lcm(20))
