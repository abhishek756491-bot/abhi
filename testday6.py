

Q.2 With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first
half values in one line and the last half values in one line.
t=(1,2,3,4,5,6,7,8,9,10)
k=t[0:5]
m=t[5:11]
print(k)
print(m)

q3.write a program which accepts a string as input to print "Yes" if the string is "YES" or "yes" or "Yes" otherwise print "No"

t=input("Enter yes, Yes, YES: ")
if t == "YES" or t == "yes" or t == "Yes":
    print("Yes")
else:
    print("no")

Q.4 Write a program to print the list after removing delete even numbers in
t=[5,6,77,45,22,12,24]
    odd=[]
        for i in t:
            if i%2!=0:
                odd.append(i)
        print(odd) 

Q.5  Write a program which accepts a string from user and print the
characters that have even indexes.

def even(s):
    for i in range(len(s)):
        if i%2==0:
            print(s[i])

s=input("enter your messege: ")
even(s)








       

        
    

   



   