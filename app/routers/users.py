from typing import List
from .. import models, schemas, utils
from fastapi import FastAPI, status, HTTPException, Depends,  APIRouter
from ..database import get_db
from sqlalchemy.orm.session import Session

router = APIRouter(
    prefix='/users',
    tags= ['Users']

)

@router.post('/create_user',status_code=status.HTTP_201_CREATED, response_model= schemas.User_response)
def create_user(user: schemas.Create_user, db:Session = Depends(get_db)):

 
    user.password = utils.hash(user.password)
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get('/', response_model= List[schemas.User_response])
def get_users(db: Session = Depends(get_db)):
    user = db.query(models.User).all()
    print(user)
    return user
    
@router.get('/{id}', response_model=schemas.User_response)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    print(user)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'User with id: {id} could not be found')

    return user
