with open('.\\Section 8\\munna.txt', 'r') as munna:
    # lines = munna.readlines()
    # text = munna.read()
    while True:
        line = munna.readline().rstrip()
        print(line)
        if 'mahadi munna' in line.casefold():
            break

# print(lines)
# print(lines[-1:])
# for line in reversed(lines):
#     print(line.strip())

# print(text)
# for char in reversed(text):
#     print(char, end="")