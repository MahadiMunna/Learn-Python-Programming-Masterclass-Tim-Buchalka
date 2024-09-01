import random

answer = random.randint(0,10)
guess = 0
count = 3
guessed = False
print(answer)
print("Please guess a number between 1 and 10")
while answer!=guess and count!=0:
    guess = int(input())
    if answer==guess:
        print("You guessed it!")
        guessed = True
        break
    
    elif answer<guess:
        print(f"Please guess lower(remaining guess {count}): ")
    elif answer>guess:
        print(f"Please guess higher(remaining guess {count}): ")
    
    count-=1

if not guessed:
    print("You failed in 3 attempts to guess. Game over!")