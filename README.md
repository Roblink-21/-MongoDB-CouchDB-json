# - MongoDB-CouchDB-json

# Integrantes
-
-
-
- Luis Jácome
- Sebastián Valencia
- Roberth Pincha

# Instrucciones: 

1.- Formar grupos de trabajo y crear una base de datos, dentro de ella crear una colección con el nombre de cada integrante y cada una de ellas de la fuente de datos kaggle seleccionar un json de su interés e insertarlo en MongoDB Atlas. (un json por compañero)

2.- Exportar los datos de MongoDB a CouchDB con el script "mongo2couch.py", el script está diseñado apra copiar como fuente una base de datos local, ustedes deben implementar el script para que lo copie desde su MongoDB Atlas.

3.- Crear un readme en github indicando los pasos(script) y los resultados obtenidos(capturas).

# Resolución (Descripción Paso a Paso)







# Evidencias:

1.- Creación de la DataBase

![atlas](https://user-images.githubusercontent.com/58041699/126088348-46783967-12ee-44ad-825d-e12581e0243a.JPG)

2.- Vinculación con la DataBase

![devel](https://user-images.githubusercontent.com/58041699/126088317-c55a06fe-179f-499f-8eff-d3c7c8a1305c.JPG)

3.- Conexión al Cluster desde MongoDB Compass

![Captura de pantalla 2021-07-18 234257](https://user-images.githubusercontent.com/58041699/126104207-885aeb83-8d59-4ce4-a7d9-42f56aff505b.png)

4.- Importación en una colección de varios data set de Kaggle realizada por cada integrante

![develop](https://user-images.githubusercontent.com/58041699/126105194-b0a4cc90-4d83-4d99-ac29-df8a9bf03d04.JPG)

# Pasos de la conexión de MongoDB con CouchDB:

1.- Asegurarse de tener instalado el driver PyMongo caso contrario instalarlo desde la terminal (el driver PyMongo permite extrar los datos)

![install](https://user-images.githubusercontent.com/58127103/126202577-4eeb19bf-3ece-40c4-8509-bd169eea5c39.png)

2.- Selección del método de conexión en este caso "Connect to application" y obtención de la cadena de conexión

![8a00c568-1dd0-4fb4-b21e-1f1189d36bf3](https://user-images.githubusercontent.com/58041699/126104495-c4a0fb79-8562-4352-bd51-ad7b8daa44f1.jpg)

3.- Selección del lenguaje con su respectiva versión

![f8523d2b-d6ea-4f85-92ed-3951178a0280](https://user-images.githubusercontent.com/58041699/126104525-e7517a7f-4633-4d10-9898-8f30614b8db6.jpg)

4.- Modificación de la cadena de conexión con las respectivas credenciales

![script](https://user-images.githubusercontent.com/58041699/126104624-e60c8f84-76a7-453a-b7c8-884c098ccef6.JPG)

5.- Funcionamiento correcto del scrip, se muestra los documentos que se van extrayendo de MongoDB

![resul](https://user-images.githubusercontent.com/58041699/126104784-7790158d-fcc1-464c-8b87-43966ed49320.JPG)

6.- Datos de MongoDB en CouchDB

![bd](https://user-images.githubusercontent.com/58041699/126104888-d1da2a49-640e-431f-b7a4-f34849bec915.JPG)

![4f52642b-04b1-416a-822b-92db44fdf5ca](https://user-images.githubusercontent.com/58041699/126105081-7f6d24ad-b10f-4662-8ae0-4d9b30ddb503.jpg)












