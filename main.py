import pgzrun

# -- constantes

WIDTH = 800
HEIGHT = 600
ROWS = 7

# -- variables globales

# ** bricks **
bricks = []
for y in range(0, 30 * ROWS, 30):
    for x in range(0, WIDTH, 100):
        brick = Actor("brick", anchor=["left", "top"])
        brick.pos = [x, y]
        bricks.append(brick)


# ** player **
player = Actor("player")
player.pos = [WIDTH/2, HEIGHT - 50]


# ** ball **

ball = Actor("ball")
ball.pos = [WIDTH/2, HEIGHT - 100]

ball_speed = [240, -240]

# -- fonctions

def draw():
    screen.clear()
    for brick in bricks:
        brick.draw()
        
    player.draw()
    ball.draw()

# -- programme principal

def update(dt):

    if dt > 0.5:
        return
    # *** mouvement de la balle ***
    pos = ball.pos
    mvt_x = ball_speed[0] * dt
    mvt_y = ball_speed[1] * dt
    pos = [pos[0] + mvt_x, pos[1] + mvt_y]

    if pos[0] > WIDTH - 10:
        pos[0] = WIDTH - 10
    elif pos[0] < 10:
        pos[0] = 10

    if pos[1] > HEIGHT - 10:
        pos[1] = HEIGHT - 10
    elif pos[1] < 10:
        pos[1] = 10

    ball.pos = pos



    # *** collision avec l'écran ***
    if ball.pos[0] >= WIDTH - 10 or ball.pos[0] <= 10:
        invert_horizontal_speed()

    if ball.pos[1] <= 10 or ball.pos[1] >= HEIGHT -10:
        invert_vertical_speed()

    # *** collision avec le player ***

    if ball.colliderect(player):
        invert_vertical_speed()

    # *** collision avec les briques

    for brick in bricks:
        if ball.colliderect(brick):
            invert_vertical_speed()
            bricks.remove(brick)
            break


def on_mouse_move(pos):
    x = pos[0]
    y = player.pos[1]
    player.pos = [x, y]


def invert_horizontal_speed():
    ball_speed[0] *= -1

def invert_vertical_speed():
    ball_speed[1] *= -1

def on_key_down(key):
    if key == keys.SPACE:
        invert_horizontal_speed()

pgzrun.go()