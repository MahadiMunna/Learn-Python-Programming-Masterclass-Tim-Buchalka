numbers = "9,123;253:194 324,399;500:778"
seperators = ""
for char in numbers:
    if not char.isnumeric():
        seperators += char

print (seperators)
values = "".join(char if char not in seperators else " " for char in numbers).split()
print([int (val) for val in values])