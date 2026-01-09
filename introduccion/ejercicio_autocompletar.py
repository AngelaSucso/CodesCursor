import random

def juego_adivinar_numero():
    """
    Juego donde el usuario debe adivinar un número del 1 al 100.
    El programa da pistas 'mayor' o 'menor' según corresponda.
    """
    numero_secreto = random.randint(1, 100)
    intentos = 0
    
    print("=" * 50)
    print("¡Bienvenido al juego de adivinar el número!")
    print("=" * 50)
    print("He pensado en un número entre 1 y 100.")
    print("¡Intenta adivinarlo!")
    print("-" * 50)
    
    while True:
        try:
            # Solicitar al usuario que ingrese un número
            intento = int(input("\nIngresa tu número: "))
            intentos += 1
            
            # Verificar si el número es válido (entre 1 y 100)
            if intento < 1 or intento > 100:
                print("Por favor, ingresa un número entre 1 y 100.")
                continue
            
            # Comparar el intento con el número secreto
            if intento < numero_secreto:
                print(f"❌ El número es MAYOR que {intento}")
            elif intento > numero_secreto:
                print(f"❌ El número es MENOR que {intento}")
            else:
                print("\n" + "=" * 50)
                print(f"¡🎉 FELICIDADES! 🎉 Has adivinado el número!")
                print(f"El número secreto era: {numero_secreto}")
                print(f"Lo lograste en {intentos} intento(s)")
                print("=" * 50)
                break
                
        except ValueError:
            print("❌ Por favor, ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n\n¡Juego cancelado! Hasta luego.")
            break

if __name__ == "__main__":
    juego_adivinar_numero()
