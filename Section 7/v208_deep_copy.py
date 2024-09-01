import copy
numbers = {
    1:["O",'N',"E"],
    2:["T","W","O"],
    3:["T","H","R","E"],
}
# Shallow copy
# new_numbers = numbers.copy()
# new_numbers[3].append("E")
# print(new_numbers[3])
# print(numbers[3])
## same output
# ['T', 'H', 'R', 'E', 'E']
# ['T', 'H', 'R', 'E', 'E']

#Deep copy
new_numbers = copy.deepcopy(numbers)
new_numbers[3].append("E")
print(new_numbers[3])
print(numbers[3])
## Different output
# ['T', 'H', 'R', 'E', 'E']
# ['T', 'H', 'R', 'E']

