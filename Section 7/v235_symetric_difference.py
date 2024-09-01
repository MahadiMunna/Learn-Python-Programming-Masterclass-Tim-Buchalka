number1 = {1,2,5,6,7,9}
number2 = {3,4,5,6,8,9}

symetric_difference = number1 ^ number2 #it collects unique values between sets
print(symetric_difference)

number1 = [1,2,5,6,7,9]
number2 = [3,4,5,6,8,9]

symetric_difference = set(number1).symmetric_difference(number2)
print(symetric_difference)