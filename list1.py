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