# ==========================================
# utils.py - Funciones reutilizables
# ==========================================

import re

def bienvenida():
    """
    Muestra un mensaje de bienvenida al usuario.
    No recibe parámetros ni retorna valores.
    """
    print("==========================================")
    print("  Bienvenido al sistema de funciones      ")
    print("  Laboratorio 6 - Fundamentos de Prog.   ")
    print("==========================================")

def calcular_promedio(a, b):
    """
    Recibe dos números y retorna su promedio.
    Parámetros: a (número), b (número)
    Retorna: promedio (flotante)
    """
    return (a + b) / 2

def calcular_suma(a, b):
    """
    Recibe dos números y retorna su suma.
    Parámetros: a (número), b (número)
    Retorna: suma (flotante)
    """
    return a + b

def validar_email(texto):
    """
    Verifica si una cadena tiene formato de correo electrónico.
    Parámetros: texto (string)
    Retorna: True si es válido, False si no lo es
    """
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(patron, texto):
        return True
    else:
        return False

def es_mayor_de_edad(edad):
    """
    Verifica si una persona es mayor de edad.
    Parámetros: edad (entero)
    Retorna: True si edad >= 18, False si no
    """
    return edad >= 18

def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    Parámetros: base (número), altura (número)
    Retorna: área (flotante)
    """
    return base * altura