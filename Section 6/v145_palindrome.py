def is_palindrome(string):
    return string[::-1] == string

word = input("Please enter a word: ")

if is_palindrome(word.casefold()):
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not a palindrome')