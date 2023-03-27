import datetime


class DatatoJson(): 
    """
    Esta clase nos permite retornar un Json de datos
    """

    def insertData(self): 

        try : 
            #pedimos los datos  para ingresar     
            titleMovie =  input("enter title of movie"); 
            ageMovie   =  input("enter age of movie"); 
            direct = input("enter director of movie ");
            year = int(input("insert year: "))
            moth = int(input("insert moth: "))
            day = int(input("insert day: "))



            #convertimos en un objeto dic
            queryJson = {
                "titulo" : titleMovie , 
                "año"    : ageMovie , 
                "director" : direct , 
               "release_date": datetime.datetime(year, moth, day)
            } 
            #retornamos el diccionario 
            return queryJson ;    
                 
        except Exception as e: 
            print(e)
     

    def queryKeyValuetoJson(self): 
        import os 
        os.system("cls")
        multistring = """
        
        choose option  

            1. set for key value. 
            2. set all  collection movie.

        [ EXAMPLE ]

        example for update elemente  for key value 
  
        { "titulo" : "titlemovie" }
        { "año" : "ageMoview"} 
        { "director":  "director" }
        
        example element for collection 

        {
            "titulo" : titleMovie , 
            "año"    : ageMovie , 
            "director" : direct 
        } 
             >
        """;  

        
        try:   
            #imprimimos  el string de ejemplo 
            print(multistring);
            
            #le pedimos que opcion necesita 
            option = str(input()); 

            # dependiendo de la opcion  asi devolver el objeto dic 
            if option == "1": 
            
                keyupdate = input("enter value key");
                valuetoudpate = input("enter value");  

                return { keyupdate : valuetoudpate } 
            
            elif option == "2":
                return self.insertData()
            else: 
                print("this option does not exist pleas try agian.")
                
        except Exception  as e: 
            print(e) 
    
    #devuelve un json de Key value 
    def justforKeyvalue(self):
        try: 
        
                
            keyupdate = input("enter value key");
            valuetoudpate = input("enter value");  
            filterJson = { keyupdate : valuetoudpate } 
            return  filterJson 

        except Exception as e: 
            print(e)
      
    