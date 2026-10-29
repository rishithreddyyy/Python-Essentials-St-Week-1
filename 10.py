def validate_password(password):
    errors = []

    if len(password) < 8:
        errors.append("Password must contain at least 8 characters")
    if not any(char.isupper() for char in password):
        errors.append("Password must contain an uppercase letter")
    if not any(char.islower() for char in password):
        errors.append("Password must contain a lowercase letter")
    if not any(char.isdigit() for char in password):
        errors.append("Password must contain a digit")

    special_characters = "!@#$%^&*"
    if not any(char in special_characters for char in password):
        errors.append("Password must contain a special character")

    return {"is_valid": len(errors) == 0, "errors": errors}


if __name__ == "__main__":
    print(validate_password("weak"))
    print(validate_password("Weak123"))
    print(validate_password("MySecure@1"))
