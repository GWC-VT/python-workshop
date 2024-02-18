
# basic printing, variables, data types


print("hello world")
message = "hello world"    # str
print(message)
message = 12    # int
print(message)
message = True    # bool
print(message)


# math operations


print(1 + 1)
print(2 * 3)
print(7 / 2) # regular division
print(7 // 2) # integer division
print(2 ^3)


# equals


x = 1
y = 2
print(x == y)    # returns a boolean


# lists
# explain that a list is also a variable
# it's an object so it comes with pre defined functions (append)


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
# explain meaningful indentation


for word in my_list:
    print(word)     # prints each word from the list on its own line


# for loop with range

for x in range(5):  # range is from 0 to 4
    print(x)


# here's one that's a little more interesting

for x in range(5):
    print("?" * x)


# now let's define this process as a function

def triangle():
    for x in range(5):
        print("?" * x)


triangle()


# now let's add parameters


def triangle_params(num):
    for x in range(num):
        print("?" * x)


# now when we call triangle_params, we can tell it how big to make the triangle


triangle_params(10)