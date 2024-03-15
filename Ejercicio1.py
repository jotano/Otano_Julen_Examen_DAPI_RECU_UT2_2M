import os 
def OrdenarLista(file_path):
    """
    La siguiente función recibe una lista de números enteros
    y los escribe en un fichero llamado ListaOrdenadas.txt.
    La función no devuelve nada.
    """
    
    if not os.path.isfile("ListaOrdenada.txt"):
        with open("ListaOrdenada.txt","w") as file:
            file.write("1\t 2\t 3\t 4\t \n")
    if os.path.isfile("ListaOrdenada.txt"):
        with open("ListaOrdenada.txt","w") as file:
            file.write("1\t 2\t 3\t 4\t \n")

file_path = "ListaOrdenada.txt"
OrdenarLista(file_path) 
           

def NumeroPar(file_path): 
    """
    Esta función abrirá un fichero que contendrá una lista 
    ordenada de números, lo leerá y escribirá en otro 
    fichero llamado ListaDePares.txt
    """
    
    if not os.path.isfile("ListaOrdenada.txt"):
        with open("ListaOrdenada.txt","w") as file:
            file.write("1\t 2\t 3\t 4\t \n")
    if os.path.isfile("ListaOrdenada.txt"):
       with open("ListaOrdenada.txt","r") as file:
           lines = file.readlines()
           if "2" or "4" in "ListaOrdenada.txt":
               with open("ListaDePares.txt","w") as file:
                   file.write ("2\t 4\t")
                   
file_path2 = "ListaDePares.txt"
NumeroPar(file_path2)



       
          




            

