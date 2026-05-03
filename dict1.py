
#Q.1 Write a Python program to add a new key-value pair to a dictionary,
#   modify an existing value, and access a specific key.
dics = {"name":"Aman","age":"22","Grade":"B"}
dics["age"]=25
dics.update({ "city": "New York"})
print(dics)

# Q.2 Write a Python program to remove a specific key from a dictionary,
# retrieve all key-value pairs, and check whether a given key exists.
car={"brand":"toyota","model":"carmy","year":2022,"colour":"blue"}
car.pop("year")
print("model Exist :","year" in car)
print("model Exist :","colour" in car)

# Q.3 Write a Python program to create a dictionary by mapping two
# equal-length  lists , one containing keys and the other containing values.
key=["name","age","city"]
value=["ravi",25,"ujjain"]
result=dict(zip(key,value))
print(result)

# Q.4 Write a Python program to remove all items from a dictionary while
# keeping the dictionary object itself intact.
fruits={"banana":100,"apple":30,"year":2022,"colour":"blue"}
fruits.clear()
print(fruits)

# Q.5  Write a Python program to combine two dictionaries into a single
# dictionary. If both dictionaries share a key, the value from the second
# dictionary should take precedence.
dict1={"a":1,"b":2}
dict2={"b":3,"c":4}
dict1.update(dict2)
print(dict1)

# Q.6 Write a Python program to retrieve a specific value from a dictionary
# that is nested inside another dictionary.
person={"name":"chetan","address":{"city":"Mumbai","Zip":"460001"}}
result=person["address"]["city"]
print("city : ",result)

# Q.7 Write a Python program to remove multiple specific keys from a
# dictionary in one operation.
p={"id":101,"name":"laptop","price":999,"stock":50,"warehouse":"A3"}
k=p.pop("stock")
l=p.popitem()
print(p)

# Q.8 Write a Python program to calculate the total of all numerical values
# stored in a dictionary.

Expenses={"rent":5000,"food":8000,"transport":400,"other":1500}
sum=0
for i in Expenses.values():
    sum=sum+i
print(sum)


# Q.9 Write a Python program to rename an existing key in a dictionary
# while preserving its associated value and the rest of the dictionary
# unchanged.
employee = {"fname":"john","age":30,"department":"Engineering"}
employee["first_name"] = employee.pop("fname")
print(employee)


# Q.10 Write a Python program to create a new dictionary containing only
# a specified subset of keys from an existing dictionary.
informantion={"id":42,"name":"abhishek","email":"abhishek7564@gmail.com","password":"Abhi@78","joined":"28-04-2004"}
informantion.popitem()
informantion.popitem()

print(informantion)