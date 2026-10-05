1
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
fruits.remove("apple")
print(fruits)
fruits.discard("banana")
print(fruits)

2
colors = {"red", "green", "blue"}
colors.clear()
print(colors)

3
animals = {"cat", "dog", "bird", "fish"}
print(len(animals))

4
data = set()

if not data:
    print("The set is empty.")
else:
    print("The set is not empty.")

5
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
# set_c = set_a.union(set_b)
set_c = set_a | set_b
print(set_c)

6
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
# set_c = set_a.intersection(set_b)
set_c = set_a & set_b
print(set_c)

7
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
# set_c = set_a.difference(set_b)
set_c = set_a-set_b
print(set_c)

8
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_c = set_a.symmetric_difference(set_b)
print(set_c)

9
numbers = {42, 7, 19, 85, 3, 56}
maximum=max(numbers)
print(maximum)
minimum=min(numbers)
print(minimum)

10
numbers = {42, 7, 19, 85, 3, 56}
addition=sum(numbers)
print(addition)

11
fruits = {"apple", "banana"}
new_fruits = ["cherry", "mango", "apple"]
fruits.update(new_fruits)
print(fruits)

12
base = {1, 2}
from_list = [3, 4]
from_tuple = (5, 6)
from_set = {7, 8}
base.update(from_list,from_tuple,from_set)
print(base)


14
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
print("subset or not ",set_a.issubset(set_b))
print("subset or not ",set_b.issuperset(set_a))

15
set_a = {1, 2, 3}
set_b = {4, 5, 6}
print("disjoint or not:",set_a.isdisjoint(set_b))
set_c = {1,4,2}
print("disjoint or not:",set_a.isdisjoint(set_c))

16
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

a.difference_update(b)

print("a =", a)

17
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
a.intersection_update(b)
print(a)

18
a.symmetric_difference_update(b)
print(a)

19
items = {10, 20, 30, 40, 50, 60}
to_remove = {20, 40, 60}
items.difference_update(to_remove)
print(items)

20
s = {100, 200, 300}
popped = s.pop()
print("Popped:", popped)

s = set()
try:
    s.pop()
except KeyError as e:
    print("Error:", e)

20
numbers = {1, 2, 3, 6, 7, 9, 12, 14, 15}
divisible_by_3 ={x for x in numbers if x%3 == 0}
print("divisible_by_3:",divisible_by_3)

21
list1 = [1, 2, 3, 4, 5, 3, 2]
list2 = [3, 4, 5, 6, 7, 4, 5]
list1_set = set(list1)
list2_set = set(list2)

print(list1_set & list2_set)

22
text = "the cat sat on the mat the cat"
l=text.split()
print(set(l))

23
tags = {"python", "set", "programming", "tutorial"}
string = " | ".join(sorted(tags))
print(string)

24
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
print("is this subset:",a.issubset(b))
print("is this superset:",b.issuperset(a))

25
fs = frozenset([1, 2, 3, 4, 5])

print("frozenset:", fs)
print("Intersection with {3, 4, 5, 6}:", fs.intersection({3, 4, 5, 6}))

try:
    fs.add(6)
except AttributeError as e:
    print("Error:", e)

26
conprehension={x*x for x in range(2,22,2)}
print(sorted(conprehension))

27
items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# k=set()
n=[]
for item in items:
    if item not in n:
        n.append(item)
        # k.add(item)
print(n)
# print(k)

28
A = {1, 2, 3, 4, 5, 6, 7, 8}
B = {2, 4, 6}
C = {5, 7, 9}
d = A.difference(B, C)
print(d)

29
# 1. यह दिखाने के लिए सेट बनाना कि यह टुपल को स्टोर कर सकता है
try:
    my_tuple = (1, 2, 3)
    my_set = {my_tuple, "apple", "banana"}
    print("सफलता! सेट में टुपल स्टोर हो गया:", my_set)
except TypeError as e:
    print("टुपल स्टोर करने में एरर आई:", e)

print("-" * 50)

# 2. यह दिखाने की कोशिश करना कि सेट में लिस्ट स्टोर नहीं हो सकती
try:
    my_list = [4, 5, 6]
    # यहाँ एरर आएगी
    wrong_set = {my_list, "cherry"} 
except TypeError as e:
    print("फेल! सेट में लिस्ट स्टोर नहीं हो सकी।")
    print("एरर का कारण (Error Message):", e)


30

Assignment: both names point to the same set object
ref = original
ref.add(99)
print("--- Assignment (=) ---")
print("original:", original)
print("ref:", ref)

# Reset
original = {1, 2, 3, 4, 5}

# Shallow copy: independent object
copied = original.copy()
copied.add(42)
print("\n--- Shallow copy (.copy()) ---")
print("original:", original)
print("copied:", copied)

import calendar
print(calendar.calendar(2026))

31

import time

large_list = list(range(1_000_000))
large_set = set(range(1_000_000))
target = 999999

start = time.time()
result = target in large_list
list_time = time.time() - start

start = time.time()
result = target in large_set
set_time = time.time() - start

print(f"List lookup time:  {list_time:.6f} seconds")
print(f"Set lookup time:   {set_time:.6f} seconds")