from typing import Dict
from config import collection



def mongo_create(data_collection:Dict):
    collection.insert_one(data_collection) 
    # lista
    # collection.insert_many(list[dic1, dic2, etc..])
    return print("si se pudo")

def mongo_update(search:Dict, newData:Dict):
    collection.update_one(search, {"$set": newData})

def mongo_delete(search:Dict):
    collection.delete_one(search)

def mongo_read():
    results = collection.find()
    for r in results:
        print(r)

def mongo_query(search:Dict):
    results = collection.find(search)
    for r in results:
        print(r)

if __name__ == '__main__':
    # Nota si las pruebas se hacen desde WSL mongodb tiene que estar instalado en esa maquina virtual, esto solo aplica en windows
    document = {"_id":4, "name": "mouse", "price": 300}
    # mongo_create(document)
    # mongo_read()
    #mongo_query({"price": 400})
    #mongo_update({"price": 400}, document)
    mongo_delete({"_id": 4})
    
    #otros comandos utiles
    # para contar los objetos
    c =collection.count_documents({})
    print(c)
    #para incrementar el valor de un dato
    i = collection.update_one({"_id":3},{"$inc": {"price": 30}})
    mongo_read()