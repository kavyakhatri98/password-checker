import string

COMMON_PASSWORDS = {"123456", "123456789", "12345678","admin", "iloveyou", "letmein","password", "qwerty"}

def check_password(password):
    if password.lower() in COMMON_PASSWORDS:
        return "Password is too common."

    if len(password) < 8:
        return "Password must be at least 8 characters long."

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if has_upper and has_lower and has_digit and has_special:
        return "Password is valid."
    else:
        if not has_upper:
            return "Password must contain at least one uppercase letter."
        if not has_lower:
            return "Password must contain at least one lowercase letter."
        if not has_digit:
            return "Password must contain at least one digit."
        if not has_special:
            return "Password must contain at least one special character."

password = input("Enter a password: ")
result = check_password(password)
print(result)
