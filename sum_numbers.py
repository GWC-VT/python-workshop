# prints the sum of number up to num
def sum_numbers(num):
    x = 1
    total = 0
    while x <= num:
        total = total + x
        x = x + 1
    print(total)


number = input("Please input a number: ")
sum_numbers(int(number))

# suggestions

# test it and see if it's producing correct results
# try to modify it to take a user input for num
# try writing a method to calculate factorials, which are a similar process
