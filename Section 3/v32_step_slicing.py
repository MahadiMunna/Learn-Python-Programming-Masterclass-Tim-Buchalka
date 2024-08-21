numbers = "9,223;372 036,037:854;775'807"
seperators = numbers[1::4]
print(seperators) 

values = "".join(char if char not in seperators else " " for char in numbers).split()
print([int (val) for val in values])

#############################
##### Need to Breakdown #####
#############################