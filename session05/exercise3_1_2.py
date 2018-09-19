import turtle
from turtle_shape import arc, circle, move, polygon


def petal(t, r, angle):
    """Draws a petal using two arcs.

    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)


def flower(t, n, r, angle):
    """Draws a flower with n petals.

    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0 / n)


jack = turtle.Turtle()

# draw a sequence of three flowers, as shown in the book.
move(jack, -100, 0)
flower(jack, 7, 60.0, 60.0)

move(jack, 0, 0)
flower(jack, 10, 40.0, 80.0)

move(jack, 100, 0)
flower(jack, 20, 140.0, 20.0)

jack.hideturtle()
turtle.mainloop()
