k=4587
count=0
while k>0:
    k= k//10
    count += 1
print("abi: ",count)

p=12321
temp=p
n=0

while p>0:
    k=p%10
    n=n*10+k
    p=p//10

if temp == n:
    print("this is pelindrom")
else:
    print("not a pelindrom")

for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=(" "))
    print()

for i in range(5,0,-1):
    for j in range(0,i):
        print("*",end=(" "))
    print()

l=[10,7,56,8,7,6,7,9,3,6]
Even=[]
Odd=[]
for i in l:
    if i%2 == 0:
        Even.append(i)
    else:
        Odd.append(i)
print(Even)
print(Odd)

words = ["apple","ball","cat","dog","papaya"]
for word in words:
    print(word  ,- len(word))

x={x:x*x for x in range(1,11)}
print(dict(x))

