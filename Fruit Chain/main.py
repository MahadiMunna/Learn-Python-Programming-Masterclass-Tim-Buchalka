import time
from constants import banner, error, make_date
from users import User, admin_user, customer_user
from auth import login, register
from fruit import Fruit

admin = User('admin','Admin','Shaheb Mohodoy','admin@gmail.com', 'Male','admin')
munna = User('munna','Mahadi','Munna','munna@gmail.com', 'Male','munna')
admin.make_admin()
current_user = None
def load_data():
    with open('./Fruit Chain/fruits.txt', 'r') as fruits:
        for line in fruits:
            fruit_name, price, unit, origin, discount, supply_date, expiry_date = tuple(line.strip('\n').split(','))
            price = float(price)
            discount = float(discount)
            supply_date = make_date(supply_date)
            expiry_date = make_date(expiry_date)
            Fruit(fruit_name, price, unit, origin, discount, supply_date, expiry_date)
            
load_data()
banner('#')
banner(' ')
banner('Welcome to FruitChain')
banner(' ')
banner('#')
while True:
    if current_user:
        banner('#')
        banner(' ')
        banner(f'Hello, {current_user.fullname}')
        banner(' ')
        banner('#')
    if current_user == None:
        print('Enter your option:\n1. Login\n2. Register\n3. Exit')
        option = input(">  ")

        if option == '1':
            current_user = login()
        elif option == '2':
            current_user = register()
        elif option == '3':
            banner('#')
            banner("FruitChain is shutting down...")
            time.sleep(4)
            banner("Thank you!")
            banner('#')
            break
        else:
            error('!')
            error("Ops! You have chosen an invalid option!")
            error('!')

    else:
        if current_user.is_admin():
            while True:
                print("Enter your option:\n1. Add new fruit\n2. Update fruit\n3. Manage stock\n4. Manage users\n5. Manage orders\n6. Profile\n7. Logout")
                op = input(">  ")
                if op in "123456":
                    admin_user(current_user, op)
                elif op == '7':
                    break
                else:
                    error('!')
                    error("Ops! You have chosen an invalid option!")
                    error('!')
        else:
            while True:
                print("Enter your option:\n1. See available fruits\n2. Flash-sale\n3. Cart\n4. Orders\n5. Profile\n6. Logout")    
                op = input(">  ")
                if op in "12345":
                    customer_user(current_user, op)
                elif op == '6':
                    break
                else:
                    error('!')
                    error("Ops! You have chosen an invalid option!")
                    error('!')

        current_user = None
        print("\nLogged out successfully!\n")