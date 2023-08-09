# Password Validation Function

def validate_password(password):
    if " " in password:
        return False
    if len(password) < 8:
        return False
    if not any(x.isupper() for x in password):
        return False
    if not any(x.islower() for x in password):
        return False
    if not any(x.isdigit() for x in password):
        return False
   
    return True