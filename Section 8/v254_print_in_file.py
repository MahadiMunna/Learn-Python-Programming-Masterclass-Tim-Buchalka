data = [
    "I'm Mahadi Hasan Munna",
    "My home town is Tangail"
]

filename = '.\\Section 8\\munna_print.txt'

with open(filename, 'w') as munna:
    for line in data:
        print(line, file=munna)

with open(filename, 'r') as munna:
    text = munna.readlines()
    print(text)