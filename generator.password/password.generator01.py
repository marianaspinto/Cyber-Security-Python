# generate random password with all random characters
import random
import string

# password with 10 characters by default, containing letters, numbers 
# and symbols, stored in the variable "alphabet", and repeated as many times
# as requested
def generate_password(length: int = 10):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password

password = generate_password()
print(f"Generator Password: {password}")
