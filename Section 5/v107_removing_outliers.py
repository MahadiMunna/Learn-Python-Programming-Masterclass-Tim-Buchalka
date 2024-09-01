numbers=[4,5,104,105,150,172,190,195,199,200,203,250,288,293,320,350]

min_value = 100
max_value = 300

stop=0
for index,value in enumerate(numbers):
    if numbers[index]>=min_value:
        stop = index
        break
numbers=numbers[stop:]
print(numbers)

start = 0
for value in range(len(numbers)-1, 0, -1):
    if numbers[value]<=max_value:
        start=value+1
        break

numbers=numbers[:start]
print(numbers)