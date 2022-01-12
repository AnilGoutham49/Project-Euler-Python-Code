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

print(prime_nums(1, 110000)[10000])
