import csv
from datetime import datetime
from constants import generate_hash, error, success

class Order(object):

    orders_list = []
    def __init__(self, user, billing_address, items, total_amount, payment_method, payment_status):
        self.user = user
        self.billing_address = billing_address
        self.items = items
        self.total_amount = total_amount
        self.payment_method = payment_method
        self.payment_status = payment_status
        self.order_status = None
        self.timestamp = datetime.now()
        text = f'{user.user_name}{items}{total_amount}{payment_method}{self.timestamp}'
        self.order_id = generate_hash(text)
        Order.orders_list.append(self)

    def set_order_status(self, status):
        self.order_status = status
    
    def items_representation(self):
        items = ""
        for index, item in enumerate(self.items):
            items+=f'{item.item.fruit_name}x{item.quantity}'
            if index == len(self.items)-1:
                items+=''
            else:
                items+=', '

        return items

class BillingAddress(object):

    def __init__(self, village, post, police_station, district, phone):
        self.village = village
        self.post = post
        self.police_station = police_station
        self.district = district
        self.phone = phone
    def __str__(self):
        return f'{self.village}, {self.post}, {self.police_station}, {self.district}, {self.phone}'
    
def place_order(current_user):
    print('Please provide your address information- ')
    billing_address = BillingAddress(
        input("Village: "),
        input("Post: "),
        input("Police station: "),
        input("District: "),
        input("Phone number: "))
    items = [item for item in current_user.cart]
    total_amount = current_user.get_total_amount()
    payment_status = "Pending"
    payment_method = input("Enter your payment method (1.Card, 2.Mobile Banking, 3.Cash on delivery): ")
    if payment_method == '1':
        payment_method = "Card"
        payment_status = "Paid"
    elif payment_method == '2':
        payment_method = "Mobile Banking"
        payment_status = "Paid"
    elif payment_method == '3':
        payment_method = "Cash on delivery"
    else:
        error('!')
        error("Invalid payment method. Please try again.")
        error('!')
        return
    
    my_order = Order(current_user, billing_address, items, total_amount, payment_method, payment_status)
    my_order.set_order_status("In Queue")
    current_user.orders.append(my_order)
    current_user.cart = []

    success('*')
    success("Order placed successfully!")
    success('*')

def view_orders(current_user):
    if len(current_user.orders) == 0:
        print('='*10 + 'Orders' + '='*10)
        print('You don\'t have any orders yet!')
        print('='*len('='*10 + 'Cart Items' + '='*10))
        return
    else:
        print('='*10 + 'Orders' + '='*10)
        for index, order in enumerate(current_user.orders):
            print(f'{index+1}. {order.items_representation()} - {order.total_amount} - {order.payment_status} - {order.order_status} - {order.timestamp}')
        print('='*len('='*10 + 'Cart Items' + '='*10))
    
    print('\nEnter your option:\n1. Cancel order\n2. Remove order from list\nEnter 0 for go back')
    option = input('>  ')
    if option == '1':
        no = int(input('Enter order no for cancel: '))
        current_user.orders[no-1].order_status = 'Cancelled'
        success('*')
        success('You cancelled the order successfully')
        success('*')
    elif option == '2':
        no = int(input('Enter order no for remove from list: '))
        order = current_user.orders[no-1]
        current_user.orders.remove(order)
        success('*')
        success('You removed the order from list successfully')
        success('*')
    elif option == '0':
        return

def manage_orders():
    if len(Order.orders_list) == 0:
        print('='*10 + 'Orders' + '='*10)
        print('No orders available')
        print('='*len('='*10 + 'Cart Items' + '='*10))
        return
    else:
        print('='*10 + 'Orders' + '='*10)
        for index, order in enumerate(Order.orders_list):
            print(f'{index+1}. {order.user.fullname} - {order.items_representation()} - {order.total_amount} - {order.payment_method} - {order.order_status} - {order.timestamp}')
        print('='*len('='*10 + 'Cart Items' + '='*10))
    
    print('\nEnter your option:\n1. Update order\n2. Remove order from list\n3. Export to CSV\nEnter 0 for go back')
    option = input('>  ')

    if option == '1':
        no = int(input('Enter order no for update: '))
        order = Order.orders_list[no-1]
        print("============Order details============")
        print(f'Customer: {order.user.fullname}\nAddress: {order.billing_address.__str__()}\nOrdered items: {order.items_representation()}\nPayable amount: {order.total_amount}\nPayment method: {order.payment_method}\nPayment status: {order.payment_status}\nOrder status: {order.order_status}\nTimestamp: {order.timestamp}')
        print('======================================')
        print('Enter your option:\n1. Update order status\n2. Update payment status\nEnter 0 for go back')
        update_option = input('>  ')
        if update_option == '1':
            order.order_status = input('In queue/In processing/In transit/Delivered: ')
            success('*')
            success('Order status updated successfully')
            success('*')
        elif update_option == '2':
            order.payment_status = input('Paid/Unpaid: ')
            success('*')
            success('Payment status updated successfully')
            success('*')
        elif update_option == '0':
            return
        else:
            error('!')
            error("Invalid option. Please try again.")
            error('!')
    elif option == '2':
        no = int(input('Enter order no for remove from list: '))
        order = Order.orders_list[no-1]
        Order.orders_list.remove(order)
        success('*')
        success('You removed the order from list successfully')
        success('*')
    elif option == '3':
        with open('./Fruit Chain/orders.csv', 'w', encoding='UTF8', newline='') as order_file:
            writer = csv.writer(order_file)
            header = ['Customer Name','Billing Address','Ordered Items','Payable Amount','Payment Method','Payment status','Order Status','Timestamp']
            writer.writerow(header)
            for order in Order.orders_list:
                row = [order.user.fullname, order.billing_address.__str__(), order.items_representation(), order.total_amount, order.payment_method, order.payment_status, order.order_status, order.timestamp]
                writer.writerow(row)
                
        success('*')
        success('CSV file has been created successfully')
        success('*')
    elif option == '0':
        return
    else:
        error('!')
        error("Invalid option. Please try again.")
        error('!')