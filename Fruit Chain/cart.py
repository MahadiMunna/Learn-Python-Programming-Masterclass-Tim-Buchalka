from constants import calculate_total_price, success, error
from fruit import Fruit
from orders import place_order

class CartItem(object):

    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity
        self.total_price = calculate_total_price(item, quantity)

def add_to_cart(current_user):
    while True:
        print('Enter your option:\n1. See details\n2. Add to cart\n3. View Cart\n0. Back')
        option = input(">  ")

        if option == '1':
            no = int(input('Enter fruit no to see details: '))
            fruit = Fruit.fruit_list[no-1]
            print(f'\nFruit Name: {fruit.fruit_name}\nFruit Origin: {fruit.origin}\nPrice: {fruit.price}\n')
            if fruit.discount > 0:
                print(f'Discount: {fruit.discount}%\nDiscount Price: {fruit.get_price}\n')
            print(f'Supply Date: {fruit.supply_date}\nExpiry Date: {fruit.expiry_date}')
            if fruit.stock_out:
                print('Status: Stock Out!\n')
            else:
                print('Status: Available!\n')
            
            print('Enter your option:\n1. Add to cart\nEnter 0 for go back')
            option = input(">  ")
            if option == '1':
                quantity = int(input('Enter quantity: '))
                cart_item = CartItem(fruit, quantity)
                current_user.cart.append(cart_item)

                success('*')
                success(f'{fruit.fruit_name} added to cart successfully!')
                success('*')
            elif option == '0':
                pass
        elif option == '2':
            no = int(input('Enter fruit no: '))
            fruit = Fruit.fruit_list[no-1]
            quantity = int(input('Enter quantity: '))
            cart_item = CartItem(fruit, quantity)
            current_user.cart.append(cart_item)

            success('*')
            success(f'{fruit.fruit_name} added to cart successfully!')
            success('*')
        elif option == '3':
            view_cart(current_user)
        elif option == '0':
            break
        else:
            error('!')
            error("Ops! You have chosen an invalid option!")
            error('!')

def view_cart(current_user):
    if len(current_user.cart) == 0:
        print('='*10 + 'Cart Items' + '='*10)
        print('Your cart is empty!')
        print(f'Total Price: {current_user.get_total_amount()}\n')
        return
    else:
        print('='*10 + 'Cart Items' + '='*10)
        for index, cart_item in enumerate(current_user.cart):
            print(f'{index+1}. {cart_item.item.fruit_name}({cart_item.item.unit})x{cart_item.quantity} - {cart_item.total_price}')
        print('='*len('='*10 + 'Cart Items' + '='*10))
        print(f'Total Price: {current_user.get_total_amount()}\n')
    
    print('Enter your option:\n1. Update cart\n2. Place order\nEnter 0 for go back')
    option = input(">  ")
    if option == '1':
        item_no = int(input('Enter item number: '))
        item = current_user.cart[item_no-1]
        print('If you want to remove enter quantity = 0')
        quantity = int(input(f'Enter new quantity for {item.item.fruit_name}: '))
        if quantity == 0:
            current_user.cart.remove(item)
            success('*')
            success(f'{item.item.fruit_name} removed from cart successfully!')
            success('*')
        else:
            item.quantity = quantity
            item.total_price = calculate_total_price(item.item, item.quantity)
            success('*')
            success(f'{item.item.fruit_name}\'s quantity updated successfully!')
            success('*')
    elif option == '2':
        place_order(current_user)
    elif option == '0':
        return
    else:
        error('!')
        error("Ops! You have chosen an invalid option!")
        error('!')