fruits = {"apple", "banana", "cherry"}
fruits.add("mango")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.discard("app")# agar elememnt absent hai to error nahio dikhata hai
print(fruits)

colors = {"red", "green", "blue"}
colors.clear()
print(colors)

animals = {"cat", "dog", "bird", "fish"}
print(len(animals))

data = set()
if not data:
    print("The set is empty.")
else:
    print("The set is not empty.")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
s=set_a.union(set_b)
print(s)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
s=set_a.intersection(set_b)
print(s)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
s=set_a.difference(set_b)
print(s)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
s=set_a.symmetric_difference(set_b)
print(s)

numbers = {42, 7, 19, 85, 3, 56}

max_num = 0
min_num = 999

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print("Max:", max_num)
print("Min:", min_num)

numbers = {10, 20, 30, 40, 50}
s=0
for x in numbers:
    s += x
print(s)

fruits = {"apple", "banana"}
new_fruits = ["cherry", "mango", "apple"]
fruits.update(new_fruits)
print(fruits)

base = {1, 2}
List = [3, 4]
Tuple = (5, 6)
Set = {7, 8}
base.update(List,Tuple,Set)
print(base)

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}

print("Is set_a a subset of set_b?", set_a.issubset(set_b))
print("Is set_b a superset of set_a?", set_b.issuperset(set_a))

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
k=a.difference(b)
print(k)

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
k=a.intersection(b)
print(k)

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
k=a.symmetric_difference(b)
print(k)

items = {10, 20, 30, 40, 50, 60}
Remove = {20, 40, 60}
print(items.difference(Remove))

s = {100, 200, 300}
popped = s.pop()
print("Popped:", popped)

s = set()
try:
    s.pop()
except KeyError as e:
    print("Error:", e)

numbers = {1, 2, 3, 6, 7, 9, 12, 14, 15}
m={x for x in numbers if x % 3 == 0}
print(m)

list1 = [1, 2, 3, 4, 5, 3, 2]
list2 = [3, 4, 5, 6, 7, 4, 5]
list1 =set(list1)
list2 =set(list2)
k=list1.intersection(list2)
print(k)\

text = "the cat sat on the mat the cat"
t= text.split()
tu=set(t)
print(len(tu))

tags = {"python", "set", "programming", "tutorial"}
k=" | ".join(sorted(tags))
print(k)


x ={x*x for x in range(2,21,2)}
print(sorted(x))

items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
items = set(items)
print(list(items))