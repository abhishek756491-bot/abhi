# q1 (reserve1)

# a="durga"
# s=a[::-1]
# print(s)

# q2 (reverse 2)

# a="durga"
# s=''.join(reversed(a))
# print(s)

# 3 (reverse 3)
# a=input("Enter your choice ")
# r=''
# l=len(a)-1
# while l>=0:
#     r=r+a[l]
#     l -= 1
# print(r)
    
# 4 reverse order of word
# s=input("Enter your words ")
# l=s.split()
# t=[]
# n=len(l)-1
# while n >= 0:
#     t.append(l[n])
#     n -= 1
# m=' '.join(t)
# print(m)

# q4 reverse internal content of each word

# s=input("Enter a sentences ")
# s1=s.split()
# l=0
# r=[]
# while l < len(s1):
#     r.append(s1[l][::-1])
#     l += 1
# n=' '.join(r)
# print(n)

# q5 print at character at odd position  and even position for the given string

# s=input("Enter a string")
# print("even",s[0::2])
# print("odd")s[1::2]

# 2nd way
# s = "abhishek"

# i = 0

# print("Even:")

# while i < len(s):
#     if i % 2 == 0:
#         print(s[i],end=',')
#     i += 1

# i = 0
# print()
# print("Odd:")

# while i < len(s):
#     if i % 2 != 0:
#         print(s[i],end=',')
#     i += 1


#3rd way
# s = "abhishek"
# i = 0
# print("Even:")
# while i < len(s):
#     print(s[i],end=',')
#     i += 2

# print()
# i = 1
# print("Odd:")
# while i < len(s):
#     print(s[i],end=',')
#     i += 2


#merge two character in a single string
# s1=input("Enter first string :")
# s2=input("Enter second string :")
# r=''
# i=0
# while i < len(s1):
#     r=r+s1[i]
#     r=r+s2[i]
#     i += 1
# print(r)

#short number and alphabates first alphabates

s=input("Enter character ")
i=0
alpha=''
digit=''
while i < len(s):
    if s[i].isalpha():
        alpha=alpha+s[i]
    if s[i].isdigit():
        digit=digit+s[i]
    i+=1
alpha = ''.join(sorted(alpha))
digit = ''.join(sorted(digit))
print(alpha+digit)

########### in anothor way

# s=input("Enter character")
# s1=s2=output=''
# for x in s:
#     if x.isalpha():
#         s1=s1+x
#     if x.isdigit():
#         s2=s2+x
# for x in sorted(s1):
#     output += x
# for x in sorted(s2):
#     output += x
# print(output)


#question __________
# s=input("Enter character")
# n=''
# for x in s:
#     if x.isalpha():
#         n += x
#         p=x
#     else:
#         n=n+p*(int(x)-1)
# print(n)

