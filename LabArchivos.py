# ==========================================
# ETAPA 1: Escribir y leer archivo de texto
# ==========================================

def escribir_contacto(nombre, telefono):
    with open("contactos.txt", "a") as archivo:
        archivo.write(f"{nombre},{telefono}\n")
    print(f"Contacto '{nombre}' guardado correctamente.")

def leer_contactos():
    print("\n--- Lista de contactos ---")
    try:
        with open("contactos.txt", "r") as archivo:
            lineas = archivo.readlines()
            if len(lineas) == 0:
                print("No hay contactos registrados.")
            else:
                for i, linea in enumerate(lineas):
                    datos = linea.strip().split(",")
                    print(f"  {i+1}. Nombre: {datos[0]} | Teléfono: {datos[1]}")
    except FileNotFoundError:
        print("No existe el archivo todavía.")

# ==========================================
# ETAPA 2: Ingresar datos y buscar contacto
# ==========================================

def ingresar_contacto():
    nombre = input("Nombre del contacto: ")
    telefono = input("Teléfono del contacto: ")
    escribir_contacto(nombre, telefono)

def buscar_contacto(nombre_buscar):
    print(f"\n--- Buscando '{nombre_buscar}' ---")
    try:
        with open("contactos.txt", "r") as archivo:
            lineas = archivo.readlines()
            encontrado = False
            for linea in lineas:
                datos = linea.strip().split(",")
                if datos[0].lower() == nombre_buscar.lower():
                    print(f"Encontrado: Nombre: {datos[0]} | Teléfono: {datos[1]}")
                    encontrado = True
            if not encontrado:
                print("Contacto no encontrado.")
    except FileNotFoundError:
        print("No existe el archivo todavía.")

def contar_contactos():
    try:
        with open("contactos.txt", "r") as archivo:
            lineas = archivo.readlines()
            print(f"\nTotal de contactos registrados: {len(lineas)}")
    except FileNotFoundError:
        print("No existe el archivo todavía.")

# ==========================================
# MENÚ PRINCIPAL
# ==========================================

def menu_principal():
    while True:
        print("\n========== LABORATORIO 5 ==========")
        print("1. Agregar contacto")
        print("2. Ver todos los contactos")
        print("3. Buscar contacto por nombre")
        print("4. Contar contactos")
        print("5. Salir")

        opcion = input("\nElige una opción: ")

        if opcion == "1":
            ingresar_contacto()
        elif opcion == "2":
            leer_contactos()
        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            buscar_contacto(nombre)
        elif opcion == "4":
            contar_contactos()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

menu_principal()