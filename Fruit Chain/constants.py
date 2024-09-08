import hashlib, datetime

def generate_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()[:10]

def banner(text, width=50):
    if text == '#':
        print('#' * width)
    else:
        text = text.center(width-4)
        print(f"##{text}##")

def success(text, width=50):
    if text == '*':
        print('*' * width)
    else:
        text = text.center(width-4)
        print(f"**{text}**")

def error(text, width=50):
    if text == '!':
        print('!' * width)
    else:
        text = text.center(width-4)
        print(f"!!{text}!!")

def make_date(date):
    return datetime.datetime.strptime(date, '%Y-%m-%d',).date()

def calculate_total_price(item, quantity):
    return item.get_price*quantity
