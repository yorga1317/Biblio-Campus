#Blblio Campus
    #Gestion Libros 
        #agregar 
        #Actualizar
        #Eliminar
    #Prestamo de libro 
        #crear
    #devolucion de libros
        #crear
    #lista libros
    #lista libros prestados
        # lista solo los libros que no tienen devolucion 
    #Historial de prestamos
        #listado
    #Salir

#Realizar en modulos (Pendiente)
#LIbro --> Codigo, Nombre; Autor; Editorial.
#Prestamo --> Fecha, Devolucion, Nombre, Documento.
#Historial -> [Prestamos]
import os
def limpiarConsola():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def opciones( opcion: str = "Ingrese la opcion: \n --> "):
    return input(opcion)

def enterParaContinuar(mensaje: str = "Enter para continuar..."):
    input(mensaje)

'''def validarInput(titulo: str, valMin: int = 0, valMax: int = 5):
    while True:
        try:
            res = int(input(f"{titulo}: \n"))
            if res >= valMin and res <= valMax:
                return res
            else:
                print(f"Por favor ingrese solo valores permitidos...\n de {valMin} a {valMax}")
                enterParaContinuar()
                limpiarConsola()
        except:
            enterParaContinuar("oiga mano No sea toche 😝!!! \nEnter para continuar...")'''



menu = '''
 __  __ _____ _   _ _   _ 
|  \/  | ____| \ | | | | |
| |\/| |  _| |  \| | | | |
| |  | | |___| |\  | |_| |
|_|  |_|_____|_| \_|\___/ 

1. Gestion Libros 
2. Prestamo de libro 
3. devolucion de libros
4. Lista libros
5. Lista libros prestados
6. Historial de prestamos
7. Salir
'''
subMenu = '''
MENU - Gestion Libros
1. Agregar
2. Actualizar
3. Eliminar
'''
MeEquivoque ='''
1. Continuar
2. Regresar
'''

Biblioteca = {
  "libro" : [],
  "prestados" : [],
  "historial" : [],
}

    
while True:
    print(menu)
    respuesta = opciones()
    limpiarConsola()
    if respuesta == "1":
        print(MeEquivoque)
        respuesta = opciones()
        if respuesta == "1":
            print("hola")
            enterParaContinuar()
        elif respuesta == "2":
            enterParaContinuar()        
    elif respuesta == "2":
        print(MeEquivoque)
        respuesta = opciones()
        if respuesta == "1":
            print("hola")
            enterParaContinuar()
        elif respuesta == "2":
            enterParaContinuar()      
    elif respuesta == "3":
        pass
    elif respuesta == "4":
        pass
    elif respuesta == "5":
        pass
    elif respuesta == "6":
        pass
    elif respuesta == "7":
        pass
    else: 
        print("La opcion que ingreso fue incorrecta ")
        input("Continiar.. presione enter ")
