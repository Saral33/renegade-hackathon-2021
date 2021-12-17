from datetime import datetime, timedelta
from cryptography.hazmat.primitives.ciphers import algorithms
from fastapi import Depends, HTTPException, status
from jose import jwt , JWTError
from sqlalchemy.orm import Session
from . import schemas, database, models
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

secret_key = 'sffhdjfdsfdfsdfsdfsfsgy'
alg = 'HS256'
token_time = 30

def create_access_token(data: dict):
    data_copy = data.copy()
    expiry_time = datetime.utcnow() + timedelta(minutes=token_time)
    data_copy.update({'exp':expiry_time})
    token = jwt.encode(data_copy, secret_key, algorithm=alg)
    return token

def verify_access_token(token: str, credential_exception):
    try:
        payload = jwt.decode(token, secret_key, algorithms=alg)
        id: str = payload.get("user_id")
        if id is None:
            raise credential_exception
        # token_data = schemas.Token_data()
        # print(token_data)
        return id
    except JWTError:
        raise credential_exception
    
    

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db) ):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"could not validate credentails", headers={"www-Authenticate": "Bearer"})

    id = verify_access_token(token, credential_exception)
    user = db.query(models.User).filter(models.User.id == id ).first()
    return user

    






















# from jose import JWTError, jwt
# from datetime import datetime, timedelta
# from . import schemas

# SECRET_KEY = 'RNAASJSIFSDIGjasfihasrw'
# ALOGRITHM = 'HS256'
# TOKEN_EXPIRES_IN = 20

# def create_access_token(data: dict):
#     copy = data.copy()
#     expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRES_IN)
#     copy.update({'exp': expire})
#     token = jwt.encode(copy, SECRET_KEY, algorithm =ALOGRITHM)
#     return token

# def verify_access_token(token: str, credentials_exception):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithm = ALOGRITHM )
#         payload.get('user_id')

#         if not id:
#             raise credentials_exception
#         token_data = schemas.Token(id=id)
#     except JWTError:
#         raise credentials_exception
#     return token_data
    
    




