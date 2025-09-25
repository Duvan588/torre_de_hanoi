def torres_de_hanoi(n, origen, auxiliar, destino): #Usamos 3 torres, donde en la primera tendremos todos los 
    #discos, y la última sera donde se deben organizar, usaremos la segund como ayuda
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}") #Si solo tenemos un disco pues simplemente lo pasamos directamente a la última torre
    else:
        torres_de_hanoi(n-1, origen, destino, auxiliar) #para n discos diferentes a uno empezaremos moviento el disco superior a la torre auxiliar 

        print(f"Mover disco {n} de {origen} a {destino}") #luego movemos el disco más grande a la torre destino
        torres_de_hanoi(n-1, auxiliar, origen, destino) #y finalmente movemos los discos de la torre auxiliar a la torre destino

# Uso pidiendo al usuario el número de discos:

n_discos = int(input("Ingrese el número de discos: "))
torres_de_hanoi(n_discos, 'A', 'B', 'C') #A es la torre origen, B la auxiliar y C la destino
