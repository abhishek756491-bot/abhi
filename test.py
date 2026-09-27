# k=4587
# count=0
# while k>0:
#     k= k//10
#     count += 1
# print("abi: ",count)

# p=12321
# temp=p
# n=0

# while p>0:
#     k=p%10
#     n=n*10+k
#     p=p//10

# if temp == n:
#     print("this is pelindrom")
# else:
#     print("not a pelindrom")

# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end=(" "))
#     print()

# for i in range(5,0,-1):
#     for j in range(0,i):
#         print("*",end=(" "))
#     print()

# l=[10,7,56,8,7,6,7,9,3,6]
# Even=[]
# Odd=[]
# for i in l:
#     if i%2 == 0:
#         Even.append(i)
#     else:
#         Odd.append(i)
# print(Even)
# print(Odd)

# words = ["apple","ball","cat","dog","papaya"]
# for word in words:
#     print(word  ,- len(word))

# x={x:x*x for x in range(1,11)}
# print(dict(x))

# for n in range(2000,3201):
#     if n%7 == 0 and n%5 != 0:
#         k=n
#         print(k,end=",")

# words = input("Enter words separated by comma: ")

# items = words.split(" ")

# items.sort()

# print("Sorted Output:")
# for i in items:
#     print(i, end=" ")


# k=eval(input(""))
# n=[n*n for n in k if n%2 != 0]
# result = ",".join([str(x) for x in n])
# print(result)

# def s(n):
#     s=n*n
#     print(s)
# s(9)

# def square_dict():
#     x={x:x*x for x in range(1,21)}
#     print(x)

# square_dict()

# t=(1,2,3,4,5,6,7,8,9,10)
# k=t[:5]
# m=t[5:]
# print(list(k))
# print(list(m))

# t = [5, 6, 77, 45, 22, 12, 24]

# new_list = []

# for i in t:
#     if i % 2 != 0:
#         new_list.append(i)

# print(new_list)
# def even(s):
#     for i in range(len(s)):
#         if i%2==0:
#             print(s[i])

# s=input("enter your messege: ")
# even(s)

# name = input("Enter name: ")
# if name == "abhi":
#     print("hello abhi")
# else:
#     print("hello guest")
# print("how are you")

# brand = input("Enter your brand")
# if brand == "killer":
#     print("killer")
# elif brand == "sparky":
#     print("sparky")
# elif brand == "lavies":
#     print("leviv 's")

# a = int(input("Enter your first number : "))
# b = int(input("Enter your second number : "))

# if a > b:
#     print("greatest number is : ",a)
# else:
#     print("greatest number is : ",b)


# a = int(input("Enter your first number : "))
# b = int(input("Enter your second number : "))
# c = int(input("Enter your Third number : "))

# if a > b > c:
#     print("greatest number is : ",a)
# elif b > c:
#     print("greatest number is : ",b)
# else:
#     print("greatest number is : ",c)

# a = int(input("Enter a number"))
# sum = 0
# for x in range(a+1):
#     sum=sum+x
# print(sum)

# a = 1
# while a <= 10:
#     print(a)
#     a += 1

# a = ''
# while a!="abhi":
#     a = input("Enter name : ")
# print("right")

# for i in range(7):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# for i in range(6,12):
#     for j in range(i+7):
#         print("*",end=" ")
#     print()


for i in range(5,0,-1): 
    for j in range(i):
        print(i,end=' ')    
    print() 
    
    
    