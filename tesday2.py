# Define the range
a = 1
b = 10

for i in range(a, b + 1):
    for j in range(a, b + 1):
        product = i * j
        print(product, end=" ")
    print()

# Q.2 Print a downward half-pyramid pattern using stars (*)
r = 5

for i in range(r, 0, -1):
    
    for j in range(0, i):
        print("*", end=" ")

    print()

#Q.3 Start with a list of 10 numbers. Iterate through them and sort them
#into two separate lists: one for even numbers and one for odd numbers.
numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]


even = []
odd = []


for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)


print("Even numbers:", even)
print("Odd numbers:", odd)


# Q.4  Create a list of 5 words. Write a loop that iterates through the list
# and prints each word alongside its character count.
squares_dict = {}

for i in range(1, 11):
    squares_dict[i] = i * i

print(squares_dict)



#Q.5 Create a dictionary where the keys are numbers from 1 to 10 and the
# values are the squares of those numbers.
user = input("Enter a sentence: ")


sentence = user.replace(" ", "_")


print(sentence)

# Q.6 Ask the user for a sentence. Replace every empty space in that
# sentence with an underscore (_) and print the final result.

words = input("Enter a sentenses")

for word in words:
    
    print(f"{word} - {len(word)}", end=" ")
