sentence = input("Enter a sentence: ")

def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    
    return string[::-1]==string

if palindrome_sentence(sentence.casefold()):
    print(f'"{sentence}" is a palindrome sentence')
else:
    print(f'"{sentence}" is not a palindrome sentence')