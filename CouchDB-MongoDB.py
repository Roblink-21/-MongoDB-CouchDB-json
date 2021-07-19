#!/usr/bin/env python
# coding: utf-8

# In[7]:


import json
from argparse import ArgumentParser
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb


# In[10]:


#Establecer el direccionamiento de nuestro CouchDB
URL = 'http://Rob:RP38490ytFH@127.0.0.1:5984'
print(URL)

#Verificacion de la conexion con CouchDB
try:
    response = requests.get(URL)
    if response.status_code == 200:
        print('CouchDB connection: Success')
    if response.status_code == 401:
        print('CouchDB connection: failed', response.json())
except requests.ConnectionError as e:
    raise e

#Establecer los parametros que resibira la base de datos
server=couchdb.Server(URL)
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

#Establecer el direccionamiento de nuestra plataforma como servicio (MongoDB Atlas) 
CLIENT = MongoClient('mongodb+srv://esfot:esfot@cluster0.xf99e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')


#Verifica la coneccion del cluster de MongoDB
try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)

#Identificar la base de datos de MongoDB
DBS=['TheDevelopers']


#Verifica si la base de datos esta creada o no en la plataforma CouchDB
try:
    dbc=server.create('mongo_destino2') #Crea la base de datos.
except:
    dbc=server['mongo_destino2'] #Apunta a la base de datos que ya ha sido creada.
    
#Crea una lista donde recopila los documentos de las colecciones de la base de datos(MongoDB)
for db in DBS:
    if db not in ('admin', 'local','config'):  
        cols = CLIENT[db].list_collection_names()  #Recopila la coleccion dentro de una lista
        for col in cols:
            print('Querying documents from collection {} in database {}'.format(col, db)) #Muestra los doc's de la coleccion
            for x in CLIENT[db][col].find():  
                try:
                    
                    documents=json.loads(json_util.dumps(x))

                    documents["_id"]=str(documents["_id"]["$oid"])


                    print(documents)
                    doc=dbc.save(documents)

                except TypeError as t:

                    print('current document raised error: {}'.format(t))
                    SKIPPED.append(x)  # creating list of skipped documents for later analysis
                    continue    # continue to next document
                except Exception as e:
                    raise e  


# In[ ]:




