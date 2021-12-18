from fastapi.security import oauth2
from sqlalchemy.sql.functions import mode
from .. import models, schemas, utils
from fastapi import FastAPI, status, HTTPException, Depends,  APIRouter
from ..database import get_db
from sqlalchemy.orm.session import Session
from typing import List
from .. import oauth2


router = APIRouter(
    prefix='/posts',
    tags= ['Posts']
)

@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute(""" select * from posts  """)
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    print(posts)
    return posts

@router.get('/{id}',response_model=schemas.Post)
def get_post(id: int,db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    # cursor.execute(''' select * from posts where id = %s ''', (str(id)))
    # post_id = cursor.fetchone()
    post_id = db.query(models.Post).filter(models.Post.id == id).first()

    if post_id.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to view post")

    if not post_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"post with id {str(id)} could not be found")
    return post_id

@router.post('/create_posts',status_code=status.HTTP_201_CREATED, response_model= schemas.Post)
def create_posts( post: schemas.Post_create,db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" insert into posts (title, content) values (%s, %s) returning * """ ,(post.title, post.content))
    # new_post = cursor.fetchone()
    # conn.commit()
    new_post = models.Post(user_id=current_user.id , **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.delete('/delete_post/{id}')
def delete_post(id: int,db: Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user)):
    # cursor.execute(''' delete from posts where id= %s returning *''', (str(id)))
    # deleted_post = cursor.fetchone
    # conn.commit()
    deleted_post = db.query(models.Post).filter(models.Post.id == id)
    print(deleted_post)
    post = deleted_post.first()

    if post == None:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=f"post with {str(id)} could not be found")
    
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to delete post")

    deleted_post.delete(synchronize_session=False)
    db.commit()


    return {'Data': f'The post with id {id} was deleted'}

@router.put('/update_post/{id}',status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def update_post(id: int, up_post:schemas.Post_create,db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    # cursor.execute(''' update posts set title=%s, content= %s where id=%s returning * ''',(post.title, post.content, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()

    updated_post = db.query(models.Post).filter(models.Post.id == id)
    post = updated_post.first()

    if post == None:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=f"post with id: {id} could not be found")

    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Not authorized to update post")

    updated_post.update(up_post.dict(), synchronize_session=False)
    db.commit()
    return updated_post.first() 

