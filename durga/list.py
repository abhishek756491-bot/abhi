list = []
print(type(list))

dyanamic input
list = eval(input("Enter input list: "))
print(list)
print(type(list))

list function
l=list(range(0,10,2))
print(l)
print(type(l))

#with split function
s="Learning python is very very easy !!!"
l=s.split()
print(l)
print(type(l))

start here for questiion from py native
1.
numbers = [2, 3, 5, 7]
print("third element - ",numbers[2])
print("length of list - ",len(numbers))
print("is list is emplty ? - ",[] in numbers)

2
numbers[1]=200
numbers.append(600)
numbers.insert(2,300)
numbers.pop()
numbers.pop(0)
print(numbers)

3
sum=0
l=len(numbers)
for x in numbers:
    sum=sum+x
    avg=sum/l
print("sum is : ",sum)
print("avg is : ",avg)

4
max=numbers[0]
min=numbers[0]
for x in numbers:
    if max < x:
        max=x
    if min > x:
        min=x
print(max)
print(min)

5
p=1
for x in numbers:
    p=p*x
print(p)

6
odd=0
even=0
for x in numbers:
    if x%2 == 0:
        even += 1
    else:
        odd += 1
print("even number in list : ",even)
print("odd number in list : ",odd)

7
print("reverse list is :",numbers[::-1])

8
l = [56, 12, 89, 3, 22]
l.sort()
print(l)

9
m=l.copy()
print(m)

10
c=l+m
print(c)

11
print(l[1:4])

12
l[0],l[2]=l[2],l[0]
print(l)

13
nlist=[[1, 2], [3, 4, 5], [6, 7]]
print(nlist[1][2])

14
l=["Laptop", "Mouse", "Monitor", "Keyboard"]
print("Laptop" in l)

15 longest string
large_str = l[0]
for x in l:
    if len(large_str) < len(x):
        large_str = x
print(large_str)

16
l= [1, 2, 3, 4, 5]
s=[i*i for i in l]
print(s)

17
a=[10, 20, 30, 10, 40, 10, 50]
print(a.count(10))

18
l=[x for x in a if x != 10]
print(l)

19
b=["Mike", "", "Emma", "Kelly", "", "Brad"]
r=[x for x in b if x != ""]
print(r)

20
duplicates = [10, 20, 10, 30, 40, 40, 20, 50]
u=set(duplicates)
unique=list(u)
print(unique)

21
mix=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even=[x for x in mix if x%2 == 0]
print(even)

22
l1=["Py", "is", "awes"]
l2=["thon", " ", "ome"]
l3=[]
for x,y in zip(l1,l2):
   l3.append(x+y)
print(l3)

23
List1= [10, 20, 30]
List2= [100, 200, 300]
for x,y in zip(List1,List2):
    print(x,y)

24
l=[10, 20, 30,30,30,30, 40, 50,30]
l.insert(3,35)
print(l)

25
l.remove(30)
l.insert(2,300)
print(l)

27
l=list(set(l))
l.sort()
print(l[-2])

28
def find_mode(numbers):
    if not numbers:
        return None

    # सबसे ज़्यादा बार आने वाला नंबर और उसकी गिनती को ट्रैक करने के लिए
    max_count = 0
    mode = numbers[0]

    # लिस्ट के हर नंबर को जांचें
    for num in numbers:
        # .count() फ़ंक्शन से पता चलेगा कि वह नंबर लिस्ट में कितनी बार है
        count = numbers.count(num)
        
        # अगर मौजूदा नंबर की गिनती पहले वाले से ज़्यादा है, तो इसे बदल दें
        if count > max_count:
            max_count = count
            mode = num

    return mode

# चलाकर देखने के लिए उदाहरण:
sample_list = [1, 3, 3, 3, 2, 2, 1, 4]
print("बहुलक (Mode) है:", find_mode(sample_list))

another way
आपकी लिस्ट (यहाँ अपनी लिस्ट बदल सकते हैं)
numbers = [1, 3, 3, 3, 2, 2, 1, 4, 3, 2]

# बहुलक (Mode) निकालने की सबसे सरल लाइन
mode = max(set(numbers), key=numbers.count)

# उत्तर प्रिंट करें
print("बहुलक (Mode) है:", mode)

29
def fun(l,n):
    return l[::3]

l=['a','b','c','d','e','f','g']
n=3
print(fun(l,n))

30
def pelindrom(lst):
    return lst == lst[::-1]

lst=[1, 5, 3, 2, 1]
print(pelindrom(lst))

31
l1=[1, 5, 10, 20]
l2=[6, 7, 20, 80, 100]
l3=[3, 4, 15, 20, 30, 70, 80]
l4=[]
for x in l1:
    for y in l2:
        for z in l3:
            if x == y == z:
                l4.append(x)
print(l4)

32
def filt(l,k):
    result=[]
    for x in l:
        if len(x) >= k:
            result.append(x)
            return result
l=["apple", "pie", "banana", "kiwi", "pear"]
k=5
print(filt(l,k))

33
def sort(lst):
    return lst == sorted(lst)

l1=[1, 5, 10, 20]
print(sort(l1))

34
Keys= ["name", "age", "city"]
Values= ["Alice", 25, "New York"]
d=dict(zip(Keys,Values))
print(d)

34
l1=[1, 2, 3, 4, 5]
l2=[2, 4, 6]
l=l1 - l2
print(l)


35
l=[10, -5, 20, -1, 0, -8]
m=[]
for x in l:
    if x >= 0:
        m.append(x)
print(m)

36
def ext(l, item):
    for x in l:
        x.append(item)
    return l

m = [['apple', 'banana'], ['cherry', 'date']]
item = "abhi"
print(ext(m, item))

37
l1=["Hello ", "Take "]
l2=["Dear", "Sir"]
l3=[]
for x in l1:
    for y in l2: 
        l3.append(x+y)
print(l3)

38
l=[[1, 2, 3], [4, 5], [6, 7, 8, 9]]
k=[]
for x in l:
    for i in x:
        k.append(i)
print(k)

39
nested = [1, [2, 3], [4, [5, [6, 7]]]]
k = []
def flatten(data):
    for x in data:
        if isinstance(x, list):
            flatten(x)  # अगर टुपल है, तो फंक्शन खुद को दोबारा चलाएगा
        else:
            k.append(x)  # अगर नंबर है, तो लिस्ट में जोड़ देगा
print(k)


