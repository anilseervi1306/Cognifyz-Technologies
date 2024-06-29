import re

def is_email_valid(email_address):
    # Email pattern with character sets
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(?:[a-zA-Z]{2}|com|org|net|edu|gov|mil|biz|info|mobi|name|aero|jobs|museum)$'
    
    # Compiling the pattern
    email_regex = re.compile(email_pattern)
    
    # Checking the email matches with pattern
    if email_regex.fullmatch(email_address):
        return True
    else:
        return False

def get_user_input():
    email_input = input("Enter an email address to validate: ")
    return email_input

def display_validation_result(email_address, is_valid):
    if is_valid:
        print(f"The email address '{email_address}' is valid.")
    else:
        print(f"The email address '{email_address}' is not valid.")

def main():
    user_email = get_user_input()
    email_validation_result = is_email_valid(user_email)
    display_validation_result(user_email, email_validation_result)

if __name__ == "__main__":
    main()