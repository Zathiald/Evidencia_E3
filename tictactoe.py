"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""


# Importamos el módulo turtle
import turtle
from freegames import line

# Inicializa el tablero como una lista de listas
board = [['' for _ in range(3)] for _ in range(3)]


# Dibujamos la cuadrícula del juego tic-tac-toe.
def grid():
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


# Dibujamos el jugador X
def drawx(x, y):
    turtle.color('red')
    turtle.width(2.5)
    line(x + 35, y + 33, x + 100, y + 100)
    line(x + 35, y + 100, x + 100, y + 33)


# Dibujamos el jugador O
def drawo(x, y):
    turtle.color('blue')
    turtle.width(3)
    turtle.up()
    turtle.goto(x + 67, y + 33)
    turtle.down()
    turtle.circle(33)


# Redondeamos el valor hacia abajo a la cuadrícula con tamaño de cuadrado 133.
def floor(value):
    return ((value + 200) // 133) * 133 - 200


# Inicializamos el estado del juego
state = {'player': 0}
players = [drawx, drawo]


# Dibujamos X o O en el cuadrado seleccionado.
def tap(x, y):
    x = floor(x)
    y = floor(y)

    # Convertimos las coordenadas a índices de la lista
    i, j = int((x + 200) // 133), int((y + 200) // 133)
    # Verificamos si la casilla está vacía
    if board[i][j] == '':
        player = state['player']
        draw = players[player]
        draw(x, y)
        board[i][j] = 'X' if player == 0 else 'O'
        turtle.update()
        state['player'] = not player


# Configuramos la ventana del juego
turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
grid()
turtle.update()
turtle.onscreenclick(tap)
turtle.done()
