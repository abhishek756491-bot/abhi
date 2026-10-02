# list = []
# print(type(list))

#dyanamic input
# list = eval(input("Enter input list: "))
# print(list)
# print(type(list))

#list function
# l=list(range(0,10,2))
# print(l)
# print(type(l))

##with split function
# s="Learning python is very very easy !!!"
# l=s.split()
# print(l)
# print(type(l))

# start here for questiion from py native
#1.
# numbers = [2, 3, 5, 7]
# print("third element - ",numbers[2])
# print("length of list - ",len(numbers))
# print("is list is emplty ? - ",[] in numbers)

#2
# numbers[1]=200
# numbers.append(600)
# numbers.insert(2,300)
# numbers.pop()
# numbers.pop(0)
# print(numbers)

#3
# sum=0
# l=len(numbers)
# for x in numbers:
#     sum=sum+x
#     avg=sum/l
# print("sum is : ",sum)
# print("avg is : ",avg)

#4
# max=numbers[0]
# min=numbers[0]
# for x in numbers:
#     if max < x:
#         max=x
#     if min > x:
#         min=x
# print(max)
# print(min)

#5
# p=1
# for x in numbers:
#     p=p*x
# print(p)

#6
# odd=0
# even=0
# for x in numbers:
#     if x%2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("even number in list : ",even)
# print("odd number in list : ",odd)

#7
# print("reverse list is :",numbers[::-1])

#8
# l = [56, 12, 89, 3, 22]
# l.sort()
# print(l)

#9
# m=l.copy()
# print(m)

#10
# c=l+m
# print(c)

#11
# print(l[1:4])

#12
# l[0],l[2]=l[2],l[0]
# print(l)

#13
# nlist=[[1, 2], [3, 4, 5], [6, 7]]
# print(nlist[1][2])

#14
# l=["Laptop", "Mouse", "Monitor", "Keyboard"]
# print("Laptop" in l)

#15 longest string
# large_str = l[0]
# for x in l:
#     if len(large_str) < len(x):
#         large_str = x
# print(large_str)

#16
# l= [1, 2, 3, 4, 5]
# s=[i*i for i in l]
# print(s)

#17
# a=[10, 20, 30, 10, 40, 10, 50]
# print(a.count(10))

#18
# l=[x for x in a if x != 10]
# print(l)

#19
# b=["Mike", "", "Emma", "Kelly", "", "Brad"]
# r=[x for x in b if x != ""]
# print(r)

#20
# duplicates = [10, 20, 10, 30, 40, 40, 20, 50]
# u=set(duplicates)
# unique=list(u)
# print(unique)

#21
# mix=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even=[x for x in mix if x%2 == 0]
# print(even)

#22
# l1=["Py", "is", "awes"]
# l2=["thon", " ", "ome"]
# l3=[]
# for x,y in zip(l1,l2):
#    l3.append(x+y)
# print(l3)

#23
List1= [10, 20, 30]
List2= [100, 200, 300]
list3= zip(List1,List2)
for x,y in list3:
    list3
print(list3)