# ==========================================
# ETAPA 1: Manipulación de cadenas
# ==========================================

def etapa1():
    print("\n--- ETAPA 1: Métodos de cadenas ---")
    
    texto = "Fundamentos de Programacion en Python y C#"
    print(f"Texto original: {texto}")
    
    # Subcadena
    sub = texto[0:12]
    print(f"Subcadena (0 al 12): {sub}")
    
    # Buscar palabra
    pos = texto.find("Python")
    print(f"Posición de 'Python': {pos}")
    
    # Reemplazar palabra
    nuevo = texto.replace("Python y C#", "Python")
    print(f"Texto reemplazado: {nuevo}")
    
    # Separar texto
    partes = texto.split(" ")
    print(f"Texto separado por espacios: {partes}")

# ==========================================
# ETAPA 2: Listas paralelas
# ==========================================

def etapa2():
    print("\n--- ETAPA 2: Listas paralelas ---")
    
    nombres = ["Carlos", "Ana", "Luis", "Maria", "Pedro"]
    edades  = [20, 17, 23, 15, 19]
    
    print("Lista de personas:")
    for i in range(len(nombres)):
        print(f"  {nombres[i]} - {edades[i]} años")
    
    # Buscar persona por nombre
    buscar = input("\nIngresa un nombre a buscar: ")
    encontrado = False
    for i in range(len(nombres)):
        if nombres[i].lower() == buscar.lower():
            print(f"{nombres[i]} tiene {edades[i]} años.")
            encontrado = True
            break
    if not encontrado:
        print(f"No se encontró a '{buscar}' en la lista.")

# ==========================================
# ETAPA 3: Estructura combinada
# ==========================================

def etapa3():
    print("\n--- ETAPA 3: Estructura combinada ---")
    
    usuarios = [
        {"nombre": "Carlos",  "email": "carlos@gmail.com",  "ciudad": "Lima"},
        {"nombre": "Ana",     "email": "ana@gmail.com",     "ciudad": "Trujillo"},
        {"nombre": "Luis",    "email": "luis@gmail.com",    "ciudad": "Lima"},
        {"nombre": "Maria",   "email": "maria@gmail.com",   "ciudad": "Arequipa"},
        {"nombre": "Pedro",   "email": "pedro@gmail.com",   "ciudad": "Trujillo"},
        {"nombre": "Sofia",   "email": "sofia@gmail.com",   "ciudad": "Lima"},
    ]
    
    print("Lista de usuarios:")
    for u in usuarios:
        print(f"  {u['nombre']} | {u['email']} | {u['ciudad']}")
    
    # Búsqueda por ciudad
    ciudad = input("\nIngresa una ciudad a buscar: ")
    print(f"\nUsuarios en {ciudad}:")
    encontrados = 0
    for u in usuarios:
        if u["ciudad"].lower() == ciudad.lower():
            print(f"  - {u['nombre']} ({u['email']})")
            encontrados += 1
    if encontrados == 0:
        print("  No se encontraron usuarios en esa ciudad.")

# ==========================================
# ETAPA 4: Ordenamiento alfabético
# ==========================================

def etapa4():
    print("\n--- ETAPA 4: Ordenamiento alfabético ---")
    
    nombres = ["Carlos", "Ana", "Luis", "Maria", "Pedro", "Sofia", "Bruno", "Valeria"]
    
    print(f"Lista original:    {nombres}")
    
    # Ordenamiento burbuja para cadenas
    lista_ord = nombres.copy()
    n = len(lista_ord)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista_ord[j] > lista_ord[j + 1]:
                lista_ord[j], lista_ord[j + 1] = lista_ord[j + 1], lista_ord[j]
    
    print(f"Lista ordenada:    {lista_ord}")

# ==========================================
# MENÚ PRINCIPAL
# ==========================================

def menu_principal():
    while True:
        print("\n========== LABORATORIO 4 ==========")
        print("1. Etapa 1 - Métodos de cadenas")
        print("2. Etapa 2 - Listas paralelas")
        print("3. Etapa 3 - Estructura combinada")
        print("4. Etapa 4 - Ordenamiento alfabético")
        print("5. Salir")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == "1":
            etapa1()
        elif opcion == "2":
            etapa2()
        elif opcion == "3":
            etapa3()
        elif opcion == "4":
            etapa4()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")
menu_principal()

