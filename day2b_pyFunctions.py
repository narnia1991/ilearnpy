# 
# Print
# 
# We can configure the separator of the parameters

age = 30
name = "Narnia"
# this will print My name is  | Narnia |  And I am  | 30 | years old
print("My name is ", name, " And I am ", age, "years old", sep=" | ")

# this will print My name is  , Narnia ,  And I am  , 30 , years old
print("My name is ", name, " And I am ", age, "years old", sep=" , ")

# In the same way, we can configure the behavior of the line end 
# these two print function will output My name is  Narnia -  And I am  30 years old instead of two separate lines
print("My name is ", name, end=" - ")
print(" And I am ", age, "years old")

# 
# Help 
# 
# This will print the documentation of a variable or function
# help(age)

def this_func():
    pass

# this will print Help on function this_func in module __main__:
# help(this_func)


# 
# Range
# 
# Produces an Iterator. Wrap in List to have array of values

# Overloads
# range(stop_value)
# range(start_value, stop_value)
# range(start_value, stop_value, step_value)

# This Prints [0...9]
rng = range(10)
print(list(rng))

# This Prints [2...9]
rng = range(2,10)
print(list(rng))

# This Prints [2,4,6,8]
rng = range(2,10,2)
print(list(rng))


# 
# Map 
# 
# apply function to every element in an Iterable
# Produces an Iterator. Wrap in List to have array of values
strings = ["an", "apple", 'a', 'day']

lengths = map(len, strings)
# prints [2, 5, 1, 3]
print(list(lengths))

# lambda, single line anonymous function
lengths = map(lambda x: x + "-", strings)
# prints ['an-', 'apple-', 'a-', 'day-']
print(list(lengths))



# 
# Filter 
# 
# return the element if condition is fulfilled
# Produces an Iterator. Wrap in List to have array of values
def longer_than_2(string):
    return len(string) > 2

filtered = filter(longer_than_2, strings)
# prints ['apple', 'day']
print(list(filtered))



# 
# Sum 
# 
# return the sum of the Iterable object
numbers = {1,2,3,4,5,6,7}
# prints 28
print(sum(numbers))

# we can declare the starting number
# prints 38
print(sum(numbers, start=10))



# 
# Sort 
# 
people=[{
  "name": "Torey",
  "age": 70
}, {
  "name": "Lizabeth",
  "age": 95
}, {
  "name": "Sile",
  "age": 57
}, {
  "name": "Angy",
  "age": 7
}, {
  "name": "Giraldo",
  "age": 26
}]

# prints [{'name': 'Angy', 'age': 7}, {'name': 'Giraldo', 'age': 26}, {'name': 'Sile', 'age': 57}, {'name': 'Torey', 'age': 70}, {'name': 'Lizabeth', 'age': 95}]
print(sorted(people, key=lambda person: person["age"] ))



# 
# Enumerate 
# 
for index, person in enumerate(people):
    # prints 
    # 1. Torey
    # 2. Lizabeth
    # 3. Sile
    # 4. Angy
    # 5. Giraldo
    print(f"{index+1}. {person["name"]}")
    

# 
# Zip
# 
# combine iterables with ease
names=["Merilyn","Rooney","Jolee","Geordie","Lauraine"]
ages=[10,32,21,51,12]

combined = list(zip(names, ages))
# prints [('Merilyn', 10), ('Rooney', 32), ('Jolee', 21), ('Geordie', 51), ('Lauraine', 12)]
print(combined)


# 
# Open
# 
# open file and write in it
file=open("test.txt", "w")
file.write("hello world")
file.close()


# Best Practice. This will automatically close the file after the block
with open("test2.txt", "w") as file: 
    file.write("hello world2")