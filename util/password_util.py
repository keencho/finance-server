from werkzeug.security import generate_password_hash, check_password_hash


def encrypt_password(password: str) -> str:
    return generate_password_hash(password)


def check_password(origin_password: str, entered_password: str) -> bool:
    return check_password_hash(origin_password, entered_password)