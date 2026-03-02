def mostrar_sala(asientos):
    """Muestra el estado de la sala de cine en formato de tabla."""
    print("Estado de la sala:")
    for fila in asientos:
        print(" ".join(map(str, fila)))  # Imprime cada fila con espacios entre asientos

def reservar_asiento(asientos, fila, columna):
    """Reserva un asiento en la sala de cine si está disponible."""
    if asientos[fila][columna] == 0:
        asientos[fila][columna] = 1
        print("¡Asiento reservado con éxito!")
    else:
        print("Lo siento, ese asiento ya está reservado.")

# Inicializar la matriz de asientos (0 = libre, 1 = reservado)
asientos = [[1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

# Bucle principal para interactuar con el usuario
while True:
    mostrar_sala(asientos)

    try:
        fila = int(input("Ingrese la fila (0 a 2): "))
        columna = int(input("Ingrese la columna (0 a 3): "))

        if 0 <= fila <= 2 and 0 <= columna <= 3:
            reservar_asiento(asientos, fila, columna)
        else:
            print("¡Fila o columna inválida! Intente de nuevo.")
    except ValueError:
        print("¡Entrada inválida! Debe ingresar números enteros.")

    continuar = input("¿Desea reservar otro asiento? (s/n): ")
    if continuar.lower() != 's':
        break

print("¡Gracias por usar nuestro sistema de reservas!")