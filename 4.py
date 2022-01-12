# def palindrome(n):
#     s = str(n)
#     if s == s[::-1]: print('Given number is a palindrome')
#     else: print('Given number isn\'t a palindrome')
#
# palindrome(907)

def prod_palindrome():
    list1 = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            k = i*j
            l = str(k)
            if l == l[::-1]: list1.append(k)
    list1.sort()
    return f'The largest palindrome made from the product of two 3-digit numbers is {list1[-1]}'

print(prod_palindrome())
