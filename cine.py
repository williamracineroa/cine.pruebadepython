filas= 8 
columnas= 10
sala= []

for i in range (filas):
    filas= []
    for h in range (columnas):
        filas.append("_")
    sala.append(filas)
    
w=1
while w==1:
    
    print ("_______________________")
    print ("------- MENU ---------")
    print ("1. si desea reservar un puesto")
    print ("2. si desea salir")
    
    num_opcion=int(input("ingrese el nuemro de la accion que desea realizar"))

    if num_opcion==1:
            fila_puesto=int(input("ingresa el numero de la fila que deseas reservar(0-7):"))
            columna_puesto=int(input("ingrese la columna donde desea sentarse(0-9):"))
            
            
            if sala[fila_puesto][columna_puesto]== "_":
                
                sala[fila_puesto][columna_puesto]="x"
                print("asiento reservado")
                for filas in sala :
                    print(filas)
            elif sala[fila_puesto][columna_puesto]=="x":
                print("asiento ocupado intente con otro")
                for filas in sala :
                    print(filas)
                
            elif num_opcion == 2:
                print("gracias por usar nuestro servicio")
                
            else:
                print ("ingrese un valor valido del menu")