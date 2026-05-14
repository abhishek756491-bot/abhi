#Name = Abhishek kumar
# batch=py builder 3

#Q.1 W.A.P to print the fibonaaci series using for loop
n = 10

a = 0
b = 1

print(a, b, end=" ")

for i in range(2, n):
    c = a + b
    print(c, end=" ")
    a = b
    b = c

# Q.2 W.A.P. to find the second highest number in a list.
lst = [10, 45, 67, 89, 23, 89]

largest = max(lst)

lst.remove(largest)

second_highest = max(lst)

print("Second Highest Number =", second_highest)

# Q.3 W.A.P. to display unique value in a tuple.
t = (1, 2, 3, 2, 4, 5, 1, 6)

unique = set(t)

print("Unique values =", unique)

# Q.4 W.A.P. to find square root of any number without using predefined function
n = 25

i = 1

while i * i <= n:
    if i * i == n:
        print("Square Root =", i)
    i += 1

# Q.5 W.A.P.  to find the sum of prime number in a list.
lst = [2, 3, 4, 5, 6, 7, 11]

sum = 0

for num in lst:
    prime = True

    if num < 2:
        prime = False

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        sum = sum + num

print("Sum of prime numbers =", sum)