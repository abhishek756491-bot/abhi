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




