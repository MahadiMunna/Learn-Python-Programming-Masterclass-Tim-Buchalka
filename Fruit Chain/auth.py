from users import User
from constants import generate_hash, error, success

def login():
    user_name = input("Enter your username: ")
    input_pass = input("Enter your password: ")
    password = generate_hash(input_pass)
    for user in User.user_list:
        if user.user_name == user_name and user.get_password() == password:
            return user
    else:
        
        error("Invalid credentials. Try again.")
        
        return None

def register():
    print("Please, provide following information-")
    user_name = input("Username: ")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Email: ")
    gender = input("Gender(Male/Female): ")
    password = input("Password: ")
    re_pass = input("Re-type password: ")
    if password != re_pass:
        
        error("Passwords do not match. Try again.")
        
        return None
    else:
        
        success("Your account created successfully!")
        
        return User(user_name, first_name, last_name, email, gender, password)