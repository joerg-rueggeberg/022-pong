from turtle import Turtle

MOVE_DIST = 20


class Paddles(Turtle):
    def __init__(self, coord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(1, 5)
        self.pu()
        self.setpos(coord)

    def up(self):
        self.fd(MOVE_DIST)

    def down(self):
        self.bk(MOVE_DIST)
