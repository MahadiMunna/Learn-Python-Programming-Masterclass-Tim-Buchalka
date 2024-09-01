guess = 0
high = 1000
low = 1
guesses = 1

while high != low:
    guess = int((high+low)/2)
    cmnd = input(f'My guess is {guess}. Is your guess is high(h) or low(l) or correct(c)?')

    if cmnd == 'h':
        low = guess+1
    elif cmnd == 'l':
        high = guess-1
    elif cmnd == 'c':
        print(f'I guessed it in {guesses} steps!')
        break
    guesses+=1
else:
    print(f'I guessed it in {guesses} steps!')