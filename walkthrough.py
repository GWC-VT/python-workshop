# basic printing, variables, data types

print("hello world")
message = "hello world"    # str
print(message)
message = 12    # int
print(message)
message = True    # bool
print(message)

print(type(message))    # tells you what type your variable is

# math operations

print(1 + 1)
print(2 * 3)
print(7 / 2) # regular division
print(7 // 2) # integer division

# equals

x = 1    # assigns a value to a variable
y = 2
print(x == y)    # returns a boolean (is this statement true or false)


# lists

my_list = ["cat", "dog", "fish"]
print(my_list)
my_list.append("horse")
print(my_list)
my_list.remove("cat")
print(my_list)

# while loop

x = 0
while x < 3:
    print(x)
    x = x + 1

# for loop with list

for word in my_list:
    print(word)     # prints each word from the list on its own line

# for loop with range

for x in range(5):  # range is from 0 to 4
    print(x)

# here's one that's a little more interesting

for x in range(5):
    print("?" * x)    # you can repeat characters using multiplication


# now let's define this process as a function

def triangle():    # this alone does not run because we haven't called it
    for x in range(5):
        print("?" * x)


triangle()    # this is the function call

# now let's add parameters


def triangle_params(num):
    for x in range(num):
        print("?" * x)


# now when we call triangle_params, we can tell it how big to make the triangle

triangle_params(10)

number = input("please enter a number: ")    # asks the user for input
triangle_params(int(number))    # the input is assumed to be a string, so we have to turn it into an int
