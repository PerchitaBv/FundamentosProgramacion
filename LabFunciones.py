# Función 1: Saludo simple
def saludar(nombre):
    print(f"Hola, {nombre}! Bienvenido al laboratorio de funciones.")
# Función 2: Suma de dos números
def sumar(a, b):
    return a + b

# Función 3: Multiplicación de dos números
def multiplicar(a, b):
    return a * b

# Función 4: Verificar si un número es par o impar
def es_par(num):
    if num % 2 == 0:
        return "Par"
    else:
        return "Impar"
# Función 5: Ingresar datos del usuario
def ingresar_datos():
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    return nombre, edad
# Función 6: Calcular si es mayor de edad
def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False
# Función 7: Mostrar resultados del usuario
def mostrar_resultado(nombre, edad):
    mayor = es_mayor_de_edad(edad)
    if mayor:
        print(f"{nombre} tiene {edad} años y ES mayor de edad.")
    else:
        print(f"{nombre} tiene {edad} años y NO es mayor de edad.")
  
# --- MENÚ PRINCIPAL ---
def menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Saludar")
    print("2. Sumar dos números")
    print("3. Multiplicar dos números")
    print("4. Verificar par o impar")
    print("5. Verificar mayor de edad")
    print("6. Salir")

    opcion = input("\nElige una opción: ")

    if opcion == "1":
        nombre = input("Ingresa un nombre: ")
        saludar(nombre)
    elif opcion == "2":
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        print(f"Resultado: {sumar(a, b)}")
    elif opcion == "3":
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        print(f"Resultado: {multiplicar(a, b)}")
    elif opcion == "4":
        num = int(input("Ingresa un número: "))
        print(f"El número {num} es: {es_par(num)}")
    elif opcion == "5":
        nombre, edad = ingresar_datos()
        mostrar_resultado(nombre, edad)
    elif opcion == "6":
        print("Saliendo del programa...")
        return
    else:
        print("Opción no válida.")

    menu()

menu()