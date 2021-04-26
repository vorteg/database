from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'
DB_NAME = 'teststore'
COLLECTION_NAME = 'products'

#Conexion con  el servicio de MONGO_DB
client = MongoClient(MONGO_URI)

#Definiendo  el DataBase con el que vamos a trabajar
# si la base de datos mongo db solito la crea tambien la colleccion
db = client[DB_NAME]

#Especificando la collleccion con la que se trabajara
collection = db[COLLECTION_NAME]

# el DB se crea hasta que agregamos o interactuamos con los datos, Ir a crud para esto.


