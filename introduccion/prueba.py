print("Hola Mundo")

# Este bucle imprime los números del 0 al 10 en pantalla
for i in range(11):
    print(i)

# Lista de números primos menores de 100
primos = []
for num in range(2, 100):
    es_primo = True
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(num)

print("Estos son primos")
for primo in primos:
    print(primo)


# TODO: imprimir buenos dias
print("buenos dias")