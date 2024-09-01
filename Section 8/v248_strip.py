file_path = '.\\Section 8\\munna.txt'

with open(file_path) as munna:
    first = munna.readline()

print(first)

chars = "munn"
new_line = first.strip(chars)
print(new_line)