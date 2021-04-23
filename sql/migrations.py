from config import DBSessions as DBSessions


def delate_tables():
    #Borrar tablas
    DBSessions.BaseEngine.metadata.drop_all(DBSessions.engine)
    
def create_tables():
    #Crear tablas
    DBSessions.BaseEngine.metadata.create_all(DBSessions.engine)
    

    

if __name__ == '__main__':
    delate_tables()
    create_tables()
   