# -*- coding: cp1252 -*-

CABECERAS = []
TABLERO_VACIO = []
ANCHO = 7
LARGO = 6
FICHA_1 = "X"
FICHA_2 = "O"
FICHA_VACIA = "_"
CONDICION_GANAR = 4
MAXIMOS_INTENTOS = 42
ERROR_1 = "Accion inválida!, por favor indique un número entero"
ERROR_2 = "El numero debe estar dentro del rango!"
ERROR_3 = "Columna llena, vuelva a escojer!"
MENSAJE_1 = "felicitaciones!, ganaste"
MENSAJE_2 = "Empate!"
def multiplicar_caracteres(caracter):
    # Esta funcion la necesito para que no se rompa mi funcion mostrar_tablero
    """Esta funcion lo que hace es tomar un caracter y lo repite
    tantas veces como el ancho."""
    return caracter*ANCHO
F = multiplicar_caracteres("{} ")
# Esta constante la utilizo en mostrar_tablero para poder dar el formato al tablero

def generar_tablero(tablero):
    """Recibe una lista(que debería estar vacía) y
    devuelve un tablero (o una matriz) de ancho x alto"""
    for x in range(LARGO):
        tablero.append([(FICHA_VACIA)]*ANCHO)
    return tablero

def generar_cabeceras(cabecera):
    """Recibe una lista vacía, y devuelve una cabecera
    de valores 1, 2, ..., ANCHO+1"""
    for x in range(1,ANCHO+1):
        cabecera.append(x)
    return cabecera

def mostrar_tablero(tablero):
    """Imprime en pantalla el tablero"""
    
    print(F.format(*CABECERAS))
    for fila in tablero:
        print(F.format(*fila))

def pedir_nombres():
    """Pide al usuario que ingrese dos nombres y los devuelve"""
    
    nombre_1 = raw_input("Indique el nombre del primer jugador: ")
    nombre_2 = raw_input("Indique el nombre del segundo jugador: ")
    return nombre_1,nombre_2


def ganar_vertical(tablero):
    """Esta funcion recorre el tablero en direccion vertical, y si encuentra 4
    valores identicos seguidos, distintos al vacio, devuelve True"""
    
    for columna in range(0,ANCHO):
        for fila in range(0,LARGO/2):
            contador_vertical = 1
            # Para que se resetee el contador una vez que cambia de columna
            for desplazamiento in range (1,CONDICION_GANAR):
            # Compara hasta con el tercer elemento delante(verticalmente)
                if (tablero[fila][columna]\
                    != tablero[fila+desplazamiento][columna])\
                    or tablero[fila][columna] == FICHA_VACIA:
                    contador_vertical = 1
                if tablero[fila][columna]\
                   == tablero[fila+desplazamiento][columna]:
                    contador_vertical+=1
                if contador_vertical == CONDICION_GANAR:
                    return True

def ganar_horizontal(tablero):
    """Esta funcion recorre el tablero en direccion horizontal, y si encuentra
    4 valores identicos seguidos, distintos al vacio, devuelve True"""
    
    for fila in range(0,LARGO): 
        contador_horizontal = 1
        # Para que el contador se resetee una vez que se cambia de fila
        for columna in range(0,(ANCHO/2) + 1): 
            for desplazamiento in range (1,CONDICION_GANAR):
                # Compara hasta con el tercer elemento delante(horizontalmente)
                if (tablero[fila][columna]\
                    != tablero[fila][columna+desplazamiento])\
                    or tablero[fila][columna] == FICHA_VACIA:
                    contador_horizontal = 1
                if tablero[fila][columna]\
                   == tablero[fila][columna+desplazamiento]:
                    contador_horizontal+=1
                if contador_horizontal == CONDICION_GANAR:
                    return True
    
def ganar_diagonal_derecha(tablero):
    """Esta funcion recorre el tablero en direccion diagonal hacia la
    derecha, y si encuentra 4 valores identicos, distintos al
    vacio, devuelve True
    """
    
    for columna in range(0,(ANCHO/2)+1): 
        contador_diagonal_derecha = 1
        # Para que se resetee el contador una vez que cambia de columna
        for fila in range(0,LARGO/2): 
            contador_diagonal_derecha = 1
            # Para que el contador se resetee una vez que se cambia de fila
            for desplazamiento in range (1,CONDICION_GANAR):
                # Compara hasta con el tercer elemento delante(diagonalmente)
                if (tablero[fila][columna]\
                    != tablero[fila+desplazamiento][columna+desplazamiento])\
                    or tablero[fila][columna] == FICHA_VACIA:
                    contador_diagonal_derecha = 1
                if tablero[fila][columna]\
                   == tablero[fila+desplazamiento][columna+desplazamiento]:
                    contador_diagonal_derecha+=1
                if contador_diagonal_derecha == CONDICION_GANAR:
                    return True
                    
