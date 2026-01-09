# Recorrer números del 1 al 50
# Si el numero es multiple de 3 imprime Fizz
# Si el numero es multiple de 5 imprime Buzz
# Si el numero es multiple de 3 y 5 imprime FizzBuzz
# Y si no, imprime el numero

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
