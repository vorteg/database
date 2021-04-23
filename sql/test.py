from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime


#Connection to any database
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False})
BaseEngine = declarative_base()

#Defining Model 
class User(BaseEngine):
    __tablename__= 'users'
    
    id = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now())
    
    def __str__(self):
        return self.username
    
DataBaseSessions = scoped_session(sessionmaker(engine))
LocalSession = DataBaseSessions()

if __name__ == '__main__':
    #Borrar tablas
    BaseEngine.metadata.drop_all(engine)
    #Crear tablas
    BaseEngine.metadata.create_all(engine)
    
    # #agregando datos
    # user1 = User(username='User1', email='user1@example.com', )
    # user2 = User(username='User2', email='user2@example.com', )
    # user3 = User(username='User3', email='user3@example.com', )
    # user4 = User(username='User4', email='user4@example.com', )
    
    # LocalSession.add(user1)
    # LocalSession.add(user2)
    # LocalSession.add(user3)
    # LocalSession.add(user4)
    # LocalSession.commit()
    