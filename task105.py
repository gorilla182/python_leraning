import turtle
from math import log
import os
from colorsys import hsv_to_rgb

WIDTH = 800
X_RANGE = 3.4
ASPECT_RATIO = 4/3
PRECISION = 100
HEIGHT = round(WIDTH / ASPECT_RATIO)
Y_RANGE = X_RANGE / ASPECT_RATIO
MIN_X = -X_RANGE / 2
MAX_X = X_RANGE / 2
MIN_Y = -Y_RANGE / 2
MAX_Y = Y_RANGE / 2
STEP = 2


def power_color(distance, exp, const, scale):
    factor = distance ** exp
    return hsv_to_rgb(const + scale * factor, 1 - 0.6 * factor, 0.9)


def log_color(distance, base, const, scale):
    color = -1 * log(distance, base)
    return hsv_to_rgb(const + scale * color, 0.8, 0.9)


turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0)
turtle.colormode(1.0)


for y in range(0, HEIGHT, STEP):
    zy = y * (MAX_Y - MIN_Y) / (HEIGHT - 1) + MIN_Y
    for x in range(0, WIDTH, STEP):
        zx = x * (MAX_X - MIN_X) / (HEIGHT - 1) + MIN_X
        z = zx + zy * 1j
        c = z
        for i in range(PRECISION):
            if abs(z) > 2.0:
                break
            z = z * z + c
        distance = (i + 1) / (PRECISION + 1)
        turtle.color(log_color(distance, 10, 0.27, 1.0))
        turtle.setposition(x - WIDTH // 2, y - HEIGHT // 2)
        turtle.pendown()
        turtle.dot(2 * STEP)
        turtle.penup()

turtle.update()
turtle.done()
