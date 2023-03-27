
from CRUD import CRUD

class AppMenu: 
    """
    Esta clase es para la  implentacion del Menu 
    """
    def __init__(self) -> None:
           self.instanDabase = CRUD()


    def showOptionsMenu(self ):
          
          multiline_str = """
          Elegir una Opcion 
          1. Show all Collection of Movies
          2. ShoW for datatime 
          3. Add collection to Movies  
          4. Update Collection of Movie  
          5. Delete collection Movie
          6. Exit  
          """
          print(multiline_str);  
           
    def chooseOption(self , option ): 
       

        if option == "1": 
            self.instanDabase.listMovie(); 
        elif option == "2":
             self.instanDabase.showforDatatime();  
        elif option == "3": 
             self.instanDabase.addMovie(); 
        elif option == "4":
            counUpdateElemen = self.instanDabase.updateMovie() 
            print("Elemnte update " , counUpdateElemen )
        elif option =="5":
             self.instanDabase.deleteMovie()
        elif option == "exit": 
             exit 
            
            



if __name__ == '__main__':
    #instanciamos la clase  
    appmenu = AppMenu(); 
    appmenu.showOptionsMenu() 
    # pedimos una opcion 
    option = str(input("choose Option "));  
    appmenu.chooseOption(option);   


