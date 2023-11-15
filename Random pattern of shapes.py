import turtle
import random


def draw_random_pattern():
    turtle.speed(2)

    for _ in range(36):
        size = random.randint(50, 200)
        turtle.pensize(random.randint(1, 5))
        turtle.pencolor(random.random(), random.random(), random.random())

        for _ in range(4):
            turtle.forward(size)
            turtle.right(90)

        turtle.right(10)

    turtle.done()


if __name__ == "__main__":
    draw_random_pattern()
