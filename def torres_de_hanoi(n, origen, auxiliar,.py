def torres_de_hanoi(n, origen, auxiliar, destino, contador):
   
    if n == 1:
        contador[0] += 1
        print(f"Movimiento {contador[0]}: Mover disco 1 de {origen} a {destino}")
    else:
        torres_de_hanoi(n-1, origen, destino, auxiliar, contador)
        contador[0] += 1
        print(f"Movimiento {contador[0]}: Mover disco {n} de {origen} a {destino}")
        torres_de_hanoi(n-1, auxiliar, origen, destino, contador)

# Uso pidiendo al usuario el número de discos:
try:
    n_discos = int(input("Ingrese el número de discos: "))
    if n_discos < 1 or n_discos > 20:
        print("El número de discos debe ser mayor o igual a 1 y menor que 20.")
    else:
        contador = [0]
        torres_de_hanoi(n_discos, 'A', 'B', 'C', contador)
except ValueError:
    print("Por favor, ingrese un número entero válido.")
