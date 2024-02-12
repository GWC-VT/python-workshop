# prints the sum of numbers from 1 to num

my_num = 10  # change this to whatever number you want
curr_num = 1  # starts at 1, adds 1 to the total, then becomes 2, adds 2 to the total, and so on
total = 0  # keeps track of the sum

while curr_num <= my_num:
    total = total + curr_num
    curr_num = curr_num + 1
print(total)

# suggestions

# test it and see if it's producing correct results--try manually printing out the sum to see if the answers match!
# try to modify it to take a user input for num
# try writing a method to calculate factorials, which are a similar process
