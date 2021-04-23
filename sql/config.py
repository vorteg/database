from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime


#Connection to any database
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

class DBSessions:
    engine = create_engine(SQLALCHEMY_DATABASE_URL,
                        connect_args={"check_same_thread": False})
    BaseEngine = declarative_base()

    DataBaseSessions = scoped_session(sessionmaker(autocommit=False,
                                            autoflush=False, bind=engine))
    LocalSession = DataBaseSessions()