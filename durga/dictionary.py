 s=input("Enter word: ")
 d={}
 for x in s:
     d[x]=d.get(x,0)+1
 for k,v in d.items():
     print(k,"occured",v,"times")

 #another way with 
 s=input("Enter word: ")
 def occured(word):
     d={}
     for x in word:
         d[x]=d.get(x,0)+1
     for k,v in d.items():
         return d
 print(occured(s))

 vowel occurance


 word=input("inter word: ")
 v={"a","e","i","o","u"}
 d={}
 for x in word:
     if x in v:
         d[x]=d.get(x,0)+1
 for x,y in sorted(d.items()):
     print(x,"---",y)

 3Q.  Write a program to accept student name and marks from the keyboard 
 and creates a dictionary. Also display student marks by taking student name 
 as input? 

 n=int(input("Enter number of students: "))
 d={}
 i=1
 for x in range(n):
     name=input("name: ")
     marks=input("marks: ")
     d[name]=marks
 while True:
     name=input("Enter name for seach marks : ")
     marks=d.get(name,-1)
     if marks == -1:
         print("student not found")
     else:
         print("the name of student is ",name,"and marks is ",marks)
     option=("what do you want to another student search[YES|NO]")
   
     if option == "NO":
         break
 print("thank you for searching with me")

q1
 d={"name":"abhishek","age":24,"city":"muzaffarpur"}
 d["roll"]=89
 print(d)
 print("name",d["name"])

q2
 car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}
 remove=car.pop("brand")
 print(remove)
 print(car)
 print("brand" in car)
 print(car.items())

q3
 keys = ["name", "age", "city"]
 values = ["Bob", 25, "London"]
 d=dict(zip(keys,values))
 print(d)

q4
 car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}
 car.clear()
 print(car)

q5
 dict1 = {"a": 1, "b": 2}
 dict2 = {"b": 3, "c": 4}
 dict1.update(dict2)
 print(dict1)

q6
 person = {"name": "Carol", "address": {"city": "Paris", "zip": "75001"}}
 print("city",person["address"]["city"])

7
 student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}
 print("history Grade : ",student["grades"]["history"])

8
 keys = ["math", "science", "english", "history"]
 default = 0
 d={x:default for x in keys}
 print(d)

!!
 keys = ["math", "science", "english", "history"]
 default = 0

 scores = dict.fromkeys(keys, default)

9
 employee = {"fname": "John", "age": 30, "dept": "Engineering"}
 employee["first_name"] = employee.pop("fname")
 print(employee)

10
 product = {"id": 101, "name": "Laptop", "price": 999, "stock": 50, "warehouse": "A3"}
 product.pop("stock")
 product.pop("warehouse")
 print(product)

11
 roles = {"alice": "admin", "bob": "editor", "carol": "viewer"}
 print("admin exists in roles : ","admin" in roles.values())
 print("abhishek exists in roles : ","abhishek" in roles.values())

12
 expenses = {"rent": 1200, "food": 300, "transport": 150, "utilities": 200}
 s=sum(expenses.values())
 print("sum of total value of dictionary : ",s)

13
 user = {"id": 42, "username": "jdoe", "email": "jdoe@example.com", "password": "s3cr3t", "joined": "2021-03-15"}
 extract = ["id", "username", "email"]
 new_user = {}
 for key in extract:
     if key in user:
         new_user[key] = user[key]
 print(new_user)

14
 attributes = ["brand", "model", "year", "color"]
 details = ["Honda", "Civic", 2023, "silver"]
 car=dict(zip(attributes,details))
 print(car)

15
 text = "hello world"
 d={x:(text.count(x))  for x in text }
 print(d)

16
 company = {"name": "TechCorp", "location": {"city": "Berlin", "country": "Germany"}}
 company["location"]["city"]="mulich"
 print(company)

17
 data = {"school": {"department": {"class": {"teacher": "Mr. Smith", "students": 30}}}}
 data["school"]["department"]["class"]["students"] = 35
 print(data)

18
 Numbers 1 through 10 (generated with range())
 square={x:x*x for x in range(1,11)}
 print(square)

19
 scores = {"Alice": 82, "Bob": 45, "Carol": 91, "Dave": 58, "Eve": 73} 
 result={x:y for x,y in scores.items() if y >= 60}
 print(result)


20
 stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}
 # lowest_stock = {x for x,y in stock.items() if y == min(stock.values())}
 lowest = min(stock, key=stock.get)
 print(lowest_stock)

21
 scores = {"Alice": 88, "Bob": 95, "Carol": 72, "Dave": 95, "Eve": 84}
 high = {x for x,y in scores.items() if y == max(scores.values())}
 lowest_stock = max(scores,key=scores.get)
 print(high)
 print(lowest_stock)

22
 pairs = [("name", "Alice"), ("age", 25), ("city", "Paris")]
 d=dict(pairs)
 print(d)

23
1 = {"a": 1, "b": 2, "c": 3}
2 = {"b": 20, "c": 30, "d": 40}
ommon_keys = d1.keys() & d2.keys()
rint("Common keys:", common_keys)

24
 d1 = {"a": 1, "b": 2, "c": 3}
 d2 = {"b": 20, "d": 40}
 difference=d1.keys() - d2.keys()
 print(difference)

25
 d1 = {"a": 1, "b": 2, "c": 3}
 d2 = {"a": 1, "b": 99, "c": 3}
 d=d1.items() & d2.items()
 print(d)

26
 text = "the cat sat on the mat the cat"

 word_count = {}
 for word in text.lower().split():
     word_count[word] = word_count.get(word, 0) + 1

 print(word_count)

27
 data = {"name": "Alice", "age": None, "city": "Paris", "score": None}
 data = {x: y for x, y in data.items() if y is not None}
 print(data)

28
 data = {"banana": 3, "apple": 5, "cherry": 1, "date": 4}
 d=sorted(data)
 print(d)

29
 scores = {"Alice": 88, "Bob": 72, "Charlie": 95, "Diana": 60}

 sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1]))

 print(sorted_scores)


