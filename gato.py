import random
import os 

RED = "\033[91m"
GREEN = "\033[92m"
WHITE = "\033[97m"
RESET = "\033[0m"
#colors = [RESET, RESET, RESET, RESET, RESET, RESET, RESET, RESET, RESET]
def limpiar():
    os.system("clear")

def imprimir_tablero(tablero,colors ):
    row_separator = "--------+-------+--------"
    empty_row = "        |       |        "
    def print_row(numbers):
        print(empty_row)
        print(f"    {numbers[0]}   |   {numbers[1]}   |   {numbers[2]}    ")
        print(empty_row)
    
    print_row([f"{colors[0]}{tablero[0]}{RESET}", f"{colors[1]}{tablero[1]}{RESET}", f"{colors[2]}{tablero[2]}{RESET}"])
    print(row_separator)
    print_row([f"{colors[3]}{tablero[3]}{RESET}", f"{colors[4]}{tablero[4]}{RESET}", f"{colors[5]}{tablero[5]}{RESET}"])
    print(row_separator)
    print_row([f"{colors[6]}{tablero[6]}{RESET}", f"{colors[7]}{tablero[7]}{RESET}", f"{colors[8]}{tablero[8]}{RESET}"])
    print("")

def verificar_ganador(tablero):
    combinaciones_ganadoras = [
        [tablero[0], tablero[1], tablero[2]],
        [tablero[3], tablero[4], tablero[5]],
        [tablero[6], tablero[7], tablero[8]],
        [tablero[0], tablero[3], tablero[6]],
        [tablero[1], tablero[4], tablero[7]],
        [tablero[2], tablero[5], tablero[8]],
        [tablero[0], tablero[4], tablero[8]],
        [tablero[2], tablero[4], tablero[6]],
    ]
    for combinacion in combinaciones_ganadoras:
        if combinacion[0] == combinacion[1] == combinacion[2]:
            return combinacion[0]
    return None

def jugar_contra_maquina():
    num = [1, 2, 3, 4, "X", 6, 7, 8, 9]
    colors = [RESET, RESET, RESET, RESET, RESET, RESET, RESET, RESET, RESET]
    colors[4] = RED

    terminado = False
    limpiar()
    print(f"{GREEN}Seleccionaste jugar contra la máquina{RESET}")
    imprimir_tablero(num, colors)
    
    
    while not terminado:
        numeros = [n for n in num if isinstance(n, int)]
        print("Te toca, casillas disponibles: ", numeros)
        
        if len(numeros) == 0:
            print("¡Es un empate!")
            break

        numero = int(input("¿A cuál le das?: "))
        if numero in num:
            num[num.index(numero)] = "O"

            #colors[colors(numero)] = RED
            colors[numero - 1] = GREEN

            limpiar()
            imprimir_tablero(num, colors)
            ganador = verificar_ganador(num)
            if ganador:
                print(f"¡{ganador} ha ganado!")
                return
            numeros = [n for n in num if isinstance(n, int)]
            if len(numeros) == 0:
                print("¡Es un empate!")
                break
          
            rango = random.choice(numeros)

            num[num.index(rango)] = "X"
            colors[rango - 1] = RED
            limpiar()
            imprimir_tablero(num, colors)
            
            ganador = verificar_ganador(num)
            if ganador:
                print(f"¡{ganador} ha ganado!")
                return
        else:
            print("Esa casilla ya está ocupada. Intenta de nuevo.")

def jugar_dos_personas():
    num2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    colors = [RESET, RESET, RESET, RESET, RESET, RESET, RESET, RESET, RESET]
    terminado = False
    turno = True
    limpiar()
    print(f"{GREEN}Seleccionaste jugar con dos personas{RESET}")
    imprimir_tablero(num2, colors)
    
    while not terminado:
        numeros = [n for n in num2 if isinstance(n, int)]
        print("Te toca, casillas disponibles: ", numeros)
        
        if len(numeros) == 0:
            print("¡Es un empate!")
            break

        select = int(input("Selecciona uno: "))
        if select in num2:
            letra = "O" if turno else "X"
            num2[num2.index(select)] = letra
            cel = RED if letra == "X" else GREEN
            colors[select - 1] = cel


            limpiar()
            imprimir_tablero(num2, colors)
            ganador = verificar_ganador(num2)
            if ganador:
                print(f"¡{ganador} ha ganado!")
                return
            turno = not turno
        else:
            print("Esa casilla ya está ocupada. Intenta de nuevo.")

def main():
    while True:
        limpiar()
        print("Juego del gato")
        jugar = int(input("¿Qué quieres jugar?\n1. Contra la máquina\n2. Dos jugadores\nEscribe 1 o 2: "))
        
        if jugar == 1:
            print("Seleccionaste jugar contra la máquina")
      
            jugar_contra_maquina()
        elif jugar == 2:
            print("Seleccionaste jugar con dos personas")
            jugar_dos_personas()
        else:
            print("Opción no válida. Intenta de nuevo.")
            continue
        
        volju = input("¿Quieres volver a jugar? (SI o no): ").strip().lower()
        
        limpiar()
        if volju != "si":
            print("¡Adiós!")
            break

if __name__ == "__main__":
    main()