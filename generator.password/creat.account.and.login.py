# store the password with a hash value and read it securely, without 
# displaying the characters in the user interface
import hashlib
import getpass

password_manager = {}

# create acount with username and password 
def create_account():
    user_name = input("Enter your desired username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest() 
    # "encode" converts a string value to bytes, as hash work with binare values, 
    # and "hexadigest" converts to hexadecimal
    password_manager[user_name] = hashed_password 
    # store tue username and password in the "password_anager" variable as a key-value pair
    print("Account created successfully!")

# create an account or login in
def login():
    username = input("Enter your desired username: ")
    password  = getpass.getpass("Enter your desired password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login successfully!")
    else:
        print("Invalid username or password")

# main function with selection menu
def main():
    while True:
        choice = input("Enter 1 to create an account, 2 to login, or 0 to exit: ") 
    
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
           break
        else:
           print("Invalid choice")


if __name__ == "__main__":
        main()

    


