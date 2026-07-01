# Importación de funciones desde la librería sympy
from sympy import isprime, factorint

# Función que evalúa si un número es primo
def es_primo(n):
    return isprime(n)

# Función que descompone un número en factores primos
def descomponer_factores(n):
    return factorint(n)

# Mostrar mensaje de bienvenida
print("-"*61)
print("  Bienvenido/a al Evaluador de Números Primos y Compuestos!")
print("-"*61)

# Ciclo que solicita y valida la entrada del usuario
while True:
    try:
        # Convertir la entrada a entero
        numero = int(input("Por favor, ingresa un número entero positivo: "))
        
        # Verificar que el número sea mayor que cero
        if numero > 0:
            break  # Salir del ciclo si el número es válido
        else:
            print("Error: El número debe ser un entero mayor que cero")
    
    # Si la conversión falla (no es número entero), mostrar error
    except ValueError:
        print("Error: Ingresa solo números enteros. No se permiten letras, caracteres especiales ni decimales.")

# Evaluar si el número ingresado es primo
if es_primo(numero):
    print(f"\nEl número ingresado {numero} es PRIMO ya que solo es divisible entre 1 y entre sí mismo")
else: 
    # Si no es primo, mostrar factores primos
    print(f"\nEl número ingresado {numero} NO es primo.")
    print("Sus factores primos paso a paso:")

    # Obtener los factores y mostrarlos repetidos según su exponente
    factores = descomponer_factores(numero)
    for factor, exponente in factores.items():
        for temp in range(exponente):
            print(f"-> {factor}")