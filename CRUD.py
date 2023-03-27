import datetime
import bson
from  Database import DbConnetcMongoDB
from utilis import DatatoJson; 


class CRUD: 
    """
    Esta clase nos permetira hacer las operaciones basicas CRUD  
    """

    def __init__(self) -> None:
       # instanciamos la conecion de base de mongoDB 
       connectionDb =  DbConnetcMongoDB()
       database = connectionDb.selectDataBase('sis11a-v-prueba')
       self.collection = connectionDb.selectCollection( database, "Movies") 
       #instanciamos el convert data to json  
       self.datatojson = DatatoJson(); 
    


    def listMovie(self)->None:
        try: 
            option   = input(""" 
                1. SHOW ALL
                2. filter for other -->  """)
            
            if option == "1": 
                
                # Obtener todos los documentos de la colección
                documentos = self.collection.find()
                # Imprimir cada documento
                for documento in documentos:
                    print(documento)

            elif option == "2": 
                
                filterJson = self.datatojson.justforKeyvalue()
                documentos = self.collection.find(filterJson)
                # Imprimir cada documento
                for documento in documentos:
                    print(documento)
        except Exception as e: 
            print(e)
            

    #agregar peliculas             
    def addMovie(self):
        try:
            query = self.datatojson.insertData()

            result = self.collection.insert_one(query) 
            print("Todo Salio bien..."  , result.inserted_id)
        

        except Exception as e: 
            print(e)
 
    #actulizar pelicula 
    def updateMovie(self) -> int:

        try: 

            idToUpdate = input("Insert the ID to Update ")  
        
            opetator = input("insertar operatos  Default [$set] >  ")
        
            if opetator == '' : 
                opetator = "$set"
                myquery = self.datatojson.queryKeyValuetoJson() 
                newvalues = { opetator: myquery }
            else: 
                myquery = self.datatojson.queryKeyValuetoJson() 
                newvalues = { opetator: myquery }

            resultcounUpdate = self.collection.update_one({ "_id": bson.ObjectId(idToUpdate)}, newvalues).modified_count

            return resultcounUpdate; 

        except Exception as e :
            print(e)
             

    # eleminar pelicula 
    def  deleteMovie(self)->None: 

        try: 
            
            deleforId =  bson.ObjectId(input("enter the id to delete ")); 
            # Define a filter to match the document(s) you want to delete
            filter = {"_id": deleforId} 

            # Delete the first document that matches the filter
            result = self.collection.delete_one(filter).deleted_count

            print("id removed successfully ")

            return result; 

        except Exception as e : 

            print(e)


    def showforDatatime(self): 

            try:

                typefilter =input("Add type of filter default[$gt] ");  
                year = int(input("insert year: "))
                moth = int(input("insert moth: "))
                day = int(input("insert day: "))
                
                filter = None 
                if typefilter == '':
                    release_date = str(datetime.datetime(year, moth, day)) 
                    # Define a filter to match the documents you want to retrieve
                    filter = {"release_date": {"$gt": release_date }}

                else : 

                    release_date = str(datetime.datetime(year, moth, day)) 
                   # release_date_str = release_date.strftime('%Y-%m-%dT%H:%M:%S')

                    filter = {"release_date": { typefilter : release_date }}


                # Find all documents that match the filter and print them
                cursor = self.collection.find(filter)
   
                for document in cursor:
                    print(document)
                   

            except Exception as e: 
                print(e) 


         