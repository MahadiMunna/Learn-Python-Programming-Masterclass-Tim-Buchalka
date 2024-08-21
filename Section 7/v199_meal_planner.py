from contents import pantry, recipes

def add_to_shopping(data: dict, item: str, quantity: int) -> None:
    data[item] = data.setdefault(item, 0) + quantity

display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index+1)] = key

shopping_list = {}

while True:
    print('-'*30)
    print("Please enter your choice: ")
    print('-'*30)
    for key, value in display_dict.items():
        print(f'{key}: {value}')
    print("0: For go to market with shopping list")
    choice = input('> ')
    if choice == '0':
        print("You shopping list: ")
        for item, quantity in shopping_list.items():
            print(f'{item}: {quantity}')
        break
    elif choice in display_dict:
        print("Checking ingredients: ")
        choosen_item = display_dict[choice]
        ingridients = recipes[choosen_item]
        print(ingridients)
        for item, quantity in ingridients.items():
            quantity_in_pantry = pantry.get(item, 0)
            if quantity_in_pantry >= quantity:
                print(f"{item} OK")
            else:
                required = quantity - quantity_in_pantry
                print(f"You need to buy {required} {item}")
                add_to_shopping(shopping_list, item, required)

    else:
        print('-'*30)
        print("You have choosen invalid option!")