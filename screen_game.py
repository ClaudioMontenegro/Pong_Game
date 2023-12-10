from turtle import Turtle

POSITIONS = list(range(-280, 320, 40))
X = 0


class PongScreen:
    def __init__(self):
        self.dashes = []
        self.middle_dashes()

    def middle_dashes(self):
        for position in POSITIONS:
            self.middle = Turtle("square")
            self.middle.color("white")
            self.middle.shapesize(1)
            self.middle.penup()
            self.middle.goto(X, position)
            self.dashes.append(self.middle)


