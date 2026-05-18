# Question 1:
# Question: Use a list comprehension to square each odd number in a list. The
# list is input by a sequence of comma-separated numbers. Suppose the
# following input is supplied to the program: 1,2,3,4,5,6,7,8,9 Then, the output
# should be: 1,3,5,7,9

k=eval(input(""))
n=[n*n for n in k if n%2 != 0]
result = ",".join([str(x) for x in n])
print(result)


# Question 2:
# Create a user define function which can calculate square value of number.
def s(n):
    s=n*n
    return(s)
print(s(9))

# Question 3:
# Define a function that can convert a integer into a string and print it in console.
def convert(num):
    s=str(num)
    print(s)

convert(45)


# Question 4:
# Define a function which can print a dictionary where the keys are numbers
# between 1 and 20 (both included) and the values are square of keys.

def square_dict():
    x={x:x*x for x in range(1,20)}
    print(x)

square_dict()

# Question 5:
# Define a function which can generate a dictionary where the keys are
# numbers between 1 and 20 (both included) and the values are square of keys.
# The function should just print the values only.

def square_dict():
    d = {x: x*x for x in range(1, 21)}
    print(d.values())
square_dict()


