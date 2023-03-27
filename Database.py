import pymongo 


class DbConnetcMongoDB: 
    
    """
    Esta clase nos permite  hacer la coneccion 
    """

    def __init__(self) -> None:
        connectionString = "mongodb://localhost:27017";
        self.mongclient = pymongo.MongoClient(connectionString);
        self.db = None;  
         
    
    def selectDataBase(self , nameDataBaseMongoDB):
      
        return self.mongclient[nameDataBaseMongoDB]; 
        
    
    def selectCollection(self , database ,collection):
       collection =  database[collection]  
       return  collection;  


       