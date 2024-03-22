"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *

from freegames import line

# Inicializa el tablero como una lista de listas
board = [['' for _ in range(3)] for _ in range(3)]

def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    color('red')
    width(2.5)
    line(x + 35, y + 33, x + 100, y + 100)
    line(x + 35, y + 100, x + 100, y + 33)


def drawo(x, y):
    """Draw O player."""
    color('blue')
    width(3)
    up()
    goto(x + 67, y + 33)
    down()
    circle(33)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)

    # Convierte las coordenadas a índices de la lista
    i, j = int((x + 200) // 133), int((y + 200) // 133)
    
    # Verifica si la casilla está vacía
    if board[i][j] == '':
        player = state['player']
        draw = players[player]
        draw(x, y)
        board[i][j] = 'X' if player == 0 else 'O'
        update()
        state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
