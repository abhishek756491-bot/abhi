#Python program to interchange first and last elements in a list.
list1=[10,20,30,40,50]
list1[0],list1[4]=list1[4],list1[0]
print(list1)

#Given a list, our task is to check if an element exists in it.
list2 = [10, 20, 30, 40, 50]
element = 30
if element in list2:
    print("Element exists in the list")
else:
    print("Element does not exist in the list")

#check largest number
list3=[10, 24, 76, 23, 12]
l=list3[0]
for i in list3:
    if i>l:
       l=i
print(l)
   
#Given a list of numbers, the task is to find the smallest number in the list. For Example:
list4=[10, 24, 76, 2, 12]
l=list3[0]
for i in list3:
    if i<l:
       l=i
print(l)

#Given a list of numbers, the task is to print all positive numbers in the list. A positive number is any number greater than 0.
list5 = [-10, 15, 0, 20, -5, 30, -2]
l=[]
for i in list5:
   if i>0:
    l.append(i)
print(l)

#Find Sum and Average of List in Python
list6 = [10, 20, 30, 40, 50]
sum=0
for i in list6:
    sum=sum+i
    avg=sum/len(list6)
print(sum)
print(avg)