d = {
    1:"One",
    2:"Two",
    3:"Three",
    4:"Four",
    5:"Five",
    6:"Six",
    7:"Seven",
    8:"Eight",
    9:"Nine"
}

numbers = ["one", "two", "three", "four", "five", "six"]

new_dict = dict.fromkeys(numbers, 0)
print(new_dict)

# keys = d.keys()
# print(keys)
# for key in d.keys():
#     print(key)

## Video 203 "the `update` method"
d2 = {
    3:"The new three",
    7:"Lucky seven",
    10:"ten"
}
d.update(d2)

# for key, value in d.items():
#     print(f'{key:<2} {value}')


d.update(enumerate(numbers))
for key, value in d.items():
    print(f'{key:<2} {value}')

# video 204 "The 'value' method"

v = d.values()
print(v)
d[0] = "Zero"
for value in d.values():
    print(value)