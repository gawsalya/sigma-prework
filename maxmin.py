# create function to sort list and then return highest and lowest numbers
def sorter_func(input):
    input.sort()
    return [input[0], input[len(input) - 1]]

# testing input areas
input = [2, 4, 1, 0, 2, -1]
# print answer
print(sorter_func(input))