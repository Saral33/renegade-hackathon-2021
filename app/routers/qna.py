from fastapi.security import oauth2
from sqlalchemy.sql.functions import mode
from .. import models, schemas
from fastapi import FastAPI, status, HTTPException, Depends,  APIRouter
from ..database import get_db
from sqlalchemy.orm.session import Session
from typing import List
from .. import oauth2

router = APIRouter(tags= ['questions and answer'])

@router.get('/getq/{id}')
def get_question(id: int,db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    # cursor.execute(''' select * from posts where id = %s ''', (str(id)))
    # post_id = cursor.fetchone()
    question1= db.query(models.Question).filter(models.Question.id == id).first()

    if not question1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"post with id {str(id)} could not be found")
    return question1

@router.post('/storeans/{id}')
def store_ans(id: int, ans: schemas.Answer, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    user_ans = models.Answer(question_id=id,user_id=current_user.id , **ans.dict())
    print(user_ans)
    db.add(user_ans)
    db.commit()
    db.refresh(user_ans)
    return user_ans