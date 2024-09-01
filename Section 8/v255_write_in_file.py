data = [
    "I'm Mahadi Hasan Munna",
    "My home town is Tangail"
]

file_name = '.\\Section 8\\munna_write.txt'
with open(file_name, 'w') as munna:
    for line in data:
        munna.write(line)

