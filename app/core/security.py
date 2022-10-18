import bcrypt


def verify_password(plain_password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password)


def generate_salt() -> bytes:
    return bcrypt.gensalt()


def get_password_hash(password: str, salt: bytes) -> bytes:
    return bcrypt.hashpw(password.encode("utf-8"), salt)
