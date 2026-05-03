#Q.1(a) Write a Python program to find the factorial of any number.
n=int(input("Enter any numner: "))
p=1
for i in range(1,n+1):
    p=p*i
    print(p)


# Q.1(b)Write a Python program to count the total number of digits in a number
n = int(input("Enter your choice number: "))
count = 0
while n > 0: 
    count = count + 1
    n = n // 10 
print(count) 

# Q.2(a)Write a program that prompts the user to enter their age and prints the corresponding age
# group. The program should use the following age groups:
age=int(input("Enter your age: "))

if age>=0 and age<=12:
    print("Child")
elif age<=19:
    print("Teenager")
elif age<=59:
    print("Adult")
elif age>=60:
    print("Sinior citizen")
else:
    print("Invalid ")

# Q.2(b)Write a program to count occurrences of all characters within a string
abhi="apple"
counts={}
for i in abhi:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1
print(counts)

# Q.3(a) Write a program to print the following pattern
a=65
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(chr(a),end=" ")
        a=a+1
    print()

#Q.3(b) Write a program to check whether a number is prime or not,using user define function.
n=int(input("Enter number: "))
if n>1:
    for i in range(2,n):
        if (n%i)==0:
            print(n,"is not prime")
            break
    else:
        print(n,"is prime")
else:
    print(n,"is not prime")

# Q.4(a)Count and print how many times football; appears in list.
sport=["cricket","football","tennis","football","hockey"]
count=0
for i in range(len(sport)):
    if sport[i] == "football":
        count += 1
print("football is ",count,"times in sports")

# Q.4(b)Find and print the largest and smallest number in a list [8, 2, 15, 1, 9] without using max(),min()
# and sort().
listt=[8,2,15,15,1,9]
k=listt[0]
for i in range(len(listt)):
    if listt[i] > k:
        k=listt[i]
print("large num is ",k)
for i in range(len(listt)):
    if listt[i] < k:
        k=listt[i]
print("small num is ",k)

# Q.5(a)Write a code to print the key of a minimum value from the following dictionary.
marks={"math":89,"phy":80,"chem":67,"eng":75}
k=min(marks)
print(k)

# Q.5(b)Find Common Elements in Two Lists.
list1=[10,20,30,40]
list2=[30,40,50,60]
p=set(list1).intersection(set(list2))
print(p)