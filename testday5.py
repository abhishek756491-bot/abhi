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
# def s(n):
#     s=n*n
#     return(s)

# Question 3:
# Define a function that can convert a integer into a string and print it in console.



def diction():
