from sqlalchemy.orm import Session
from config import DBSessions
from model import User as User
import json

db = DBSessions.LocalSession 

def get_data_all(model:object,skip: int = 0, limit: int = 100):
     datos = db.query(model).offset(skip).limit(limit).all()
     return datos

def get_data(model:object, data_reference:str):
     data = db.query(model).filter_by(username=data_reference).first()
     return data

def create(data: object):          
     db.add(data)
     db.commit()

def update(data_reference, data:object, model:object):
     db_data = db.query(model).filter_by(username=data_reference).first()
     db_data.username= data.username
     db_data.email= data.email
     db.commit()
     db.refresh(db_data)
     
def delete(data_reference, model:object):
     db_data = db.query(model).filter_by(username=data_reference).first()
     if db_data:
        db.delete(db_data)
        db.commit()
     return "Dato eliminado"

if __name__ == "__main__":
     #create(User(username='User2', email='user2@example.com' ))
     #u = get_data(User, "User2")
     #a = get_data_all(User)
     #print(u)
     delete("User4", User)