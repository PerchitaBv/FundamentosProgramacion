# ==========================================
# ETAPA 1: Listas unidimensionales
# ==========================================

def etapa1():
    print("\n--- ETAPA 1: Lista unidimensional ---")
    
    # 1. Declarar e inicializar lista de 10 elementos
    lista = [15, 42, 8, 73, 29, 56, 11, 88, 34, 67]
    
    # 2. Recorrer e imprimir todos los elementos
    print("Lista original:")
    for i in range(len(lista)):
        print(f"  Posición {i}: {lista[i]}")
    
    # 3. Modificar el tercer elemento
    nuevo_valor = int(input("\nIngresa un nuevo valor para la posición 2: "))
    lista[2] = nuevo_valor
    print(f"Lista actualizada: {lista}")
    
    # 4. Buscar un número
    buscar = int(input("\nIngresa un número a buscar: "))
    if buscar in lista:
        print(f"El número {buscar} SÍ existe en la lista.")
    else:
        print(f"El número {buscar} NO existe en la lista.")

# ==========================================
# ETAPA 2: Matriz 3x3
# ==========================================

def etapa2():
    print("\n--- ETAPA 2: Matriz 3x3 ---")
    
    # Inicializar matriz vacía
    matriz = []
    
    # Llenar la matriz con datos del usuario
    print("Ingresa los 9 valores de la matriz (fila por fila):")
    for i in range(3):
        fila = []
        for j in range(3):
            valor = int(input(f"  Posición [{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    
    # Mostrar la matriz
    print("\nMatriz ingresada:")
    for fila in matriz:
        print(f"  {fila}")
    
    # Calcular suma total
    suma = 0
    for fila in matriz:
        for elemento in fila:
            suma += elemento
    print(f"\nSuma total de todos los elementos: {suma}")

# ==========================================
# ETAPA 3: Menú de operaciones sobre lista
# ==========================================

def etapa3():
    print("\n--- ETAPA 3: Operaciones sobre lista dinámica ---")
    lista = [10, 20, 30, 40, 50]
    
    while True:
        print("\n-- Menú de operaciones --")
        print("1. Insertar elemento al final")
        print("2. Eliminar elemento por posición")
        print("3. Buscar valor y mostrar posición")
        print("4. Mostrar lista actualizada")
        print("5. Volver al menú principal")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            valor = int(input("Valor a insertar: "))
            lista.append(valor)
            print(f"Lista actualizada: {lista}")
        elif opcion == "2":
            pos = int(input("Posición a eliminar: "))
            if 0 <= pos < len(lista):
                eliminado = lista.pop(pos)
                print(f"Elemento {eliminado} eliminado. Lista: {lista}")
            else:
                print("Posición inválida.")
        elif opcion == "3":
            valor = int(input("Valor a buscar: "))
            if valor in lista:
                print(f"El valor {valor} está en la posición {lista.index(valor)}")
            else:
                print(f"El valor {valor} no está en la lista.")
        elif opcion == "4":
            print(f"Lista actual: {lista}")
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

# ==========================================
# ETAPA 4: Algoritmos de ordenamiento
# ==========================================

def burbuja(lista):
    lista = lista.copy()
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def seleccion(lista):
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def etapa4():
    print("\n--- ETAPA 4: Algoritmos de ordenamiento ---")
    lista = [64, 25, 12, 45, 78, 33, 9, 51]
    
    print(f"Lista original:          {lista}")
    print(f"Ordenamiento burbuja:    {burbuja(lista)}")
    print(f"Ordenamiento selección:  {seleccion(lista)}")
    print("\nAmbos algoritmos producen el mismo resultado ordenado.")
    print("Diferencia: burbuja compara elementos adyacentes,")
    print("selección busca el menor elemento en cada pasada.")

# ==========================================
# MENÚ PRINCIPAL
# ==========================================

def menu_principal():
    while True:
        print("\n========== LABORATORIO 3 ==========")
        print("1. Etapa 1 - Lista unidimensional")
        print("2. Etapa 2 - Matriz 3x3")
        print("3. Etapa 3 - Operaciones sobre lista")
        print("4. Etapa 4 - Algoritmos de ordenamiento")
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