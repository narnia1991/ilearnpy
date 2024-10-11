# immutability
# str, int, float, bool, bytes, tuple (x,y)
# mutable
# list, set, dict


# Immutable example: 
x = (1, 2)
# this creates a copy of tuple (1, 2) since it's immutable
y = x

# x[0] = 1 this will error since tuple is not mutable
x = (1, 2, 3)
# prints (1, 2, 3) (1, 2)
print(x, y)


# Mutable example: 
x = [1, 2]
# this creates a copy of the reference to [1,2]
y = x

# x[0] = 1 this will error since tuple is not mutable
x[0] = 100
#  prints [100, 2] [100, 2]
print(x, y)

x = (1,2,3)
# prints (1, 2, 3) [100, 2], x is reassigned but y remains the same
print(x, y)


# 
# List Comprehension
# 

x = [i for i in range(10)]
# prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x)
x = [i for i in range(10) if i % 2 == 0]
# prints [0, 2, 4, 6, 8]
print(x)


# 
# Function Argument and Parameters
# 

def this_function(x, y):
    print(x,y)
    pass

#  you can pass the params as named or not
this_function(y=2, x=1)
# prints 1 2

this_function(2,1)
# prints 2 1


def that_function(x, y, z):
    print(x,y)
    pass

# you can pass mixed named and unnamed args 
# caveat you need to pass positional args before keyword/named args 
# that_function(z=2,1,y=3) will throw an error
that_function(1, z=2, y=3)
# prints 1 3

# Otional parameters, you can declare optional parameters by providing default value
def optional_function(x, y, z=None):
    print(x,y,z)
    pass
# this will not throw an error since z is optional
optional_function(1, 2)

def args_function(*args, **kwargs):
    print(args, kwargs)
    pass

# args accept any number of positional arguments which is stored in a tuple
# kwargs accepts anynumber of keyword arguments which is stored in a dictionary
args_function(1,2,3,x=10, y=20)
# prints (1, 2, 3) {'x': 10, 'y': 20}

# we can also pass array with * to break down positional arguments
# pass dictionary with ** to break down named arguments
def breakdown_function(a,b, c=True, d=False):
    print(a, b, c, d)
    pass

#  prints 1 2 watta nice
breakdown_function(*[1,2], **{"c":"watta", "d":"nice"})


# anything below this function will only run if we are running the script from this file
# if we are referencing this file from another module, it will not print this
if __name__ == "__main__":
    print("my spot")