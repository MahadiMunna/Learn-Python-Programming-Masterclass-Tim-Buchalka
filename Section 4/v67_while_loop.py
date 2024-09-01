available_exists = ['east', 'west', 'south', 'north']

exit_direction = ""
while exit_direction not in available_exists:
    exit_direction = input("Please enter a direction: ")

print(f"You are exiting by {exit_direction}")