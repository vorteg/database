from datetime import datetime
from config import DBSessions as DBSessions
from sqlalchemy import Column, Integer, String, DateTime
import migrations

class User(DBSessions.BaseEngine):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, unique=True, index=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now())
    
    def __str__(self):
        return self.username
    
if __name__ == '__main__':
    migrations.delate_tables()
    migrations.create_tables()
    