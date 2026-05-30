# ==========================================
# PROYECTO INTEGRADOR - Sistema de Estudiantes
# ==========================================

# ---------- FUNCIONES DE ARCHIVO ----------

def guardar_estudiante(nombre, edad, nota):
    """Guarda un estudiante en el archivo de texto."""
    with open("estudiantes.txt", "a") as archivo:
        archivo.write(f"{nombre},{edad},{nota}\n")
    print(f"Estudiante '{nombre}' registrado correctamente.")

def leer_estudiantes():
    """Lee y retorna todos los estudiantes del archivo."""
    try:
        with open("estudiantes.txt", "r") as archivo:
            lineas = archivo.readlines()
            estudiantes = []
            for linea in lineas:
                datos = linea.strip().split(",")
                estudiantes.append({
                    "nombre": datos[0],
                    "edad": int(datos[1]),
                    "nota": float(datos[2])
                })
            return estudiantes
    except FileNotFoundError:
        return []

# ---------- FUNCIONES DE OPERACIONES ----------

def mostrar_estudiantes():
    """Muestra todos los estudiantes registrados."""
    estudiantes = leer_estudiantes()
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return
    print("\n--- Lista de estudiantes ---")
    for i, e in enumerate(estudiantes):
        estado = "APROBADO" if e["nota"] >= 11 else "DESAPROBADO"
        print(f"  {i+1}. {e['nombre']} | Edad: {e['edad']} | Nota: {e['nota']} | {estado}")

def buscar_estudiante(nombre_buscar):
    """Busca un estudiante por nombre."""
    estudiantes = leer_estudiantes()
    encontrado = False
    for e in estudiantes:
        if e["nombre"].lower() == nombre_buscar.lower():
            estado = "APROBADO" if e["nota"] >= 11 else "DESAPROBADO"
            print(f"Encontrado: {e['nombre']} | Edad: {e['edad']} | Nota: {e['nota']} | {estado}")
            encontrado = True
    if not encontrado:
        print(f"No se encontró al estudiante '{nombre_buscar}'.")

def calcular_promedio_notas():
    """Calcula el promedio de notas de todos los estudiantes."""
    estudiantes = leer_estudiantes()
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return
    total = 0
    for e in estudiantes:
        total += e["nota"]
    promedio = total / len(estudiantes)
    print(f"Promedio general de notas: {promedio:.2f}")

def ordenar_por_nota():
    """Ordena y muestra los estudiantes de mayor a menor nota."""
    estudiantes = leer_estudiantes()
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return
    # Ordenamiento burbuja por nota descendente
    n = len(estudiantes)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if estudiantes[j]["nota"] < estudiantes[j+1]["nota"]:
                estudiantes[j], estudiantes[j+1] = estudiantes[j+1], estudiantes[j]
    print("\n--- Estudiantes ordenados por nota (mayor a menor) ---")
    for i, e in enumerate(estudiantes):
        estado = "APROBADO" if e["nota"] >= 11 else "DESAPROBADO"
        print(f"  {i+1}. {e['nombre']} | Nota: {e['nota']} | {estado}")

def ingresar_estudiante():
    """Solicita datos de un nuevo estudiante y lo guarda."""
    nombre = input("Nombre del estudiante: ")
    edad = int(input("Edad: "))
    nota = float(input("Nota (0-20): "))
    if nota < 0 or nota > 20:
        print("Nota inválida. Debe estar entre 0 y 20.")
        return
    guardar_estudiante(nombre, edad, nota)

# ---------- MENÚ PRINCIPAL ----------

def menu_principal():
    print("\n==========================================")
    print("  PROYECTO INTEGRADOR - Lab 7             ")
    print("  Sistema de Registro de Estudiantes      ")
    print("==========================================")

    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Registrar nuevo estudiante")
        print("2. Ver todos los estudiantes")
        print("3. Buscar estudiante por nombre")
        print("4. Ver promedio general de notas")
        print("5. Ver ranking por nota")
        print("6. Salir")

        opcion = input("\nElige una opción: ")

        if opcion == "1":
            ingresar_estudiante()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            buscar_estudiante(nombre)
        elif opcion == "4":
            calcular_promedio_notas()
        elif opcion == "5":
            ordenar_por_nota()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

menu_principal()