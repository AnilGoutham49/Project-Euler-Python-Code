def diff(n):
    sum_sqs = 0
    sq_sum = 0
    for i in range(1,n+1):
        sum_sqs = sum_sqs + (i**2)
        sq_sum = sq_sum + i
    return (sq_sum**2) - sum_sqs

print(diff(100))
