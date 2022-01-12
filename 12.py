from math import sqrt

def multiples(x,n):
    list_of_multiples = []
    for i in range(1, n+1):
        list_of_multiples.append(x*i)
    return list_of_multiples

def factors(x):
    up_lim = int(sqrt(x)) + 1
    checklist = range(1, up_lim)
    list_of_factors = []
    for i in checklist:
        if x%i == 0:
            list_of_factors.append(float(i))
            list_of_factors.append(x/i)
        if x%i != 0:
            eliminate_list = multiples(i, up_lim//i)
            checklist = [x for x in checklist if x not in eliminate_list]
    return set(list_of_factors)

def tr_nos(n):
    integer_list = range(1, n+1)
    list_of_tr_nos = []
    for i in integer_list:
        list_of_tr_nos.append(sum(range(i+1)))
    return list_of_tr_nos

# print(tr_nos(12400)[12374])

# print(len(factors(76576500)))

def htdn():
    numbers = tr_nos(12500)[12000:12499]
    for h,i in enumerate(numbers):
        if len(factors(numbers[h])) >= 500: break
    return h, numbers[h]

print(htdn())
