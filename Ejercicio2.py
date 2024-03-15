Info_alimentos = {}
Nombre_Alimento= input("Introduce el nombre del alimento: ")
Cantidad_gramos= input(("Ingresa la cantidad consumida en gramos: "))

Info_alimentos= {"Nombre Alimento": (Nombre_Alimento), 
               "Cantidad de gramos": (Cantidad_gramos),}
print (Info_alimentos)

Otro_Registro= input("Quieres introducit otro alimento? ")
if Otro_Registro == "si":
 Nombre_Alimento2= input("Introduce el nombre del alimento: ")
 Cantidad_gramos2= input(("Ingresa la cantidad consumida en gramos: "))

 Info_alimentos= {"Nombre Alimento": (Nombre_Alimento), 
               "Cantidad de gramos": (Cantidad_gramos),}
 Info_alimentos2= {"Nombre Alimento": (Nombre_Alimento2), 
               "Cantidad de gramos": (Cantidad_gramos2),}

 print (Info_alimentos, Info_alimentos2)



