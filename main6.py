# ==========================================
# main6.py - Programa principal
# ==========================================

from utils import (bienvenida, calcular_promedio, calcular_suma,
                   validar_email, es_mayor_de_edad, calcular_area_rectangulo)

def menu_principal():
    bienvenida()

    while True:
        print("\n========== LABORATORIO 6 ==========")
        print("1. Calcular promedio de dos números")
        print("2. Calcular suma de dos números")
        print("3. Validar correo electrónico")
        print("4. Verificar mayor de edad")
        print("5. Calcular área de un rectángulo")
        print("6. Salir")

        opcion = input("\nElige una opción: ")

        if opcion == "1":
            a = float(input("Número 1: "))
            b = float(input("Número 2: "))
            resultado = calcular_promedio(a, b)
            print(f"El promedio de {a} y {b} es: {resultado}")

        elif opcion == "2":
            a = float(input("Número 1: "))
            b = float(input("Número 2: "))
            resultado = calcular_suma(a, b)
            print(f"La suma de {a} y {b} es: {resultado}")

        elif opcion == "3":
            email = input("Ingresa un correo electrónico: ")
            if validar_email(email):
                print(f"'{email}' ES un correo válido.")
            else:
                print(f"'{email}' NO es un correo válido.")

        elif opcion == "4":
            edad = int(input("Ingresa una edad: "))
            if es_mayor_de_edad(edad):
                print(f"Con {edad} años ES mayor de edad.")
            else:
                print(f"Con {edad} años NO es mayor de edad.")

        elif opcion == "5":
            base = float(input("Base del rectángulo: "))
            altura = float(input("Altura del rectángulo: "))
            resultado = calcular_area_rectangulo(base, altura)
            print(f"El área del rectángulo es: {resultado}")

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_principal()