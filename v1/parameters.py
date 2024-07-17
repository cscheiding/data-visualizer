# Parámetros de las ventanas de inicio y juego:
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
MAIN_BACKGROUND_COLOR = 'gray'
SECONDARY_BACKGROUND_COLOR = 'darkgrey'
# ANCHO_LOGO = 200
# ALTURA_LOGO = 200
# Popup:
ALTURA_VENTANA_EMERGENTE = 100
ANCHO_VENTANA_EMERGENTE = 100
# Parámetros de la ventana de juego:
FILA_INICIAL_PEPA = 0
COLUMNA_INICIAL_PEPA = 0
TIEMPO_TIMER_MOVIMIENTO = 100 # Milisegundos entre cada sprite, para cada movimiento
TIEMPO_TRANSICION = 3 # Segundos
TIEMPO_JUEGO = 5 # Segundos
TIEMPO_ADICIONAL = 10 # Segundos
TIEMPO_APARICION = 2 # Segundos
TIEMPO_DURACION = 5 # Segundos
TIEMPO_REFRESCO_EFECTO_SONIDO = 100 # Cada cuántos milisegundos revisa si el sonido terminó
# Cheatcodes:
## Se deben presionar las teclas M + U + T + E para silenciar la ventana, con un intervalo de
## tiempo entre cada par de teclas de hasta esta cantidad de milisegundos:
TIEMPO_PRESION_TECLAS_SILENCIAR = 1000
## Lo mismo para las teclas I + N + F:
TIEMPO_PRESION_TECLAS_INFINITO = 1000
PUNTAJE_INF = 10
# Conexión con el servidor:
BYTES_MAXIMOS = 4096 # Bytes máximos del mensaje que recibe el cliente desde el servidor
# Parámetros del back-end:
CONSTANTE = 5