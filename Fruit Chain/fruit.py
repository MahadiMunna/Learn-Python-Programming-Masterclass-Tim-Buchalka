from constants import success, error, make_date

class Fruit(object):

    fruit_list = []
    def __init__(self, fruit_name, price, unit, origin, discount, supply_date, expiry_date):
        self.fruit_name = fruit_name
        self.price = price
        self.unit = unit
        self.origin = origin
        self.discount = discount
        self.supply_date = supply_date
        self.expiry_date = expiry_date
        self.stock_out = False
        Fruit.fruit_list.append(self)

    def make_stock_out(self):
        self.stock_out = True
    
    def make_stock_in(self):
        self.stock_out = False
    @property
    def get_price(self):
        if self.discount > 0:
            return float((self.price - (self.price * self.discount)/100))
        else:
            return float(self.price)

def add_fruit():
    fruit_name = input("Fruit name: ")
    price = float(input("Price per unit: "))
    unit = input("Unit (kg/gm/dozen/pcs/etc.): ")
    origin = input("Fruit origin: ")
    discount = float(input("Discount(0-100): "))
    supply_date = input("Supply date (YYYY-MM-DD): ")
    expiry_date = input("Expiry date (YYYY-MM-DD): ")
    fruit = Fruit(fruit_name, price, unit, origin, discount, supply_date, expiry_date)
    success('*')
    success(f'{fruit.fruit_name} added successfully!')
    success('*')

def view_fruits(stock_out = False):
    for index, fruit in enumerate(Fruit.fruit_list):
        if stock_out == False and fruit.stock_out == False:
            print('='*7 + f' Fruit No: {index+1} ' + '='*7)
            print(f'Fruit name: {fruit.fruit_name}')
            print(f'Price: {fruit.price}', end=" ")
            if fruit.discount > 0:
                print(f'({fruit.get_price} at {fruit.discount}% discount)', end=" ")
            print(f'per {fruit.unit}')
            if fruit.stock_out:
                print(f'Status: Stock out')
            else:
                print(f'Status: Available')
            print(f"Supply Date: {fruit.supply_date}")
            print(f"Expiry Date: {fruit.expiry_date}")
            print('='*len('='*7 + f' Fruit No: {index+1} ' + '='*7)+'\n')
            
        elif stock_out == True and fruit.stock_out == True:
            print('='*7 + f' Fruit No: {index+1} ' + '='*7)
            print(f'Fruit name: {fruit.fruit_name}')
            print(f'Price: {fruit.price}', end=" ")
            if fruit.discount > 0:
                print(f'({fruit.get_price} at {fruit.discount}% discount)', end=" ")
            print(f'per {fruit.unit}')
            if fruit.stock_out:
                print(f'Status: Stock out')
            else:
                print(f'Status: Available')
            print(f"Supply Date: {fruit.supply_date}")
            print(f"Expiry Date: {fruit.expiry_date}")
            print('='*len('='*7 + f' Fruit No: {index+1} ' + '='*7)+'\n')

def user_fruits_view():
    for index, fruit in enumerate(Fruit.fruit_list):
        if fruit.stock_out == False:
            print('='*7 + f' Fruit No: {index+1} ' + '='*7)
            print(f'Fruit name: {fruit.fruit_name}')
            print(f'Price: {fruit.price}', end=" ")
            if fruit.discount > 0:
                print(f'({fruit.get_price} at {fruit.discount}% discount)', end=" ")
            print(f'per {fruit.unit}')
            if fruit.stock_out:
                print(f'Status: Stock out')
            else:
                print(f'Status: Available')
            print('='*len('='*7 + f' Fruit No: {index+1} ' + '='*7)+'\n')

def flash_sale():
    for index, fruit in enumerate(Fruit.fruit_list):
        if fruit.stock_out == False and fruit.discount > 0:
            print('='*7 + f' Fruit No: {index+1} ' + '='*7)
            print(f'Fruit name: {fruit.fruit_name}')
            print(f'Price: {fruit.price}', end=" ")
            if fruit.discount > 0:
                print(f'({fruit.get_price} at {fruit.discount}% discount)', end=" ")
            print(f'per {fruit.unit}')
            if fruit.stock_out:
                print(f'Status: Stock out')
            else:
                print(f'Status: Available')
            print('='*len('='*7 + f' Fruit No: {index+1} ' + '='*7)+'\n')

def update_fruit():
        print('Enter 0 for go back\n')
        no = int(input('Enter the fruit no for update: '))
        if no == 0:
            return
        fruit = Fruit.fruit_list[no-1]
        print(f'\nFruit Details-\nName: {fruit.fruit_name}\nPrice: {fruit.price} per {fruit.unit}\nDiscount: {fruit.discount}\nOrigin: {fruit.origin}\nSupply Date: {fruit.supply_date}\nExpiry Date: {fruit.expiry_date}\n\n')

        print('Enter new details- \n')
        fruit.fruit_name = input('Fruit name: ')
        fruit.price = float(input('Price per unit: '))
        fruit.unit = input('Unit (kg/gm/dozen/pcs/etc.): ')
        fruit.origin = input('Fruit origin: ')
        fruit.discount = float(input('Discount(0-100): '))
        supply_date = input('Supply date (YYYY-MM-DD): ')
        fruit.supply_date = make_date(supply_date)
        expiry_date = input('Expiry date (YYYY-MM-DD): ')
        fruit.expiry_date = make_date(expiry_date)

        success('*')
        success(f'Fruit updated successfully!')
        success('*')

def manage_stock():
    print("\nChoose your option from below: \n1. Make stock out\n2. See stock out list\nEnter 0 for go back")
    option = input(">  ")
    if option == '0':
        return
    elif option == '1':
        no = int(input("Enter fruit no: "))
        fruit = Fruit.fruit_list[no-1]
        fruit.make_stock_out()
        success('*')
        success(f'{fruit.fruit_name} is now unavailable')
        success('*')
    elif option == '2':
        view_fruits(stock_out=True)
        print("\nChoose your option from below: \n1. Make stock in\nPress enter for Back")
        option = input(">  ")
        if option == '1':
            no = int(input("Enter fruit no: "))
            fruit = Fruit.fruit_list[no-1]
            fruit.make_stock_in()
            success('*')
            success(f'{fruit.fruit_name} is now available')
            success('*')
    else:
        error('!')
        error("Ops! You have chosen an invalid option!")
        error('!')

