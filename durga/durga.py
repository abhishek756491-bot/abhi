q1 (reserve1)

a="durga"
s=a[::-1]
print(s)

q2 (reverse 2)

a="durga"
s=''.join(reversed(a))
print(s)

3 (reverse 3)
a=input("Enter your choice ")
r=''
l=len(a)-1
while l>=0:
    r=r+a[l]
    l -= 1
print(r)
    
4 reverse order of word
s=input("Enter your words ")
l=s.split()
t=[]
n=len(l)-1
while n >= 0:
    t.append(l[n])
    n -= 1
m=' '.join(t)
print(m)

q4 reverse internal content of each word

s=input("Enter a sentences ")
s1=s.split()
l=0
r=[]
while l < len(s1):
    r.append(s1[l][::-1])
    l += 1
n=' '.join(r)
print(n)

q5 print at character at odd position  and even position for the given string

s=input("Enter a string")
print("even",s[0::2])
print("odd")s[1::2]

2nd way
s= input("Enter a string")
