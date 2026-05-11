#Q.1 Count total number of digits in a number

k=4587
count=0
while k>0:
    k= k//10
    count += 1
print(count)

# Q.2 Check if a number is a palindrome.
p = 12321
temp = p
n = 0

while p > 0:
    k = p % 10
    n = n * 10 + k
    p = p // 10

if n == temp:
    print("Palindrome")
else:
    print("Not Palindrome")

# Q.3 Armstrong Number Check
n = 153
temp = n
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit**3
    n = n // 10

if temp == sum:
    print("Armstrong")
else:
    print("Not Armstrong")