numbers = [10, 20, 30, 40, 50]
len(numbers)
print(len(numbers))
is_empty = len(numbers) == 0
print(f"Is the list empty? {is_empty}")

InitialList = [100, 50, 400, 500]
InitialList[1]=200

print(InitialList)

InitialList.append(600)
print(InitialList)

InitialList.insert(2,300)
print(InitialList)

InitialList.remove(600)
print(InitialList)

InitialList.pop(0)
print(InitialList)

Numbers = [10, 20, 30, 40, 50]
sum=0
for i in range(len(Numbers)):
    sum=sum+Numbers[i]
print(sum)
print(sum/len(Numbers))


Data = [45, 12, 89, 2, 67]
min=min(Data)
max=max(Data)
print(min)
print(max)

Factors = [2, 3, 5, 7]
product=1
for i in Factors:
    product *= i
print(product)

Numbers = [10, 21, 4, 45, 66, 93, 11]
Ecount=0
Ocount=0
for i in Numbers:
    if i%2 == 0:
        Ecount += 1
    else:
        Ocount += 1
print("Even is",Ecount)
print("Odd is",Ocount)

List = [100, 200, 300, 400, 500]
List.reverse()
print(List)
#other way

List[::-1]
print(List)


Unsorted = [56, 12, 89, 3, 22]
Unsorted.sort()
print(Unsorted)

Original = ["Apple", "Banana", "Cherry"]
copy=Original.copy()
print(copy)

ListA = ["Physics", "Chemistry"]
ListB = ["Maths", "Biology"]
ListA.extend(ListB)
print(ListA)

List = [10, 20, 30, 40, 50, 60, 70]
print(List[2:5])

List = [23, 65, 19, 90]
List[0],List[2] =List[2],List[0]
print(List)

NestedList = [[1, 2], [3, 4, 5], [6, 7]]
k=NestedList[1][2]
print(k)

Inventory = ["Laptop", "Mouse", "Monitor", "Keyboard"]
print("Tablet is in Inventry : ","tablet" in Inventory)

words = ["PHP", "Exercises", "Backend", "Python"]
longest = max(words,key=len)
print(longest)

List = [1, 2, 3, 4, 5]
x=[x*x for x in List]
print(x)

List = [10, 20, 30, 10, 40, 10, 50]
k = List.count(10)
print(k)

List = [5, 20, 15, 20, 25, 50, 20]
x=[x for x in List if x != 20]
print(x)

List = ["Mike", "", "Emma", "Kelly", "", "Brad"]
x=[x for x in List if x != ""]
print(x)

List = [10, 20, 10, 30, 40, 40, 20, 50]
s=set(List)
l=list(s)
l.sort()
print(l)  

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x=[x for x in List if x%2 == 0]
print(x)

List1 = ["Py", "is", "awes"]
List2 = ["thon", " ", "ome"]
res = [i + j for i, j in zip(List1, List2)]
print(res)

List1 = [10, 20, 30]
List2 = [100, 200, 300]
for x,y in zip(List1,List2):
    print(x, y)

List = [10, 20, 30, 40, 50]
List.insert(3,35)
print(List)

List = [5, 10, 15, 20, 25]
List[3]=200
print(List)

List = [12, 35, 1, 10, 34, 1, 35]
l=set(List)
m=list(l)
m.sort()
print(m[-2])

my_list = [1, 3, 3, 2, 1, 1, 4, 3, 3]
x=max(set(my_list), key = my_list.count)
print(x)

List = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(List[0:3])

List = [1, 2, 3, 2, 1]

if List == List[::-1]:
    print("Palindrome hai")
else:
    print("Palindrome nahi hai")


ListA = [1, 5, 10, 20]
ListB = [6, 7, 20, 80, 100]
ListC = [3, 4, 15, 20, 30, 70, 80]
ListA = set(ListA)
ListB = set(ListB)
ListC = set(ListC)
Listd =ListA & ListB & ListC
print(Listd)

List = ["apple", "pie", "banana", "kiwi", "pear"]
k=5
for i in List:
    x = [i for i in List if len(i) >= k]
print(x)

List = [10, 20, 30, 25, 40]
List.sort()
print(List == List.sort())

Keys = ["name", "age", "city"]
Values = ["Alice", 25, "New York"]
k=dict(zip(Keys,Values))
print(k)

ListA = [1, 2, 3, 4, 5]
ListB = [2, 4, 6]
ListA = set(ListA)
ListB = set(ListB)
ListC = ListA-ListB
print(list(ListC))

List = [10, -5, 20, -1, 0, -8]
i=[i for i in List if i >= 0]
print(i)

Nested = [['apple', 'banana'], ['cherry', 'date']]
for x in Nested:
    x.append("elderberry")
print(Nested)

List1 = ["Hello ", "Take "]
List2 = ["Dear", "Sir"]
L=[x+y for x in List1 for y in List2 ]
print(L)

List2D = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
List1D = []
for i in List2D:
    List1D.extend(i)
print(List1D)

complex_list = [1, [2, [3, 4], 5], 6, [7, 8]]

result = []
stack = [complex_list]   # pura list ek item ke form me daala

while stack:
    item = stack.pop()

    if isinstance(item, list):
        stack.extend(item)   # list ko tod ke stack me daal diya
    else:
        result.append(item)

# reverse karna padega kyunki order ulta ho gaya
result.reverse()

print("Deeply Nested:", complex_list)
print("Fully Flattened:", result)

numbers = [10, 20, 30, 40]
sum = []
total = 0
for i in numbers:
    total=total+i
    sum.append(total)
print(sum)

List = [1, 2, 3, 4, 5]
k = List[2:]+List[:2]
print(k)

l= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l.split(3)
print(l)

my_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3

chunks = []

for i in range(0, len(my_data), n):
    chunks.append(my_data[i:i+n])

print("Original:", my_data)
print("Chunks:", chunks)      

List = [0, 1, 0, 3, 12]
n=[n for n in List if n != 0]
z=[n for n in List if n == 0]
l=n+z
print(l)

n = 20
i=1
while i<n:
    if i%2 != 0:
        print(i)
    i += 1

lst = [1, 2, 3]

result = [[]]

for i in lst:
    new = []
    
    for subset in result:
        new.append(subset + [i])
    
    result = result + new

print("Original:", lst)
print("Subsets:", result)
