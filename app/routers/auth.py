from fastapi import APIRouter, HTTPException
from fastapi.param_functions import Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from starlette import status
from .. import schemas, models, database, utils, oauth2


router = APIRouter(
    prefix='/auth', tags=['authentication']
    )

@router.post(
    '/login', response_model=schemas.Token
    )
def login_user(data: schemas.Login_data,   db: Session = Depends(database.get_db)):
    print(data)
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Invalid Credentials')
    print(utils.check_password(data.password, user.password))
    if utils.check_password(data.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Invalid Credentials')
    token = oauth2.create_access_token(data= {'user_id':user.id})
    return {"access_token":token, "token_type":"bearer" }
























# from fastapi import APIRouter, HTTPException, status
# from fastapi.param_functions import Depends
# from sqlalchemy.orm import Session
# from fastapi.security import OAuth2PasswordRequestForm

# from .. import database, schemas, models, utils, oauth2

# router = APIRouter(prefix= '/auth', tags=['authentication'])

# @router.post('/login')
# def login(user_info: OAuth2PasswordRequestForm = Depends() , db: Session = Depends(database.get_db) ):
#     user = db.query(models.User).filter(models.User.email == user_info.username).first()
#     print(user)
#     if not user:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'invalid email or password')
    
#     if not utils.verify(user_info.password, user.password):
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Invalid email or password')
#     accss_token = oauth2.create_access_token(data = {'user_id': user.id} )
#     return {'access_token': accss_token, 'token_type':'bearer'}