def ganar_diagonal_izquierda(tablero):
    """Esta funcion recorre el tablero en direccion diagonal hacia la
    izquierda, y si encuentra 4 valores identicos seguidos, distintos al
    vacio, devuelve True
    """
    
    for fila in range(0,LARGO/2):
       
        contador_diagonal_izquierda = 1
        # Para que se resetee el contador una vez que cambia de columna
        for columna in range(0,(ANCHO/2)+1):
            contador_diagonal_izquierda = 1
            # Para que el contador se resetee una vez que se cambia de fila
            for desplazamiento in range (1,CONDICION_GANAR):
                # Compara hasta con el tercer elemento delante(diagonalmente)
                if (tablero[fila][-columna-1]\
                    != tablero[fila+desplazamiento][-columna-desplazamiento-1])\
                    or tablero[fila][-columna-1] == FICHA_VACIA:
                    contador_diagonal_izquierda = 1
                if tablero[fila][-columna-1]\
                   == tablero[fila+desplazamiento][-columna-desplazamiento-1]:
                    contador_diagonal_izquierda+=1
                if contador_diagonal_izquierda == CONDICION_GANAR:
                    return True

def hay_ganador(tablero):
    """Composicion de las funciones ganar_diagonal2, ganar_diagonal1,
    ganar_vertical y ganar_horizontal, en definitiva, si se
    cumple alguna de las anteriores, devuelve "Ganar"
    """
    
    if ganar_diagonal_izquierda(tablero) or ganar_diagonal_derecha(tablero)\
       or ganar_vertical(tablero) or ganar_horizontal(tablero):
        return True
    
def empate(contador,tablero):
    """Recibe un contador y un tablero, si coincide el contador con la
    constante, mientras la ultima accion no halla completado el
    tablero de forma que se cumple alguna condicion para ganar,
    devuelve True
    """
    if contador == MAXIMOS_INTENTOS and not(hay_ganador(tablero)):
        return True


def jugada(tablero,jugador,ficha):
    """Funcion que describe como se lleva acabo una jugada individual,
    recibe un tablero, un jugador, y una ficha, "posicion_ficha" y
    "condicion" son centinelas para iniciar el ciclo del turno, siendo
    el centinela "condicion" el mas importante, ya que una vez que se
    realizo una accion valida, se cambia su valor y se detienee la
    funcion, devolviendo el tablero actualizado
    """
    posicion_ficha = "1"
    condicion = "seguir"
    while posicion_ficha.isdigit() and int(posicion_ficha) <= ANCHO\
          and condicion == "seguir":
        posicion_ficha =\
        raw_input\
        ("Jugador {}:escoja una columna para insertar la ficha : ".format(jugador))
        if posicion_ficha.isdigit():
            if int(posicion_ficha) <= ANCHO and int(posicion_ficha)>0:
                contador = 0
                for x in range(LARGO):
                    if tablero[-x-1][(int(posicion_ficha))-1] == FICHA_2\
                       or tablero[-x-1][(int(posicion_ficha))-1] == FICHA_1:
                        # Si la ficha esta ocupada, la ignora
                        contador+=1
                        continue
                    if tablero[-x-1][(int(posicion_ficha))-1] == FICHA_VACIA:
                        tablero[-x-1][(int(posicion_ficha))-1] = ficha
                        mostrar_tablero(tablero)
                        condicion = "siguiente"
                        break
                if contador ==LARGO:
                    print ERROR_3

            else:
                print ERROR_2
                posicion_ficha = "1"
                continue  
        else:
            print ERROR_1
            posicion_ficha = "1"
            continue
    return tablero

def ciclo_de_juego(tablero,jugador_x,jugador_y,ficha_x,ficha_y,contador_empate):
    """Recibe un tablero, dos jugadores, dos fichas y un contador de
    empate, para desarrollar la parte mas importante del juego,
    el ciclo del mismo, no devuelve nada, se interrumpe si se cumple
    alguna condicion de victoria/empate,    
    """
    while True:
        mostrar_tablero(tablero)
        jugada(tablero,jugador_x,ficha_x)
        contador_empate+=1
        if hay_ganador(tablero):
            print jugador_x,MENSAJE_1
            break
        if empate(contador_empate,tablero):
            print MENSAJE_2
            break
        jugada(tablero,jugador_y,ficha_y)
        contador_empate+=1
        if hay_ganador(tablero):
            print jugador_y,MENSAJE_1
            break
        if empate(contador_empate,tablero):
            print MENSAJE_2
            break

def main():
    """Juego 4 en linea"""
    
    generar_cabeceras(CABECERAS)
    generar_tablero(TABLERO_VACIO)
    detener_programa = "1"
    #centinela para finalizar/resetear el juego una vez finalizado
    while detener_programa.isdigit() and detener_programa == "1":
        contador_empate = 0
        tablero_para_jugar = [x[:] for x in TABLERO_VACIO]
        # Duplica la la lista y la sublista
        jugador_1,jugador_2 = pedir_nombres()
        ciclo_de_juego(tablero_para_jugar,jugador_1,jugador_2,FICHA_1,FICHA_2,contador_empate)
        detener_programa =\
        raw_input("Ingrese 1 si desea volver a jugar, caso contrario cualquier otra cosa: ")
    
    

main()
