q1 Expected Output: {"name": "Alice", "age": 21, "grade": "B", "city": "New York"}

dics: student = {"name": "Alice", "age": 20, "grade": "B"}
dics["age"]=21
dics.update({ "city": "New York"})
print(dics)

x= ["name", "age", "city"]
y= ["Bob", 25, "London"]
#zip se ek ek value apne sthan par achala jatat hia
print(dict(zip(x,y)))

inventory = {"apples": 10, "bananas": 5, "oranges": 8}
inventory.clear()#clear ka matlav dict empty ho jata hai
print(inventory)

dict1 = {"a": 1, "b": 2} 
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)
print(dict1)

person = {"name": "Carol", "address": {"city": "Paris", "zip": "75001"}}
city=person["address"]["city"]
print("city:",city)

student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}
history=student["grades"]["history"]
print("history grade:",history)

keys = ["math", "science", "english", "history"]
default = 0
print(dict.fromkeys(keys,default))

employee = {"fname": "John", "age": 30, "dept": "Engineering"}
# employee."full_name"
print(employee)

d=eval(input("Enter dictionary:"))
s=sum(d.values())
print("Sum= ",s)

word=input("Enter any word: ")
d={}
for x in word:
   d[x]=d.get(x,0)+1
for k,v in d.items():
  print(k,"occurred ",v," times")

n=int(input("Enter the number of students: "))
d={}
for i in range(n):
 name=input("Enter Student Name: ")
 marks=input("Enter Student Marks: ")
 d[name]=marks
 print(name,marks)

A={"a":10,"B":20,"C":30}
B={"B":5,"C":15,"D":25}
A.sum(B)
print(A)