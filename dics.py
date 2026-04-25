#q1 Expected Output: {"name": "Alice", "age": 21, "grade": "B", "city": "New York"}

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
employee."full_name"
print(employee)