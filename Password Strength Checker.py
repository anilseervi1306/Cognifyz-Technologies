import re

def validate_password(password):
    
    # To Check if the password has at least 8 characters
    if len(password) < 8:
        return False
    
    # To Check if the password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    
    # To Check if the password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    
    # To Check if the password contains at least one digit
    if not re.search(r'\d', password):
        return False
    
    # To Check if the password contains at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    # If all the conditions got matched, the password is strong and valid
    return True

password = input("Enter your password: ")
is_valid = validate_password(password)

if is_valid:
    print("Password is strong and it meets the requirements.")
else:
    print("Password is weak and does not meet requirements.")