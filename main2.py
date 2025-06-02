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
from datetime import datetime

def obtenerFechaActual():
    return datetime.now().strftime("%Y-%m-%d")


import os

def limpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')


def enterParaContinuar(mensaje: str = "Enter para continuar..."):
    input(mensaje)

def validarInput(titulo: str, valMin: int = 0, valMax: int = 5):
    while True:
        try:
            res = int(input(f'{titulo}'))
            if res >= valMin and res <= valMax:
                return res
            else:
                print(f"Por favor ingrese solo valores permitidos....\nRango de {valMin} a {valMax}")
                enterParaContinuar()
                limpiarConsola()
        except:
            enterParaContinuar("Oiga mano NO sea toche 😝!!!\nEnter para continuar")

def GestionDelibros(titulo: str):
    limpiarConsola()
    while True:
        limpiarConsola()
        print(titulo)
        option = validarInput("Seleccione una opcion: ", valMin= 1, valMax= 4)
        if option == 1:
            print("\n--- Agregar nuevo libro ---")
            codigo = input("Ingrese código del libro: ")
            nombre = input("Ingrese nombre del libro: ")
            autor = input("Ingrese autor del libro: ")
            editorial = input("Ingrese editorial del libro: ")
            nuevo_libro = {
            "codigo": codigo,
            "nombre": nombre,
            "autor": autor,
            "editorial": editorial
            }
            biblioteca["libros"].append(nuevo_libro)
            print(f"\nLibro '{nombre}' agregado correctamente.\n")
            enterParaContinuar()
            pass
        elif option == 2:
            codigo_buscar = input("\nIngrese el código del libro a actualizar: ")
            # Buscar el libro en la lista
            for libro in biblioteca["libros"]:
                if libro["codigo"] == codigo_buscar:
                    print(f"Libro encontrado: {libro['nombre']} de {libro['autor']}")
                    print("\n--- Escriba el nuevo valor o presione Enter para no cambiar ---")
                    # Pedir nuevos datos (puedes dejar en blanco para no cambiar)
                    nuevo_nombre = input("Nuevo nombre: ")
                    nuevo_autor = input("Nuevo autor: ")
                    nueva_editorial = input("Nueva editorial: ")
                    
                    # Actualizar solo si se ingresó un dato
                    if nuevo_nombre.strip() != "":
                        libro["nombre"] = nuevo_nombre
                    if nuevo_autor.strip() != "":
                        libro["autor"] = nuevo_autor
                    if nueva_editorial.strip() != "":
                        libro["editorial"] = nueva_editorial
                    
                    print("\nLibro actualizado correctamente.\n")
                    return
            print("No se encontró ningún libro con ese código.\n")
            enterParaContinuar()
            pass
        elif option == 3:
            print("\n--- Eliminar libro ---")
            codigo_buscar = input("\nIngrese el código del libro que deseas eliminar: ")
            for libro in biblioteca["libros"]:
                if libro["codigo"] == codigo_buscar:
                    print(f"\nLibro encontrado: {libro['nombre']} de {libro['autor']}")
                    confirmacion = input("¿Está seguro que desea eliminar este libro? (si/no): ").lower()
                    if confirmacion == "si":
                        biblioteca["libros"].remove(libro)
                        print(" Libro eliminado correctamente.\n")
                    else:
                        print(" Operación cancelada.\n")
                    return
            print(" No se encontró ningún libro con ese código.\n")
            enterParaContinuar()
            pass
        elif option == 4:
            break

def listarLibros():
    print("\n--- Lista de Libros ---")
    if not biblioteca["libros"]:
        print("No hay libros registrados.")
    else:
        for libro in biblioteca["libros"]:
            print(f"Código: {libro['codigo']}, Nombre: {libro['nombre']}, Autor: {libro['autor']}, Editorial: {libro['editorial']}")
    print()
    enterParaContinuar("Enter Para salir...")

def prestarLibro():
    print("\n--- Préstamo de Libro ---")
    try:
        codigo_buscar = input("\nIngrese el código del libro a prestar: ")
    except:
            enterParaContinuar("Oiga mano NO sea toche 😝!!!\nEnter para continuar")
            
    # Verificar si el libro existe
    libro_encontrado = None
    for libro in biblioteca["libros"]:
        if libro["codigo"] == codigo_buscar:
            libro_encontrado = libro
            break

    if not libro_encontrado:
        print(" El libro no existe en la biblioteca.\n")
        enterParaContinuar()
        return
    

    # Verificar si ya está prestado (sin devolución)
    for prestamo in biblioteca["prestamos"]:
        if prestamo["codigo"] == codigo_buscar and prestamo["devolucion"] is None:
            print(" El libro ya está prestado y no ha sido devuelto.\n")
            enterParaContinuar()
            return
        

    # Pedir datos del estudiante
    nombre = input("Ingrese el nombre del estudiante: ")
    documento = input("Ingrese el número de documento: ")

    prestamo = {
        "codigo": codigo_buscar,
        "fecha": obtenerFechaActual(),
        "devolucion": None,
        "nombre": nombre,
        "documento": documento
    }

    biblioteca["prestamos"].append(prestamo)
    biblioteca["historial"].append(prestamo)  # Guardar copia en historial

    print(" Préstamo registrado exitosamente.\n")
    enterParaContinuar()

