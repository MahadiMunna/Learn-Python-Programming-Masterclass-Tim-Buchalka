numbers=[4,5,104,105,150,172,190,195,199,200,203,250,288,293,320,350]

min_value = 100
max_value = 300

for index in range(len(numbers)-1,-1,-1):
    if numbers[index] <= min_value or numbers[index] >= max_value:
        print(index, numbers)
        del numbers[index]

print(numbers)