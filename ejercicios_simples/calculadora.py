# Pedir al usuario una operacion (suma, resta, multiplicacion, division) y dos numeros
# Ejecute la operacion y muestre el resultado
# Debe repetirse hasta que el usuario escriba "salir" como operacion

def operaciones(operacion, numero1, numero2):
    if operacion == 1:
        return numero1 + numero2
    elif operacion == 2:
        return numero1 - numero2
    elif operacion == 3:
        return numero1 * numero2
    elif operacion == 4:
        if numero2 == 0:
            print("Error: No se puede dividir por cero")
            return None
        return numero1 / numero2
    else:
        print("Operacion no valida")
        return None

def procedimiento():
    while True:
        operacion = input("Ingrese la operacion: ")
        
        if operacion == "salir":
            print("¡Hasta luego!")
            break
        
        numero1 = float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))
        resultado = operaciones(int(operacion), numero1, numero2)
        
        if resultado is not None:
            print("El resultado de la operacion es: ", resultado)


if __name__ == "__main__":
    print("Calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    procedimiento()