def mostrarHistorial():
    print("\n --- Historial de Préstamos ---")
    
    if not biblioteca["historial"]:
        print("No hay préstamos registrados.\n")
        enterParaContinuar()
        return

    for prestamo in biblioteca["historial"]:
        codigo = prestamo["codigo"]
        fecha = prestamo["fecha"]
        devolucion = prestamo["devolucion"] if prestamo["devolucion"] else "No devuelto"
        nombre = prestamo["nombre"]
        documento = prestamo["documento"]

        print(f"Código: {codigo} | Fecha préstamo: {fecha} | Devolución: {devolucion}")
        print(f"Estudiante: {nombre} - Documento: {documento}")
        print("-" * 50)
    
    print()
    enterParaContinuar()

def listarLibrosPrestados():
    print("\n --- Libros Prestados (No devueltos) ---")

    prestamos_activos = [p for p in biblioteca["prestamos"] if p["devolucion"] is None]

    if not prestamos_activos:
        print("No hay libros prestados actualmente.\n")
        enterParaContinuar()
        return

    for prestamo in prestamos_activos:
        codigo = prestamo["codigo"]
        nombre = prestamo["nombre"]
        documento = prestamo["documento"]
        fecha = prestamo["fecha"]

        print(f"Código: {codigo} | Estudiante: {nombre} | Documento: {documento} | Fecha de préstamo: {fecha}")
    
    print()
    enterParaContinuar()

def devolverLibro():
    print("\n --- Devolución de Libro ---")
    codigo_buscar = input("Ingrese el código del libro a devolver: ")

    # Buscar préstamo activo (devolucion == None)
    for prestamo in biblioteca["prestamos"]:
        if prestamo["codigo"] == codigo_buscar and prestamo["devolucion"] is None:
            prestamo["devolucion"] = obtenerFechaActual()
            print(" Libro devuelto exitosamente.\n")
            enterParaContinuar()
            return
    
    print(" No se encontró un préstamo activo para ese código.\n")
    enterParaContinuar()

            
menuTitle ="""
 _____                                        _____ 
( ___ )--------------------------------------( ___ )
 |   |                                        |   | 
 |   | ███╗   ███╗███████╗███╗   ██╗██╗   ██╗ |   | 
 |   | ████╗ ████║██╔════╝████╗  ██║██║   ██║ |   | 
 |   | ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║ |   | 
 |   | ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║ |   | 
 |   | ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝ |   | 
 |   | ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝  |   | 
 |___|                                        |___| 
(_____)--------------------------------------(_____)
"""
menuOptions ="""
    1. Gestion de Libros 
    2. Prestamo de Libros 
    3. Devolucion de Libros 
    4. Listar Libros 
    5. Listar Libros Prestados 
    6. Historial de prestamos 
    7. Salir 
"""
subMenuOptions ="""
    MENU - Gestion Libros 
    1. Agregar 
    2. Actualizar 
    3. Eliminar 
    4. Salir
"""
biblioteca = {
    "libros": [],
    "prestamos": [],
    "historial": [],
    "devolucion": []
}

while True:
    limpiarConsola()
    print(menuTitle)
    print(menuOptions)
    respuesta = validarInput(valMax=7, valMin=1, titulo="Seleccione una opcion:\n --> ")
    if respuesta == 1:
       GestionDelibros(titulo=subMenuOptions)
       pass
    elif respuesta == 2:
        prestarLibro()
        pass
    elif respuesta == 3:
        devolverLibro()
        pass
    elif respuesta == 4:
        listarLibros()
        pass
    elif respuesta == 5:
        listarLibrosPrestados()
        pass
    elif respuesta == 6:
        mostrarHistorial()
        pass
    elif respuesta == 7:
        enterParaContinuar("Hasta la luego !!!\nEnter para continuar")
        break
    else:
        enterParaContinuar("Oiga mano NO sea toche 😝!!!\nEnter para continuar")
    limpiarConsola()

