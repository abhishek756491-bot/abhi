#q1
# fruits = ("apple", "banana", "cherry", "date")
# print(fruits[0])
# print(fruits[-1])
# print(len(fruits))

#2
# colors = ("red", "green")
# print(colors*3)

#4
# a = (1, 2) 
# b = (3, 4)
# c = (5, 6)
# print(a+b+c)

#5
# numbers = (10, 20, 30, 40, 50, 60, 70)
# print(numbers[2:5])

#6
# items = (1, 2, 3, 4, 5)
# print(items[::-1])

#7
# my_list = [10, 20, 30, 40, 50]
# tuplee=tuple(my_list)
# print(tuplee)

#8
# chars = ('a', 'b', 'c')
# string=''.join(chars)
# print(string)

#9
# fruits = ("apple", "banana", "cherry", "date")

# print("cherry" in fruits)
# print("mango" in fruits)

#10
# votes = ("yes", "no", "yes", "yes", "no", "yes")
# yes_count=0
# no_count=0
# for x in votes:
#     if x == "yes":
#         yes_count += 1
#     else:
#         no_count += 1
# print("yse is:",yes_count, "no is : ",no_count)

#11
# person = ("Alice", 30, "Engineer", "Pune")
# name,age,passion,city=person
# print("name=",name,"age=",age,"passion=",passion,"and city=",city)

#12
# a = 100
# b = 200
# b,a=a,b
# print("b=",b,"a=",a)

#13
# matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# element = matrix[1][2]
# print(element)

#14
# scores = (88, 95, 70, 62, 99, 74, 85)
# print("max:",max(scores))
# print("min:",min(scores))
# print("sum:",sum(scores))

#15
# students = (("Alice", 88), ("Bob", 73), ("Charlie", 95), ("Diana", 61))
# is_short = sorted(students, key=lambda x: x[1])
# print(is_short)

#16
# numbers = (3, 14, 7, 22, 9, 41, 18, 5)
# filtered=tuple(x for x in numbers if x > 10)
# print(filtered)

#17
# numbers = (1, 2, 3, 4, 5, 6)
# squared=tuple(map(lambda x: x * x,numbers))
# print(squared)

#25
# keys = ("name", "age", "city")
# values = ("Alice", 30, "Pune")
# dic=dict(zip(keys,values))
# print(dic)

#26
# t1 = (1, 2, 3, 4, 5, 6)
# t2 = (4, 5, 6, 7, 8, 9)
# common = tuple(x for x in t1 if x in set(t2))
# print(common)

#27
# colours = ("red", "green", "blue") 
# l=list(colours)
# l[1]="yellow"
# replace=tuple(l)
# print(replace)

#28
# t = (1, 2, [3, 4, 5])
# print("Tuple id before:", id(t))
# t[2].append(99)
# print(t)
# print("Tuple id before:", id(t))



#29
# nested = (1, (2, 3), (4, (5, (6, 7))))
# k = []
# def flatten(data):
#     for x in data:
#         if isinstance(x, tuple):
#             flatten(x)  # अगर टुपल है, तो फंक्शन खुद को दोबारा चलाएगा
#         else:
#             k.append(x)  # अगर नंबर है, तो लिस्ट में जोड़ देगा
# flatten(nested)
# t=tuple(k)
# print(t)

#30
# from collections import namedtuple

# Employee = namedtuple("Employee", ["name", "department", "salary"])

# employees = (
#     Employee("Alice",   "Engineering", 95000),
#     Employee("Bob",     "Marketing",   72000),
#     Employee("Charlie", "Engineering", 88000),
# )

# for emp in employees:
#     print(f"{emp.name} works in {emp.department} and earns ${emp.salary:,}")

# top = max(employees, key=lambda e: e.salary)
# print(f"Highest paid: {top.name} (${top.salary:,})")

