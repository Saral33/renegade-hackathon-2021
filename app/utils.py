
from cryptography.utils import deprecated
from passlib.context import CryptContext


pwd = CryptContext(schemes=['bcrypt'], deprecated= 'auto')

def hash(password):
    return pwd.hash(password)

def check_password(password, hash_password):
    return pwd.verify(hash(password), hash_password)
    
























# from passlib.context import CryptContext

# pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# def hash(password: str):
#     return pwd_context.hash(password)

# def verify(password, hash_password):
#     return pwd_context.verify(password, hash_password)
    