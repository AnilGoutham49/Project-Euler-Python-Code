def projeuler():
   x=1
   y=2
   list1 = [1,2]
   list2 = []
   while list1[-1]<4000000:
       x=x+y
       y=x+y
       if x>4000000: break
       if y>4000000: break
       list1.append(x)
       list1.append(y)
   for i in list1:
       if i%2==0: list2.append(i)
   return sum(list2)

li = projeuler()
print(li)
